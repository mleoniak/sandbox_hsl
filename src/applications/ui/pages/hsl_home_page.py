class HomePage():
    pass

    URL = "https://hsl.med.nyu.edu/"

    def __init__(self, app) -> None:
        self.app = app

        
    def navigate_to(self):
        self.app.navigate_to(self.URL)