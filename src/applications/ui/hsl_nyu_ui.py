from src.applications.ui.pages.hsl_home_page import HomePage
from src.applications.ui.base_app import BaseApp

class HslNyuUI(BaseApp):

    def __init__(self, browser) -> None:
        super().__init__(browser)

        self.hsl_home_page = HomePage(self)

    def open(self):
        self.hsl_home_page.navigate_to()

    def close(self):
        self.close_browser()