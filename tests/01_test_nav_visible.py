from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://hsl.med.nyu.edu/")

# Maximize the browser window
driver.maximize_window()

# Locate the navigation button - services
nav_button = driver.find_element(By.XPATH, "//li[@data-id='787']/a[@href='/services']")

# Perform hover action
actions = ActionChains(driver)
actions.move_to_element(nav_button).perform()

# Wait for the dropdown menu to be visible
wait = WebDriverWait(driver, 10)
dropdown_menu = wait.until(
    EC.visibility_of_element_located(
        (
            By.XPATH,
            ("//li[@data-id='787']//div[contains(@class, 'tb-megamenu-submenu')]"),
        )
    )
)


# Locate dropdown elements and check their visibility
dropdown_elements = dropdown_menu.find_elements(By.TAG_NAME, "li")


# Assertions for checking visibility of dropdown elements
assert len(dropdown_elements) == 8, "Expected 8 dropdown elements"
print("True")

# Cleanup
driver.quit()
