from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductDetailPage:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-information h2")
    QUANTITY = (By.ID, "quantity")
    ADD_TO_CART = (
        By.XPATH,
        "//button[contains(., 'Add to cart')]",
    )
    VIEW_CART = (
        By.XPATH,
        "//div[@id='cartModal']//a[contains(., 'View Cart')]",
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def get_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        ).text.strip()

    def set_quantity(self, quantity):
        quantity_field = self.wait.until(
            EC.visibility_of_element_located(self.QUANTITY)
        )
        quantity_field.clear()
        quantity_field.send_keys(str(quantity))

    def add_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART)
        ).click()
        self.wait.until(
            EC.visibility_of_element_located(self.VIEW_CART)
        )

    def view_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.VIEW_CART)
        ).click()