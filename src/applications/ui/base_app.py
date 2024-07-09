import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseApp:
    pass

    def __init__(self, browser) -> None:
        self.browser = browser

    def navigate_to(self, url):
        self.browser.get(url)

    def wait_and_click(self, locator, timeout=15):
        elem = self.browser.find_element(By.XPATH, locator)
        wait = WebDriverWait(self.browser, timeout)
        wait.until(EC.visibility_of(elem))
        elem.click()

    def get_list_of_elements(self, locator, tag_name, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        elem = wait.until(
            EC.visibility_of_element_located((By.XPATH, locator))
        ).find_elements(By.TAG_NAME, tag_name)
        time.sleep(1)
        return elem

    def get_element_by_tag_and_return_text(self, tag_name):
        wait = WebDriverWait(self.browser, timeout=10)
        elem = wait.until(EC.visibility_of_element_located((By.TAG_NAME, tag_name)))
        return elem.text

    def enter_text(self, locator, text):
        elem = self.browser.find_element(By.XPATH, locator)
        elem.clear()
        elem.send_keys(text)

    def get_element_text(self, locator):
        elem = self.browser.find_element(By.XPATH, locator)
        return elem.text

    def hover_action(self, locator):
        elem = self.browser.find_element(By.XPATH, locator)
        actions = ActionChains(self.browser)
        actions.move_to_element(elem).perform()

    def close_browser(self):
        self.browser.close()
