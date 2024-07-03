class NavigationComponent:
    pass

    NAV_SERVICES_BTN = "//li[@data-id='787']/a[@href='/services']"
    MEGA_MENU_DROPDOWN = (
        "//li[@data-id='787']//div[contains(@class, 'tb-megamenu-submenu')]"
    )
    TAG_NAME_FOR_MEGA_MENU_TAB_ELEMENTS = "li"

    def __init__(self, app) -> None:
        self.app = app
    
    def show_mega_menu_dropdown(self):
        self.app.hover_action(self.NAV_SERVICES_BTN)

    def get_navigation_dropdown_elements(self):
        return self.app.get_list_of_elements(
            self.MEGA_MENU_DROPDOWN, self.TAG_NAME_FOR_MEGA_MENU_TAB_ELEMENTS
        )