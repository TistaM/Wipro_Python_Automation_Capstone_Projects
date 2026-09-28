# Capstone Project 1: Selenium E-Commerce Automation

This project automates an e-commerce shopping flow on [Automation Exercise](https://automationexercise.com/) using Python, Selenium WebDriver, and pytest.

## Automated flow

1. Launch Chrome and log in with a demo account.
2. Remove an existing instance of the selected product from the cart so repeated runs start cleanly.
3. Search for **Blue Top** and open its product page.
4. Set the quantity to **2** and add the product to the cart.
5. Verify the product name, quantity, unit price, and total.

Test data is read from `data/test_data.json`. Login credentials are read from environment variables and are not stored in the repository.

## Requirements

* Python 3
* Google Chrome
* A registered Automation Exercise demo account

## Setup and execution

From the `capstone-project-1-selenium` directory, install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Set your demo account credentials in the current PowerShell session:

```powershell
$env:AE_TEST_EMAIL = "your-demo-email"
$env:AE_TEST_PASSWORD = "your-demo-password"
```

Run the complete flow and generate an HTML report:

```powershell
python -m pytest tests/test_purchase_flow.py -v --html=evidence/reports/execution-report.html --self-contained-html
```

Do not commit your credentials or virtual environment to GitHub.

## Project files

| Path                                     | Purpose                                                              |
| ---------------------------------------- | -------------------------------------------------------------------- |
| `pages/`                                 | Selenium page classes for login, products, product details, and cart |
| `tests/test_purchase_flow.py`            | Complete e-commerce flow and assertions                              |
| `tests/conftest.py`                      | Browser setup and teardown                                           |
| `data/test_data.json`                    | Product and expected cart values                                     |
| `evidence/reports/execution-report.html` | HTML report from a test run                                         

## Execution evidence

* HTML report: [`evidence/reports/execution-report.html`](evidence/reports/execution-report.html)
