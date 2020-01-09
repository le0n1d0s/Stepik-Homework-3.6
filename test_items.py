import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."

def test_checking_for_a_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    element_1 = button.get_attribute("value")
    element_2 = button.text
    assert element_1 == element_2