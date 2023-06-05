# Development Toolkit
Development toolkit to increase velocity and code quality.

![Tests](https://github.com/thomaspj10/Development-Toolkit/actions/workflows/tests.yaml/badge.svg)

## Installation
1. Go into the base directory.
2. `pip install -e .`

## Test suite
1. Run: `cd /tests/unit/`
2. Run the test suite `python -m unittest`

## Features
**Sql**
- Automatic model generation based on the database schema.
- Migrations to transform the database to a different state.
- Type safe way to execute sql queries.

**Infra**
- Define tasks which can be invoked from the terminal.

**Generators**
- Framework to dynamically generate Python code.

**Html**
- Type safe way to build html with Python.

## Examples
look into `/tests/project/` to see an example project. The project can be ran by running:
```shell
python infra.py
```
