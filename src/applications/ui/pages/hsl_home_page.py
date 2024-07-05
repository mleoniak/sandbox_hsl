from src.applications.ui.pages.components.navigation_component import (
    NavigationComponent,
)
from src.applications.ui.pages.components.search_this_website_component import (
    SearchThisWebsiteComponent,
)


class HomePage:
    pass

    URL = "https://hsl.med.nyu.edu/"

    def __init__(self, app) -> None:
        self.app = app
        self.search_component = SearchThisWebsiteComponent(app)
        self.navigation_component = NavigationComponent(app)

    def navigate_to(self):
        self.app.navigate_to(self.URL)

    def search_this_website(self, keyword: str):
        self.search_component.search_this_website(keyword)

    def get_search_results(self):
        return self.search_component.get_search_results()

    def show_mega_menu_services_dropdown(self):
        self.navigation_component.show_mega_menu_services_dropdown()

    def get_navigation_services_dropdown_elements(self):
        return self.navigation_component.get_navigation_services_dropdown_elements()

    def get_element_by_tag_and_return_text(self):
        return self.navigation_component.get_element_by_tag_and_return_text()
