# Capstone Project 3: Python API Automation with Behave BDD

This project tests the [Automation Exercise practice API](https://automationexercise.com/api_list) using Python `requests`, Behave BDD, and Allure reporting.

## Covered scenarios

* Verify login with valid demo account credentials
* Verify login with invalid credentials
* Create, retrieve, update, and delete a temporary user account

The login endpoint verifies credentials and returns a result code and message. It does not provide a bearer token. Temporary accounts use unique email addresses and are deleted after the scenario, including an attempted cleanup if a later step fails.

## Project structure

| Path                               | Purpose                                      |
| ---------------------------------- | -------------------------------------------- |
| `api/client.py`                    | Reusable HTTP client for the practice API    |
| `config/settings.py`               | API base URL and request timeout             |
| `features/*.feature`               | Gherkin scenarios                            |
| `features/steps/`                  | Behave step definitions                      |
| `features/environment.py`          | Client cleanup and temporary account cleanup |
| `evidence/reports/allure-results/` | Allure test result data                      |
| `evidence/reports/allure-report/`  | Generated HTML report                        |

## Setup

Install the Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

Set the credentials for a registered Automation Exercise demo account in the current PowerShell session:

```powershell
$env:AE_TEST_EMAIL = "your-demo-email"
$env:AE_TEST_PASSWORD = "your-demo-password"
```

Never commit actual credentials to GitHub.

## Run tests and generate the report

From this project directory, run all scenarios with the Allure formatter:

```powershell
python -m behave -f allure_behave.formatter:AllureFormatter -o evidence/reports/allure-results
```

Generate the HTML report using the Allure command-line tool:

```powershell
allure generate evidence/reports/allure-results -o evidence/reports/allure-report --clean
```

To open the generated report locally:

```powershell
allure open evidence/reports/allure-report
```

## Execution result

The latest reported run passed **3 scenarios**: two login scenarios and one temporary user management scenario. Review the generated Allure report for the execution details.

The API returns application-level `responseCode` values in its JSON responses. The scenarios check those values and the login messages.
