import os

from pages.login_page import LoginPage


def test_login_with_valid_account(driver):
    email = os.environ["AE_TEST_EMAIL"]
    password = os.environ["AE_TEST_PASSWORD"]

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(email, password)

    assert login_page.is_logged_in(), "Login was not successful"