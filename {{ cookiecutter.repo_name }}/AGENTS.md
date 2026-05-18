# Repository Instructions

These instructions add Hoare Lea project-specific context on top of any global Codex instructions.
Keep this file focused on information that is true for this generated project; avoid restating generic workflow guidance that already lives in `~/.codex`, `README.md`, or the `Makefile`.

## Project overview

Describe the actual Hoare Lea project here. Keep it short and concrete: the client or internal team, what the repo produces, the expected outputs, and what correct work looks like.

## Commands

- Treat `README.md` and `Makefile` as the source of truth for setup, test, lint, and run commands.
- Document only non-obvious or project-specific commands here when they exist.
- Prefer `make setup` for initial setup, `make test` for tests, and `uv run ...` for targeted Python commands unless the project documents a different workflow.

## Working defaults

- Prefer small, correct, reviewable changes over broad rewrites.
- Inspect existing code, tests, config, notebooks, and docs before guessing about project behavior.
- Find root causes before patching symptoms unless the task explicitly asks for a temporary workaround.
- Do not add production dependencies, change public interfaces, or restructure major folders without a clear project-specific reason.
{% if cookiecutter.include_streamlit_app in ['yes', 'y', 'YES', 'Y'] %}- Keep Hoare Lea Streamlit styling, assets, and visual conventions intact when editing app code.
{% endif %}

## Architecture

- `src/{{ cookiecutter.package_name }}/`: reusable project code; prefer putting durable logic here
- `tests/`: unit tests for code in `src/`
- `notebooks/`: exploration and communication; refactor stable logic back into `src/`
- `conf/`: versioned configuration
- `data/`: local data split into raw, intermediate, model input, and model output stages
{% if cookiecutter.azure_ml_project in ['yes', 'y', 'YES', 'Y'] %}- `azureml/`: Azure ML assets, environment setup, data registration, jobs, and pipeline-related scripts
{% endif %}
- `models/`: trained artifacts or model summaries
{% if cookiecutter.include_streamlit_app in ['yes', 'y', 'YES', 'Y'] %}- `app_streamlit/`: Streamlit app scaffold using Hoare Lea branding and styles
- `assets/`: Hoare Lea app assets such as logos and static styling resources
{% endif %}{% if cookiecutter.include_fastapi_app in ['yes', 'y', 'YES', 'Y'] %}- `app_fastapi/`: FastAPI app scaffold
{% endif %}
- `tasks/`: repo-local task tracking for substantial Codex work

## Task tracking

- Use `tasks/todo.md` for substantial tasks that involve multiple steps, debugging, cross-cutting edits, or meaningful verification.
- Read `tasks/decisions.md` before changing architecture, public interfaces, data contracts, modelling assumptions, workflow patterns, or other areas where prior decisions may constrain the change.
- Add an entry to `tasks/decisions.md` when the work introduces or reverses an important architectural, product, modelling, or workflow decision.
- Use `tasks/lessons.md` for repo-specific corrections, recurring gotchas, or reusable mistakes that should change future work in this repo.

## Conventions

- Keep reusable domain logic out of notebooks and app entry points when practical.
- Prefer extending existing modules under `src/{{ cookiecutter.package_name }}/` before adding parallel helpers.
- Treat raw data as immutable and keep transformations explicit in code.
- Add or update tests for non-trivial behavior changes.
- Keep documentation up to date when behavior, setup, commands, configuration, data assumptions, or user-facing workflows change.
{% if cookiecutter.azure_ml_project in ['yes', 'y', 'YES', 'Y'] %}- For Azure ML work, keep workspace-specific settings in config or environment variables rather than hard-coding them in reusable modules.
- Be careful with secrets passed to Azure ML command jobs; use Key Vault or managed identity patterns when secrets are involved.
{% endif %}

## Risk notes

- Do not commit `.env`, local data, secrets, credentials, or generated model artifacts unless the task explicitly requires it.
- Do not edit generated or derived outputs directly when the source code, config, or pipeline should change instead.
- Keep repo-level instructions specific to this project and avoid repeating generic Codex behavior from global settings.

## Verification expectations

Before saying done, run the most relevant subset of:

```bash
make test
uv build
```

For linting or formatting, use the commands documented in this repo's `Makefile` and `README.md`.
Add extra validation commands here if this project adopts them. Do not claim completion without verification; if something cannot be run, explain exactly what was blocked and what should be run next.
