# Project Air Quality ETL and Visualisation (2000–2016)

The Air Quality ETL and Visualisation project is an end-to-end data analysis workflow designed to clean, transform, and explore U.S. air pollution data from 2000 to 2016. The project focuses on scalable ETL processing, automated feature creation, pollutant unit standardisation, and generating a Power BI–ready dataset supported by meaningful exploratory visualisations.

# Dataset Content

The dataset used for this project is the U.S. Air Pollution Dataset (2000–2016), originally sourced from Kaggle. It contains approximately 1.7 million rows of pollutant measurements recorded across thousands of monitoring sites in the United States.

Key fields include:

Date Local (daily readings)

Pollutant measures: NO2, O3, SO2, CO

Pollutant AQI values

Pollutant measurement units

Site identifiers (State, County, City, Site ID)

Geolocation fields (latitude, longitude)


# Business Requirements

The business requirements for the project are as follows:

Clean and standardise the raw dataset for advanced analysis.

Create time series features.

Generate initial visualisations to support exploratory data analysis.

Produce high-level insights that could support environmental monitoring, policy decision-making, or public health analysis.

Create an interactive dashboard for data visualization.

# Hypothesis and how to validate?

Hypotheses for this project:

Air pollution levels vary significantly by quarter.
Validation: Analyse monthly and quarterly averages for each pollutant.

Pollutant levels show long-term improvement from 2000 to 2016.
Validation: Plot pollutant means over time and check for downward trends.

Certain pollutants may be strongly correlated.
Validation: Generate correlation matrices and heatmaps.

Pollution patterns differ substantially by state or region.
Validation: Group pollutant measurements by state and compare distributions.


# Use of Generative AI Tools:

ChatGPT was used for ideation, documentation drafting, code optimisation, ETL logic refinement, and problem-solving when encountering edge cases.

All outputs were checked manually for correctness.

# Ethical considerations

The dataset contains no personal or sensitive information, so privacy is not a concern.

# Challenges:

ETL Pipelining was difficult due to dataset and machine being used to create, slowing initial work on the project. 

# Solutions:

To work around the issue, ETL was directly embedded within PowerBi dashboard. 

# Main Data Analysis Libraries

pandas
numpy 
matplotlib 
seaborn 
pathlib 

# Credits

Content:

Dataset sourced from Kaggle (U.S. Pollution 2000–2016).

Acknowledgements:

Thanks to Code Institute instructors and peers.