This is an example repo to show you what the typical repo structure looks like.

## Setup

### Environment

Create and activate the conda environment:

```bash
conda env create -f environment.yml
conda activate example_repo
```

If the environment already exists, update it with:

```bash
conda env update -f environment.yml
```

### Package

Install this repo in editable mode so `example_repo` can be imported:

```bash
pip install -e .
```

### Pre-commit hooks

Install the Git hooks (ruff lint + format) once, after the environment is active:

```bash
pre-commit install
```

Hooks then run automatically on `git commit`. To run them on all files:

```bash
pre-commit run --all-files
```
