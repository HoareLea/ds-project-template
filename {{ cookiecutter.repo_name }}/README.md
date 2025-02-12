# {{ cookiecutter.project_name }}
{{ cookiecutter.description }}

## Project Structure
```
├── data
│   ├── 01_raw                <- The original, immutable data dump.
│   ├── 02_clean              <- Intermediate data that has been transformed.
│   ├── 03_final              <- The final data sets.
├── notebooks                 <- Jupyter notebooks.
├── src                       <- Source code for use in this project.
│   └── package
│       ├── __init__.py       <- Make package a Python module.
│       ├── process_data.py   <- Functions for processing data.
│       ├── utils.py          <- Misc functions.
│       ├── visualise_data.py <- Functions for plotting graphs.
├── .gitignore                <- Specify files not to commit to git (e.g. secrets)
├── Makefile                  <- Makefile with shortcuts for terminal commands
├── README.md                 <- The top-level README for the project. 
├── requirements.txt          <- Project dependencies
```

## Getting Started

### Setup

1. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. **Install Dependencies and Initialize Git**:
   ```bash
   git init
   make install
   ```

3. **Make Initial Commit**:
   ```bash
   git add .
   git commit -m "Initial commit"
   ```

## Usage
Tell people using you project any useful information here. 