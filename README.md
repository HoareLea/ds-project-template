# Hoare Lea Data Science Project Template
A standardised project structure for doing and sharing data science work that enforces best practices. This template includes useful boilerplate code for Hoare Lea projects including:
* Templates and boilerplate code for interacting with Azure ML workspaces
* Hoare Lea fonts, colors, logos and css styles added to streamlit apps by default
* Utility functions for generating plotly data visualisations in the Hoare Lea style

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

## Template Options
The prompt set is intended to keep generated projects lean while preserving Hoare Lea defaults. The main toggles are:

- `include_agent_scaffolding`: include `AGENTS.md`, `CONTEXT.md`, `docs/adr/`, and lightweight `tasks/` scratch files
- `include_streamlit_app`: include a starter Streamlit app with Hoare Lea branding under `app_streamlit/`
- `include_fastapi_app`: include a starter FastAPI app under `app_fastapi/`
- `azure_ml_project`: include Azure ML assets, jobs, and helper utilities
- `database_type`: include database utility code and matching dependencies

If `include_agent_scaffolding=no`, the generated project will not include `AGENTS.md`, `CONTEXT.md`, `docs/adr/`, or `tasks/`.

## Technologies
This project template comes with several tools designed to improve code quality and development efficiency. Some tools are included by default, while others are optional and can be chosen during the setup process.
- **[Jupyter](https://jupyter.org/)**: Jupyter Notebooks are a popular tool for data exploration and communication. They allow you to write and run code in an interactive environment, which is particularly useful for data analysis and visualization. Note that Jupyter is intended for exploration and not for production code.
- **[pytest](https://docs.pytest.org/en/)**: pytest is a testing framework for Python that makes it easy to write simple and scalable test cases. Using pytest helps ensure that your code is working correctly and can catch issues early in the development process.
- **[Docker](https://www.docker.com/)**: Docker is a platform that allows you to create, deploy, and run applications in containers. Containers are lightweight and portable, making it easy to share and run your project in any environment. Including Docker ensures that your project can be consistently run anywhere, from your local machine to a production server.
- **Makefile**: A Makefile is included to simplify running common commands. It helps you automate repetitive tasks, such as setting up your environment, running tests, or building your application. Using a Makefile can save time and reduce the potential for errors.

#### Pre-Commit Hooks
Pre-commit hooks are scripts that run automatically before you make a commit in your version control system (e.g., Git). They help ensure that your code meets certain standards before it is saved to the repository.
- **[ruff](https://github.com/astral-sh/ruff-pre-commit)**: Ruff provides fast code formatting and auto-fixing, combining functionality of tools like Flake8 and Black for streamlined code quality. It helps to avoid debates about coding style so you can focus on what the code actually does
- **[nbstripout](https://github.com/kynan/nbstripout)**: Nbstripout is a tool to strip output from Jupyter notebooks. This is useful for keeping your version control history clean by removing potentially large and unnecessary output data from the notebooks, making them easier to review and manage.

#### Optional Tools
During the setup process, you can choose to include the following optional tools. If selected, relevant boilerplate code and configuration will be added to your project.
- **Agent Scaffolding**: Adds repo-local `AGENTS.md`, `CONTEXT.md`, ADR docs, and lightweight `tasks/` files so AI agents and contributors have project-specific operating instructions, domain context, lessons, and durable decision records inside the generated repository.
- **[Azure ML](https://azure.microsoft.com/en-us/products/machine-learning)**: Azure Machine Learning is the preferred service for performing data science work at Hoare Lea. It can be used to provision compute and storage resources and has features for supporting the full ML lifecycle.
- **[Streamlit](https://streamlit.io/)**: Streamlit is a framework for creating web applications from Python scripts. It is especially useful for creating interactive data applications and dashboards with minimal effort. Including Streamlit allows you to build and share interactive data apps quickly.
- **[FastAPI](https://fastapi.tiangolo.com/)**: FastAPI is a modern, fast (high-performance) web framework for building APIs with Python. It is designed for creating RESTful APIs easily and efficiently. If you need to expose your models or data processing as APIs, FastAPI is a great choice.
- **Database Connections**: You can choose to connect to PostgreSQL or MySQL databases. If selected, helper functions will be created in the `utils` section of the local package. Update the `.env` file with the relevant database connection details to use these functions.

## Project Structure
The directory structure of your new project looks like this:
```
├── .env                   <- Local secrets and credentials that should not be stored in source control.
├── AGENTS.md              <- Optional repo-local agent instructions for the generated project.
├── CONTEXT.md             <- Optional domain context for agents and contributors.
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
├── pipelines              <- Pipeline scripts for data processing and model training.
├── pyproject.toml         <- Project metadata and dependencies.
├── references             <- Data dictionaries, manuals, and all other explanatory materials.
├── docs
│   └── adr                <- Optional architecture decision records.
├── src                    <- Source code for use in this project.
│   └── package
│       ├── __init__.py    <- Make package a Python module.
│       ├── data           <- Scripts to download or generate data.
│       ├── features       <- Scripts to turn raw data into features for modeling.
│       ├── model          <- Scripts to train models and make predictions.
│       ├── utils          <- Utility functions.
│       └── visualization  <- Scripts to create exploratory and results-oriented visualizations.
├── tasks                  <- Optional repo-local agent scratchpad files and lessons.
└── tests                  <- Tests for functions in src.
```

Optional prompts remove their corresponding files and folders during generation.

## Agent Support

If you enable `include_agent_scaffolding`, the generated project includes lightweight agent support files that are meant to remain useful without any personal global agent configuration or optional skills.

- `AGENTS.md`: project-specific Hoare Lea guidance for commands, structure, Azure ML, data handling, and verification
- `CONTEXT.md`: project domain vocabulary, invariants, workflows, and data assumptions
- `docs/adr/README.md`: ADR purpose and starter template
- `tasks/todo.md`: an ephemeral plan/progress scratchpad for substantial active work
- `tasks/lessons.md`: repo-specific corrections and recurring gotchas

Optional agent workflow setup: this template can be paired with external engineering-skill packs for agents. One compatible setup skill is `setup-matt-pocock-skills`, which creates repo-local workflow config for issue trackers, triage labels, and domain docs. If your agent environment provides that skill, run it after generation when you want those workflow docs. If not, skip this step; the repo still works with the baseline `AGENTS.md`, `CONTEXT.md`, ADRs, and task files.

Use `AGENTS.md` for repo operating instructions and `CONTEXT.md` for domain truth. ADRs in `docs/adr/` are the durable decision record.
