import os
import unittest
from pathlib import Path

from selenium import webdriver

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utilities.csv_reader import load_search_cases


class LoginSearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        result = self._outcome.result
        failed_tests = result.failures + result.errors

        failed_this_test = any(
            test is self or getattr(test, "test_case", None) is self
            for test, _ in failed_tests
        )

        if failed_this_test:
            screenshot_dir = (
                Path(__file__).resolve().parents[1]
                / "evidence"
                / "screenshots"
            )
            screenshot_dir.mkdir(parents=True, exist_ok=True)
            self.driver.save_screenshot(
                str(screenshot_dir / "unittest-login-search-failure.png")
            )

        self.driver.quit()

    def test_login_and_csv_product_searches(self):
        login_page = LoginPage(self.driver).open()
        login_page.login(
            os.environ["AE_TEST_EMAIL"],
            os.environ["AE_TEST_PASSWORD"],
        )
        self.assertTrue(login_page.is_logged_in())

        for case in load_search_cases():
            with self.subTest(case_id=case["case_id"]):
                products_page = ProductsPage(self.driver).open()
                products_page.search(case["product_name"])
                self.assertTrue(
                    products_page.product_is_visible(case["product_name"])
                )


if __name__ == "__main__":
    unittest.main()