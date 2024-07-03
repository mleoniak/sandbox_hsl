from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_nav_content(hsl_nyu_ui_app):
    """
    Summary:
      This test case verifies the navigation tab submenu quantity.

    Steps:
     1. Navigates to the HSL home page using.
     2. Hover over the navbar button.

    Expected result:
    Quantity of dropdown elements is as expected.
    """

    hsl_nyu_ui_app.hsl_home_page.navigate_to()

    hsl_nyu_ui_app.hsl_home_page.show_mega_menu_dropdown()

    elem = hsl_nyu_ui_app.hsl_home_page.get_list_of_dropdown_elements()[0]

    print(elem)
    print("hello")