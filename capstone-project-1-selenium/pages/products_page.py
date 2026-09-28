from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductsPage:
    URL = "https://automationexercise.com/products"

    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCHED_PRODUCTS_HEADING = (
        By.XPATH,
        "//h2[contains(., 'Searched Products')]",
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
        return self

    def search(self, product_name):
        search_input = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(product_name)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

        self.wait.until(
            EC.visibility_of_element_located(self.SEARCHED_PRODUCTS_HEADING)
        )
        return self

    def product_is_visible(self, product_name):
        product = (
            By.XPATH,
            f"//div[contains(@class, 'productinfo')]"
            f"//p[normalize-space()='{product_name}']",
        )
        return self.wait.until(
            EC.visibility_of_element_located(product)
        ).is_displayed()

    def open_product(self, product_name):
        product_card = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'product-image-wrapper')]"
                    f"[.//p[normalize-space()='{product_name}']]",
                )
            )
        )
        link = product_card.find_element(
            By.XPATH, ".//a[contains(., 'View Product')]"
        )
        self.driver.get(link.get_attribute("href"))
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".product-information h2")
            )
        )