# Project-5: COVID-19 Analysis

## Problem Statements:

### what are our problem statements

## Table of Contents

make a fancy hyperlink section here

explain how to look at our repo

## Executive Summary:

put what we did here

put link to our apps here, add screenshots of each app

### List of Deployed Applications:

#### Vivian Nguyen
![img](assets/images/vivian_app.png)
* [Heroku: US Covid Metric Snapshots](https://dsir824-covid19-example.herokuapp.com)
    * [Source Code for Application](https://github.com/ga-dsir824-collab/covid19-over-time)
    
#### Alex Fioto
* App
    * Source Code

#### Varun Mohan
* App
    * Source Code

## Data and Methodology:

show raw data that we found, put here

show how we modified the data, add data engineering

show our process to finding potential solutions for our problem statements

talk about data limitations about mask sentiment

## Findings:

talk about what we found

talk about visualizations

talk about our hypothesis

## Future:

talk about future development

## File Structure

SAMPLE FILE STRUCTURE, UPDATE BEFORE FINAL SUBMISSION

```bash
project-5
├── 01-EDA_summarized.ipynb
├── 02-Creating_Datasets.ipynb
├── 03-Modeling.ipynb
├── alex
│   ├── ALEX-EDA.ipynb
│   ├── democrat_mask.png
│   ├── hmm_plotting_function.ipynb
│   ├── mo_vs_ma.png
│   ├── nd_vs_ri.png
│   ├── neg_mask_cases.png
│   ├── Percent Change.ipynb
│   ├── plotly-maps.ipynb
│   ├── pos_mask_cases.png
│   ├── rate_plot_function.ipynb
│   ├── republican_mask.png
│   ├── TimeSeries.ipynb
│   ├── Top 5 Neg.png
│   ├── Top 5 Pos.png
│   ├── total_us_cases_deaths.png
│   ├── Total US Cases.png
│   ├── Total US Deaths.png
│   └── updated_hmm_plotting.ipynb
├── assets
│   └── images
│       └── vivian_app.png
├── data
│   ├── 2016election.csv
│   ├── county.csv
│   ├── covid_mask_political_combined.csv
│   ├── covid_metrics_full_time.csv
│   ├── mask-use-by-county.csv
│   ├── sme.csv
│   ├── state.csv
│   ├── two_month_snapshot.csv
│   ├── us-states.csv
│   └── ZIP-COUNTY-FIPS_2018-03.csv
├── project.md
├── README.md
├── varun_stuff
│   ├── hmm_plotting_function.ipynb
│   ├── us-states.csv
│   ├── VarunCaseDeathEDA-Copy1.ipynb
│   └── VarunCaseDeathEDA.ipynb
└── vivian_fork
    ├── annotating_plots_labels.ipynb
    ├── brainstorming.md
    ├── combined_political_covid_percent.csv
    ├── combine.ipynb
    ├── correlation.png
    ├── covid_mask_political_combined.csv
    ├── demo_streamlit
    │   ├── main.py
    │   └── test.py
    ├── EDA_and_graphs.ipynb
    ├── fancy_heatmap.py
    ├── interactrive_test.ipynb
    ├── __pycache__
    │   ├── fancy_heatmap.cpython-38.pyc
    │   └── us_states.cpython-38.pyc
    ├── us_states.py
    ├── uwu.txt
    └── web_app
        ├── demo.py
        ├── main.py
        ├── __pycache__
        │   └── us_states.cpython-38.pyc
        ├── README.md
        ├── requirements.txt
        ├── setup.sh
        └── us_states.py

10 directories, 60 files

```

## Data Dictionaries

### sme.csv

This data was combined from these sources:
LIST SOURCES

|    name     |  type   | description |
|-------------|---------|-------------|
STATE         | object  | U.S. State
NEVER         | float64 | NYT Survey: Survey Response of Mask Sentiment
RARELY        | float64 | NYT Survey: Survey Response of Mask Sentiment
SOMETIMES     | float64 | NYT Survey: Survey Response of Mask Sentiment
FREQUENTLY    | float64 | NYT Survey: Survey Response of Mask Sentiment
ALWAYS        | float64 | NYT Survey: Survey Response of Mask Sentiment
mask_negative | float64 | Engineered Column: NEVER + RARELY
mask_positive | float64 | Engineered Column: SOMETIMES + FREQUENTLY + ALWAYS
votesDem      | int64   | 2016 Election: Democratic Votes
percD         | float64 | 2016 Election: % Democratic Voters
votesRep      | int64   | 2016 Election: Republican Voters
percR         | float64 | 2016 Election: % Republican Voters
electoralDem  | int64   | 2016 Election: Democratic Electoral College Count
electoralRep  | int64   | 2016 Election: Republican ELectoral College Count
Pop           | int64   | 2016 Election: Population of U.S. State
blue          | int64   | Engineered Column: Boolean for political party
red           | int64   | Engineered Column: Boolean for political party


### covid_metrics_full_time.csv

This data is entirely from [New York Times](https://github.com/nytimes/covid-19-data)'s COVID-19 Data. For our purposes we combined it 

VARUN TALK ABOUT WHAT YOU DID TO COMBINE IT

| name  |  type  |description|
|-------|--------|-----------|
|date   | object | Date Data Collected
|state  | object | U.S. State
|fips   | int64  | Federal Information Processing Standards: State Label
|cases  | int64  | Cumulative Count of COVID-19 Cases
|deaths | int64  | Cumulative Count of COVID-19 Deaths