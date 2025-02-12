# Hoare Lea Data Science Project Template
A standardised project template aimed at beginner level python users. The template aims to encourage best-practices for structuring and sharing data work. Additionally, the template includes useful code for common data science operations including:
* Processing and cleaning data
* Generating plotly data visualisations in the Hoare Lea style
* Utilities for executing miscellaneous tasks

The goal of this template is to maintain modularity and separation of concerns:
- **Shared Code**: All reusable code should reside in the `src` directory.
- **Notebooks**: Use the shared code in notebooks, ensuring that your project remains clean and maintainable.

## Usage
1. Install cookiecutter.
   ```bash
   pip install cookiecutter
   ```
2. Start a new project. You will be prompted to enter some configuration values.
   ```bash
   cookiecutter gh:HoareLea/ds-project-template -c python-template
   ```

## Technologies
This project template comes with several tools designed to improve code quality and development efficiency.
- **[Jupyter](https://jupyter.org/)**: Jupyter Notebooks are a popular tool for data exploration and communication. They allow you to write and run code in an interactive environment, which is particularly useful for data analysis and visualization. Note that Jupyter is intended for exploration and not for production code.
- **Makefile**: A Makefile is included to simplify running common commands. It helps you automate repetitive tasks, such as setting up your environment, running tests, or building your application. Using a Makefile can save time and reduce the potential for errors.

## Project Structure
The directory structure of your new project looks like this:
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
