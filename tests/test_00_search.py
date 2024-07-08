def test_search_this_website_functionality(hsl_nyu_ui_app):
    """
    Summary:
      This test case verifies the search functionality of the HSL website.

    Steps:
     1. Navigates to the HSL home page using.
     2. Searches the website using.

    Expected result:
    The `query` is present in the search results
    """

    query = "heart"

    hsl_nyu_ui_app.hsl_home_page.navigate_to()

    hsl_nyu_ui_app.hsl_home_page.search_this_website(query)

    assert query in hsl_nyu_ui_app.hsl_home_page.get_search_results()
