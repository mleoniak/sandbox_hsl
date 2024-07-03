class HomePage:
    pass

    URL = "https://hsl.med.nyu.edu/"

    THIS_WEBSITE_TAB_BTN = '//*[@id="quicktabs-tab-frontpage_search-2"]'
    SEARCH_BOX = '//*[@id="edit-search-block-form--2"]'
    SEARCH_BTN = '//*[@id="solrsearchform1"]/div/div/div[1]/button/span'
    RESULTS_CONTENT = '//*[@id="content"]'

    NAV_SERVICES_BTN = "//li[@data-id='787']/a[@href='/services']"
    MEGA_MENU_DROPDOWN = (
        "//li[@data-id='787']//div[contains(@class, 'tb-megamenu-submenu')]"
    )
    TAG_NAME_FOR_MEGA_MENU_TAB_ELEMENTS = "li"

    def __init__(self, app) -> None:
        self.app = app

    def navigate_to(self):
        self.app.navigate_to(self.URL)

    def search_this_website(self, keyword: str):
        self.app.wait_and_click(self.THIS_WEBSITE_TAB_BTN)
        self.app.enter_text(self.SEARCH_BOX, keyword)
        self.app.wait_and_click(self.SEARCH_BTN)

    def get_search_results(self):
        return self.app.change_to_text(self.RESULTS_CONTENT)

    def show_mega_menu_dropdown(self):
        self.app.hover_action(self.NAV_SERVICES_BTN)

    def get_list_of_dropdown_elements(self):
        return self.app.get_list_of_elements(
            self.MEGA_MENU_DROPDOWN, self.TAG_NAME_FOR_MEGA_MENU_TAB_ELEMENTS
        )
