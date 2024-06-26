# Hoare Lea Data Science Project Template
A standardised project structure for doing and sharing data science work that enforces best practices. This template includes useful boilerplate code for Hoare Lea projects including:
* Hoare Lea fonts, colors, logos and css styles added to streamlit apps by default
* Utility functions for generating plotly data visualisations in the Hoare Lea style
* Utility functions for connecting to company data sources (FUTURE)

The goal of this template is to maintain modularity and separation of concerns:
- **Shared Code**: All reusable code should reside in the `src` directory.
- **Apps, Pipelines, and Notebooks**: Use the shared code in apps, pipelines, and notebooks, ensuring that your project remains clean and maintainable.

## Usage
1. Install cookiecutter.
   ```bash
   pip install cookiecutter
   ```
2. Start a new project. You will be prompted to enter some configuration values.
   ```bash
   cookiecutter gh:HoareLea/ds-project-template
   ```

## Project Structure
The directory structure of your new project looks like this:
```
├── .env                   <- Local secrets and credentials that should not be stored in source control.
├── Makefile               <- Makefile with useful commands for project setup and running analysis.
├── README.md              <- The top-level README for developers using this project.
├── app                    <- App-specific code, requirements file and Dockerfile.
├── conf                   <- Configuration files that can be stored in source control.
├── data
│   ├── 01_raw             <- The original, immutable data dump.
│   ├── 02_intermediate    <- Intermediate data that has been transformed.
│   ├── 03_model_input     <- The final, canonical data sets for modeling.
│   └── 04_model_output    <- Outputs from models (e.g. predictions).
├── models                 <- Trained and serialized models or model summaries.
├── notebooks              <- Jupyter notebooks.
├── pipelines              <- Pipeline scripts for data processing and model training.
├── pyproject.toml         <- Project metadata and dependencies.
├── references             <- Data dictionaries, manuals, and all other explanatory materials.
├── src                    <- Source code for use in this project.
│   └── package
│       ├── __init__.py    <- Make package a Python module.
│       ├── data           <- Scripts to download or generate data.
│       ├── features       <- Scripts to turn raw data into features for modeling.
│       ├── model          <- Scripts to train models and make predictions.
│       ├── utils          <- Utility functions.
│       └── visualization  <- Scripts to create exploratory and results-oriented visualizations.
└── tests                  <- Tests for functions in src.
```