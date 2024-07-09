# import src.helpers
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

    dropdown = hsl_nyu_ui_app.hsl_home_page.get_navigation_services_dropdown_elements()[
        3
    ]

    assert_ = dropdown.text

    time.sleep(1)
    dropdown.click()
    time.sleep(3)

    h1 = hsl_nyu_ui_app.hsl_home_page.get_element_by_tag_and_return_text()

    time.sleep(1)
    print(h1)

    def has_common_substring(str1, str2):
        # Convert both strings to sets of words
        set1 = set(str1.split())
        set2 = set(str2.split())
        # Find intersection of sets (common words)
        common_words = set1.intersection(set2)
        # Check if there's at least one common word
        return len(common_words) > 0

    assert has_common_substring(h1, assert_)
