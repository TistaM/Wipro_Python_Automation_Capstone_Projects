from pages.products_page import ProductsPage


def test_search_blue_top(driver):
    products_page = ProductsPage(driver)
    products_page.open()
    products_page.search("Blue Top")

    assert products_page.product_is_visible("Blue Top")