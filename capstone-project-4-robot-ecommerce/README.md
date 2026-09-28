# Capstone 4: Robot Framework E-commerce Automation

Automated shopping tests for Automation Exercise using Robot Framework and SeleniumLibrary.

## Test coverage

- Log in with a demo account
- Search for Blue Top and Winter Top
- Add each product to the cart and verify its quantity
- Log out

The suite uses reusable keywords in `resources/` and test data in `data/products.py`.

## Run the tests

From this folder, with the repository virtual environment activated and `AE_TEST_EMAIL` and `AE_TEST_PASSWORD` set:

```powershell
python -m pip install -r requirements.txt
python -m robot --outputdir evidence/reports suites