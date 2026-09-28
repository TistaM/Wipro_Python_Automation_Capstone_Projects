from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    URL = "https://automationexercise.com/login"

    EMAIL = (By.CSS_SELECTOR, "form[action='/login'] input[name='email']")
    PASSWORD = (By.CSS_SELECTOR, "form[action='/login'] input[name='password']")
    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "form[action='/login'] button[type='submit']",
    )
    LOGGED_IN_LABEL = (
        By.XPATH,
        "//*[contains(text(), 'Logged in as')]",
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.EMAIL))
        return self

    def login(self, email, password):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

    def is_logged_in(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGGED_IN_LABEL)
        ).is_displayed()