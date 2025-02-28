import allure
from pages import header, product


@allure.feature('Header > Cart')
@allure.link('https://trello.com/c/76HixPum')
@allure.title('Verify counter number')
def test_003_003_004_verify_cart_counter_number():
    header.open_product_url()
    product.add_to_cart_with_qty('M', 'Orange', '1')
    header.counter_should_be_equal('1')
