def test_nav_vis(hsl_nyu_ui_app):
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

    assert (
        len(hsl_nyu_ui_app.hsl_home_page.get_navigation_services_dropdown_elements())
        == 8
    ), "Expected 8 dropdown elements"
