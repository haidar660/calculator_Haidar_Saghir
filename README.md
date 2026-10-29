# Lab 6 Automatic Build with PyBuilder

This project implements a calculator and automates its tests and package build with PyBuilder. It includes all four base operations from the lab plus the graded modulus, exponentiation, and square-root functions.

## Project structure

```text
calculator_Haidar_Saghir/
|-- src/main/python/calculator_Haidar_Saghir/__init__.py
|-- tests/unittest/calculator_Haidar_Saghir/
|   `-- test_calculator_Haidar_Saghir.py
|-- build.py
|-- Makefile
`-- requirements.txt
```

## Setup

Create and activate a virtual environment, then install PyBuilder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the required tests

Run the unit tests through PyBuilder:

```powershell
pyb run_unit_tests
```

Run the same test module directly with Python:

```powershell
$env:PYTHONPATH = "src/main/python"
python -m unittest tests.unittest.calculator_Haidar_Saghir.test_calculator_Haidar_Saghir
```

## Build the package

Run the default PyBuilder task to test and package the project:

```powershell
pyb
```

The build report and package artifacts are written under `target/`.

The verified terminal output required by the submission is saved at `screenshots/pybuilder-build.png`.

## Optional Makefile automation

The Makefile wraps the common commands from the optional part of the lab:

- `make clean` removes PyBuilder output.
- `make install_deps` installs the requirements.
- `make test` runs all unit tests through PyBuilder.
- `make build` runs the publish task and creates the distributions.
- `make all` performs every step in order.
