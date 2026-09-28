# Capstone Project 2: Selenium Python Automation Framework

This project tests login and product search on [Automation Exercise](https://automationexercise.com/) using Selenium WebDriver with Python. It provides separate **pytest** and **unittest** suites that share Page Object Model classes, CSV test data, and central configuration.

## Features

* Page objects for the login and products pages
* Product search cases loaded from `data/search_cases.csv`
* Separate pytest and unittest test suites
* Configurable base URL and explicit wait duration
* Screenshots saved when a test fails
* HTML execution report for pytest

## Project structure

| Path                      | Purpose                                        |
| ------------------------- | ---------------------------------------------- |
| `pages/`                  | Login and products page objects                |
| `config/settings.py`      | Base URL and wait settings                     |
| `utilities/csv_reader.py` | Reads search cases from CSV                    |
| `data/search_cases.csv`   | Product search test data                       |
| `tests_pytest/`           | Parameterized pytest tests and browser fixture |
| `tests_unittest/`         | Unittest suite with CSV subtests               |
| `evidence/reports/`       | Generated pytest HTML report                   |
| `evidence/screenshots/`   | Screenshots created if a test fails            |

## Requirements

* Python 3
* Google Chrome
* An Automation Exercise demo account

Install the Python packages from this project folder:

```powershell
python -m pip install -r requirements.txt
```

Set the demo account credentials in the current PowerShell session:

```powershell
$env:AE_TEST_EMAIL = "your-demo-email"
$env:AE_TEST_PASSWORD = "your-demo-password"
```

Do not put your actual password in the CSV, source code, or GitHub repository.

## Run the tests

Run pytest and generate the HTML report:

```powershell
python -m pytest tests_pytest -v --html=evidence/reports/pytest-report.html --self-contained-html
```

Run unittest:

```powershell
python -m unittest discover -s tests_unittest -p "test_*.py" -v
```

The pytest suite runs one test per CSV row. The unittest suite checks the CSV rows as subtests within one test method.

## Configuration

`config/settings.py` uses `https://automationexercise.com` and a 15-second explicit wait by default. To override either value for a run, set `AE_BASE_URL` or `AE_WAIT_SECONDS` in PowerShell before executing the tests.

## Results and evidence

* Pytest: **2 passed** in the latest reported run.
* Unittest: **1 test, OK** in the latest reported run; it checks both CSV cases as subtests.
* Pytest HTML report: [`evidence/reports/pytest-report.html`](evidence/reports/pytest-report.html)
* Failure screenshots: generated in `evidence/screenshots/` only when a test fails.

