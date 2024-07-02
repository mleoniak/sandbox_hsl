from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the URL
driver.get("https://hsl.med.nyu.edu/")

# Click on the tab
driver.find_element(By.XPATH, '//*[@id="quicktabs-tab-frontpage_search-2"]').click()

# Clear the search input
search_box = driver.find_element(By.XPATH, '//*[@id="edit-search-block-form--2"]')
search_box.clear()

# Type into the search input
search_box.send_keys("heart")

# Click the search button
driver.find_element(
    By.XPATH, '//*[@id="solrsearchform1"]/div/div/div[1]/button/span'
).click()

# Add your necessary wait time and other steps here
results = driver.find_elements(By.XPATH, '//*[@id="content"]')
assert any(
    "heart" in result.text.lower() for result in results
), "Keyword 'heart' not found in search results."

# Close the WebDriver
driver.quit()
