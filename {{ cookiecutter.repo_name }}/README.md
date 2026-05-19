# {{ cookiecutter.project_name }}
{{ cookiecutter.description }}

## Project Structure
```
├── .env                   <- Local config and secrets that should not be stored in source control.
{% if cookiecutter.include_codex_scaffolding in ['yes', 'y', 'YES', 'Y'] -%}
├── AGENTS.md              <- Repo-local Codex instructions for this project.
{% endif -%}
├── Makefile               <- Makefile with useful commands for project setup and running analysis.
├── README.md              <- The top-level README for developers using this project.
├── app                    <- App-specific code, requirements file and Dockerfile.
├── assets                 <- Assets for use in web-apps.
├── azureml                <- Scripts for creating Azure ML assets and running jobs.
├── conf                   <- Configuration files that can be stored in source control.
├── data
│   ├── 01_raw             <- The original, immutable data dump.
│   ├── 02_intermediate    <- Intermediate data that has been transformed.
│   ├── 03_model_input     <- The final, canonical data sets for modeling.
│   └── 04_model_output    <- Outputs from models (e.g. predictions).
├── models                 <- Trained and serialized models or model summaries.
├── notebooks              <- Jupyter notebooks.
├── pyproject.toml         <- Project metadata and dependencies.
├── .python-version        <- Specifies the version of Python to use
├── references             <- Data dictionaries, manuals, and all other explanatory materials.
├── src                    <- Source code for use in this project.
│   └── {{ cookiecutter.package_name }}
│       ├── __init__.py    <- Make {{ cookiecutter.package_name }} a Python module.
│       ├── data           <- Scripts to download or generate data.
│       ├── features       <- Scripts to turn raw data into features for modeling.
│       ├── model          <- Scripts to train models and make predictions.
│       ├── utils          <- Utility functions.
│       └── visualization  <- Scripts to create exploratory and results-oriented visualizations.
{% if cookiecutter.include_codex_scaffolding in ['yes', 'y', 'YES', 'Y'] -%}
├── tasks                  <- Repo-local task tracking, lessons, and decisions for substantial Codex work.
{% endif -%}
└── tests                  <- Tests for functions in src.
```

## Getting Started

### Setup

1. **Build project, create virtual environment (venv) and install dependencies using uv**:
   ```bash
   make setup
   ```

2. **Activate virtual environment**:
   ```bash
   source .venv/bin/activate
   ```

3. **Make Initial Commit**:
   ```bash
   git add .
   git commit -m "Initial commit"
   ```

4. **Update Environment Variables**:
Much of the codebase is reliant on environment variables. Set any relevant variables in the `.env` file.
**Please Note: You can define secrets in `.env` but note that any variables passed in the definition of an Azure ML command job will be exposed. In this case, use Key Vault.**

{% if cookiecutter.include_codex_scaffolding in ['yes', 'y', 'YES', 'Y'] -%}
### Codex Support Files

This project includes optional repo-local Codex scaffolding:

- `AGENTS.md`: project-specific Hoare Lea instructions that complement any global `~/.codex` settings
- `tasks/todo.md`: a lightweight plan/progress file for substantial tasks
- `tasks/lessons.md`: repo-specific lessons and recurring gotchas
- `tasks/decisions.md`: notable architectural, modelling, or workflow decisions

If you plan to use Codex in this repo, update `AGENTS.md` early and replace the placeholder sections with the real project context, datasets, outputs, constraints, and any important local conventions.

These files make the repo more self-contained when used across machines with different Codex global configuration.

{% endif -%}

### Usage

#### Azure ML
- **Component Registration**: There is boilerplate code in `azureml` for creating and registering data assets and environments.
- **Jobs and Pipelines**: Azure ML Jobs should be defined and run from the `azureml` directory. These can be orchestrated using the Azure ML Pipelines service.
- **Utility Functions**: There are a number of utility functions for interacting with Azure ML in the `{{cookiecutter.package_name}}.utils.azure_ml` module. 

#### Data

- **Immutability**: Raw data should not be edited. Transform data through your processing pipeline.
- **Local Directory Structure**: Organize any local data into `01_raw`, `02_intermediate`, `03_model_input`, and `04_model_output`.
- **Cloud Data Storage**: If using Azure ML you should upload data to Datastores. To create a local copy of any registered data assets use the `{{cookiecutter.package_name}}.utils.azure_ml.sync_data_local` function.

#### Code Quality

-- **Ruff**: Ruff provides fast linting and auto-fixing for Python code, combining functionality of tools like Flake8 and Black for streamlined code quality.
- **pytest**: The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

#### Notebooks

- **Purpose**: Notebooks are for exploration and communication. Refactor useful code into the `src` directory.
- **nbstripout**: Notebook output should ~not~ rarely be committed to source control because it creates ugly diffs and risks data leakage. Nbstripout is installed as a pre-commit hook. It can be ignored by setting the ```"keep_output": true``` metadata on a cell.
- **Auto-reloading**:
  ```python🚡
  %load_ext autoreload
  %autoreload 2
  ```

#### Applications

- **Streamlit and FastAPI**: If selected, templates are provided with `requirements.txt` and `Dockerfile` for building containerized apps.

### Database Connections

- **Database Connections**: If selected, utility functions for database connections are in `utils/db.py`. Configuration settings are added to `.env`.

### Project Philosophy

The goal is to maintain modularity and separation of concerns:
- **Shared Code**: All reusable code should reside in the `src/{{ cookiecutter.package_name }}` directory.
- **Apps, Pipelines, and Notebooks**: Use the shared code in apps, pipelines, and notebooks, ensuring that your project remains clean and maintainable.
