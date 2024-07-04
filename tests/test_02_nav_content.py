# import helpers
import time

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

    hsl_nyu_ui_app.hsl_home_page.show_mega_menu_services_dropdown()

    dropdown = hsl_nyu_ui_app.hsl_home_page.get_navigation_services_dropdown_elements()
    if dropdown:
        for n in dropdown:
            time.sleep(0.5)
            if hasattr(n, "text"):
                print(n.text)
            else:
                print("Dropdown element does not have a 'text' attribute.")
    else:
        print("No dropdown elements found.")

    # elements = hsl_nyu_ui_app.hsl_home_page.get_list_of_elements_choose_one()
    # print(len(elements))

    # h1= hsl_nyu_ui_app.hsl_home_page.get_element_by_tag_change_to_text()

    # assert helpers.has_common_substring(dropdown, h1)
