# Python Project Template

This is a starter template for Python projects used in GitHub Classroom.

## What’s Included

- Basic Python functions in `main.py`
- Unit tests in `test_main.py` using `pytest`
- Automated testing via GitHub Actions
- `requirements.txt` to install dependencies

## How to Run Tests

1. Install dependencies:

```
bash
pip install -r requirements.txt
```

2. Run tests locally:
```
pytest
```

## Functions to implement
- return0()
Returns 0.

- returnNTimesA(n, a)
Returns n * a. Currently just returns a. You should implement it.

## Yaml file:
```
name: Run Grading Tests Only

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run only grading tests
        run: |
          pytest tests/grading_test.py
```
