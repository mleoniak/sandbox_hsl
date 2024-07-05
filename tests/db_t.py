import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Configure Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--window-size=1920,1080")  # Specify window size if needed

# Initialize the driver with options
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get("https://hsl.med.nyu.edu/")

# Maximize the browser window
driver.maximize_window()

# Locate the navigation button - services
nav_button = driver.find_element(
    By.XPATH, '//*[@id="block-tb-megamenu-main-menu"]/div/div/ul/li[2]'
)

# Perform hover action
actions = ActionChains(driver)
actions.move_to_element(nav_button).perform()

# Wait for the dropdown menu to be visible
wait = WebDriverWait(driver, 10)
dropdown_menu = wait.until(
    EC.visibility_of_element_located(
        (
            By.XPATH,
            '//*[@id="block-tb-megamenu-main-menu"]/div/div/ul/li[2]/div/div/div',
        )
    )
)

# Locate dropdown elements and check their visibility
dropdown_elements = dropdown_menu.find_elements(By.TAG_NAME, "li")


# def has_common_substring(str1, str2):
#     # Convert both strings to sets of words
#     set1 = set(str1.split())
#     set2 = set(str2.split())

#     # Find intersection of sets (common words)
#     common_words = set1.intersection(set2)

#     # Check if there's at least one common word
#     return len(common_words) > 0


if dropdown_elements:
    # for n in range(0, len(dropdown_elements) - 1):
    first_element = dropdown_elements[0]
    li_title = first_element.text
    print(li_title)
    first_element.click()

    # Wait for the new site to open
    time.sleep(1)

    # Print the <h1> text after site open -> ITS GO TO THE BAE APP LIKE FIND ELEMENT VIA TAG NAME
    h1_element = driver.find_element(By.TAG_NAME, "h1")
    print(h1_element.text)

    assert li_title in h1_element.text, "The title does not match the clicked element"
    print("True")

    # assert has_common_substring(
    #     li_title, h1_element.text
    # ), "No common substring found between the titles"
    # print("True")
    # # driver.back()
    # time.sleep(2)

# Cleanup
driver.quit()
