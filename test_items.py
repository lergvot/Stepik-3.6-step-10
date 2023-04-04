from selenium.webdriver.common.by import By
import time

def test_see_basket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30) # ожидание, что бы проверить локализацию
    basket = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')

    assert len(basket) > 0, 'Кнопка корзины не найдена'
