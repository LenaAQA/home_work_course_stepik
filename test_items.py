from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_add_to_basket_button(browser):
    browser.get(link)

    WebDriverWait(browser, 10).until(EC.url_contains("coders-at-work_207"))

    button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
    )

    assert button.is_displayed()
