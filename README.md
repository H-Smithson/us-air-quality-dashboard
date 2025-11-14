# Project Air Quality ETL and Visualisation (2000–2016)

The Air Quality ETL and Visualisation project is an end-to-end data analysis workflow designed to clean, transform, and explore U.S. air pollution data from 2000 to 2016. The project focuses on scalable ETL processing, automated feature creation, pollutant unit standardisation, and generating a Power BI–ready dataset supported by meaningful exploratory visualisations.

## Dataset Content

The dataset used for this project is the U.S. Air Pollution Dataset (2000–2016), originally sourced from Kaggle. It contains approximately 1.7 million rows of pollutant measurements recorded across thousands of monitoring sites in the United States.

Key fields include:

Date Local (daily readings)

Pollutant measures: NO2, O3, SO2, CO

Pollutant AQI values

Pollutant measurement units

Site identifiers (State, County, City, Site ID)

Geolocation fields (latitude, longitude)

## Business Requirements

The business requirements for the project are as follows:

Clean and standardise the raw dataset for advanced analysis.

Create time series features.

Generate initial visualisations to support exploratory data analysis.

Produce high-level insights that could support environmental monitoring, policy decision-making, or public health analysis.

Create an interactive dashboard for data visualization.

## Hypothesis and how to validate?

Hypotheses for this project:

Air pollution levels vary significantly by quarter.
Validation: Analyse monthly and quarterly averages for each pollutant.

Pollutant levels show long-term improvement from 2000 to 2016.
Validation: Plot pollutant means over time and check for downward trends.

Certain pollutants may be strongly correlated.
Validation: Generate correlation matrices and heatmaps.

Pollution patterns differ substantially by state or region.
Validation: Group pollutant measurements by state and compare distributions.

## Project Management

Tasks were divided up amongst the team.

A project board was created with 'issues' to assist the management of delivery.

A team group chat was used to keep on top of issues (see above) and agree solutions.

Progress was monitored and alternative solutions identified where hardware and software constraints caused delays.

## Dashboard design

The Power BI dashboard was created as a stand-alone tool for those with an interest in air quality. It's designed to enable the user to select specific US states and/or years to see how the 4 air quality indicators measured during that time period, to be able to make informed decisions regarding which gases/seasons to target any measures towards.

Addition of longitude and latitude data was required in order to overcome Azure maps' confusion with US county names when those names represent more than one location in the world.

## Use of Generative AI Tools:

ChatGPT was used for ideation, documentation drafting, code optimisation, ETL logic refinement, and problem-solving when encountering edge cases.

All outputs were checked manually for correctness.

## Ethical considerations

The dataset contains no personal or sensitive information, so privacy is not a concern.

## Challenges

ETL Pipelining was difficult due to dataset and machine being used to create, slowing initial work on the project.

## Solutions

To work around the issue, ETL was directly embedded within Power Bi dashboard as an alternative approach as one that could be deployed at speed and still provide an MVP for users.

## Main Data Analysis Libraries

pandas
numpy 
matplotlib 
seaborn 
pathlib 

## Credits

Content was created using the Code Institute repo template.

Code content was based on the Learning Management System content provided by the Code Institute.

Copilot and ChatGPT were both used for coding, assistance in developing hypotheses and sense checking approaches and outputs.

### Datasets

Pollution dataset sourced from Kaggle (U.S. Pollution 2000–2016). <https://www.kaggle.com/datasets/sogun3/uspollution>
US latitude and longitude for counties was supplied by SimpleMaps.com <https://simplemaps.com/data/us-counties>

### Acknowledgements:

Thanks to Code Institute instructors and peers.