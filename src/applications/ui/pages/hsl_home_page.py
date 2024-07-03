from src.applications.ui.pages.components.search_this_website_component import (
    SearchThisWebsiteComponent,
)
from src.applications.ui.pages.components.navigation_component import (
    NavigationComponent,
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
        self.search_component.search(keyword)

    def get_search_results(self):
        return self.search_component.get_search_results()

    def show_mega_menu_dropdown(self):
        self.navigation_component.show_mega_menu_dropdown()

    def get_list_of_dropdown_elements(self):
        return self.navigation_component.get_navigation_dropdown_elements()
