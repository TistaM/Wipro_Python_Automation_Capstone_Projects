import os

import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utilities.csv_reader import load_search_cases


@pytest.mark.parametrize("case", load_search_cases(), ids=lambda case: case["case_id"])
def test_login_and_search(driver, case):
    login_page = LoginPage(driver).open()
    login_page.login(
        os.environ["AE_TEST_EMAIL"],
        os.environ["AE_TEST_PASSWORD"],
    )
    assert login_page.is_logged_in()

    products_page = ProductsPage(driver).open()
    products_page.search(case["product_name"])
    assert products_page.product_is_visible(case["product_name"])