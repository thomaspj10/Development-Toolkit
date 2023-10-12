# Development Toolkit
Development toolkit to increase velocity and code quality.

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
- Tags are automatically generated from a json file containing the html5 specification.
- Migration tool to convert native HTMl to the DSL.

**Logger**
- Log messages and exceptions based on a log level.
