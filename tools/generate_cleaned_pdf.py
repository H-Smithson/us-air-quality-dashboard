#!/usr/bin/env python3
"""Generate a multi-page PDF summarizing the cleaned datasets.

For each dataset this script will:
- note whether the file exists
- estimate total rows (line count minus header)
- read a small sample (up to 50 rows)
- render a summary page with columns, counts, and sample table

Output: `jupyter_notebooks/outputs/cleaned_datasets_summary.pdf`
"""
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
# Write the summary PDF next to the cleaned CSVs in `outputs/` so it's "in place"
OUT_DIR = ROOT / 'outputs'
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Use the four cleaned CSVs that exist in the outputs/ directory
FILES = {
    'clean_200_2016': ROOT / 'outputs' / 'pollution_us_200_2016_clean.csv',
    'clean_2000_2016': ROOT / 'outputs' / 'pollution_us_2000_2016_clean.csv',
    'numeric_fixed': ROOT / 'outputs' / 'pollution_us_200_2016_clean_numeric_fixed.csv',
    'standardized': ROOT / 'outputs' / 'pollution_us_200_2016_clean_numeric_standardized.csv',
}

OUT_PDF = OUT_DIR / 'cleaned_datasets_summary.pdf'

def estimate_rows(path: pathlib.Path):
    try:
        with path.open('r', encoding='utf-8', errors='ignore') as fh:
            # count lines, subtract header
            total = sum(1 for _ in fh)
        return max(total - 1, 0)
    except Exception:
        return None

def make_page(pp: PdfPages, title: str, path: pathlib.Path):
    fig, ax = plt.subplots(figsize=(11, 8.5))
    ax.axis('off')
    ax.set_title(title, fontsize=14, fontweight='bold', pad=12)

    if not path.exists():
        ax.text(0, 0.8, f'File not found: {path}', fontsize=10)
        pp.savefig(fig)
        plt.close(fig)
        return

    est = estimate_rows(path)
    ax.text(0, 0.02, f'Path: {path}', fontsize=8, wrap=True)
    ax.text(0, 0.08, f'Estimated total rows: {est if est is not None else "unknown"}', fontsize=10)

    # read a small sample
    try:
        sample = pd.read_csv(path, nrows=50)
    except Exception as e:
        ax.text(0, 0.5, f'Error reading sample: {e}', fontsize=9, wrap=True)
        pp.savefig(fig)
        plt.close(fig)
        return

    cols = ', '.join(sample.columns[:20].astype(str))
    ax.text(0, 0.14, f'Columns (first 20 shown): {cols}', fontsize=8, wrap=True)

    # prepare sample table (limit rows to 12 to keep readability)
    tbl = sample.head(12)
    # render table
    try:
        table = ax.table(cellText=tbl.values,
                         colLabels=tbl.columns,
                         cellLoc='left',
                         loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(7)
        table.scale(1, 1.2)
    except Exception:
        ax.text(0, 0.5, 'Could not render table preview (too many columns).', fontsize=9)

    pp.savefig(fig, bbox_inches='tight')
    plt.close(fig)

def main():
    with PdfPages(OUT_PDF) as pp:
        for var, path in FILES.items():
            title = f"Dataset: {var}"
            make_page(pp, title, path)

    print('Wrote PDF:', OUT_PDF)

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('Failed:', exc, file=sys.stderr)
        raise
