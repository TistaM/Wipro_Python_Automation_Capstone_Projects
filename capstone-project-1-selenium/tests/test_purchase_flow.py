import os
import json
from pathlib import Path

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_detail_page import ProductDetailPage
from pages.products_page import ProductsPage

screenshots = Path(__file__).resolve().parents[1] / "evidence" / "screenshots"
screenshots.mkdir(parents=True, exist_ok=True)

data_file = Path(__file__).resolve().parents[1] / "data" / "test_data.json"
test_data = json.loads(data_file.read_text(encoding="utf-8"))

product_name = test_data["product_name"]
quantity = test_data["quantity"]

def test_purchase_flow(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(
        os.environ["AE_TEST_EMAIL"],
        os.environ["AE_TEST_PASSWORD"],
    )
    assert login_page.is_logged_in()
    CartPage(driver).remove_product_if_present("Blue Top")

    products_page = ProductsPage(driver)
    products_page.open()
    products_page.search("Blue Top")
    assert products_page.product_is_visible("Blue Top")
    river.save_screenshot(str(screenshots / "01-product-search.png"))
    products_page.open_product("Blue Top")

    detail_page = ProductDetailPage(driver)
    assert detail_page.get_product_name() == "Blue Top"
    detail_page.set_quantity(2)
    detail_page.add_to_cart()
    detail_page.view_cart()

    cart_page = CartPage(driver)
    assert cart_page.product_quantity("Blue Top") == "2"
    assert "500" in cart_page.product_price("Blue Top")
    assert "1000" in cart_page.product_total("Blue Top")

    driver.save_screenshot(str(screenshots / "02-verified-cart.png"))