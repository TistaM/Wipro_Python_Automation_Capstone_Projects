from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def product_row(self, product_name):
        return self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//tr[.//a[normalize-space()='{product_name}']]",
                )
            )
        )

    def product_quantity(self, product_name):
        row = self.product_row(product_name)
        return row.find_element(
            By.CSS_SELECTOR, ".cart_quantity button"
        ).text.strip()

    def product_price(self, product_name):
        row = self.product_row(product_name)
        return row.find_element(
            By.CSS_SELECTOR, ".cart_price"
        ).text.strip()

    def product_total(self, product_name):
        row = self.product_row(product_name)
        return row.find_element(
            By.CSS_SELECTOR, ".cart_total"
        ).text.strip()

    def remove_product_if_present(self, product_name):
        self.driver.get("https://automationexercise.com/view_cart")

        row_locator = (
            By.XPATH,
            f"//tr[.//a[normalize-space()='{product_name}']]",
        )

        # Wait for the cart to finish loading.
        self.wait.until(
            EC.presence_of_element_located((By.ID, "cart_info"))
        )

        rows = self.driver.find_elements(*row_locator)
        if rows:
            rows[0].find_element(
                By.CSS_SELECTOR, ".cart_quantity_delete"
            ).click()
            self.wait.until(
                EC.invisibility_of_element_located(row_locator)
            )

        # Reload to verify the item was removed from the site's cart.
        self.driver.refresh()
        self.wait.until(
            EC.presence_of_element_located((By.ID, "cart_info"))
        )
        assert not self.driver.find_elements(*row_locator), (
            f"{product_name} is still in the cart before the test starts"
        )