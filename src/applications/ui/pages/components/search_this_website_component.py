class SearchThisWebsiteComponent:
    pass
    THIS_WEBSITE_TAB_BTN = '//*[@id="quicktabs-tab-frontpage_search-2"]'
    SEARCH_BOX = '//*[@id="edit-search-block-form--2"]'
    SEARCH_BTN = '//*[@id="solrsearchform1"]/div/div/div[1]/button/span'
    RESULTS_CONTENT = '//*[@id="content"]'

    def __init__(self, app) -> None:
        self.app = app

    def search(self, keyword: str):
        self.app.wait_and_click(self.THIS_WEBSITE_TAB_BTN)
        self.app.enter_text(self.SEARCH_BOX, keyword)
        self.app.wait_and_click(self.SEARCH_BTN)

    def get_search_results(self):
        return self.app.change_to_text(self.RESULTS_CONTENT)
