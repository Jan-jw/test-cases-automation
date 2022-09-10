from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Globals
website = "https://itera-qa.azurewebsites.net/home/automation"

# Launch new browser
# Open URL https://itera-qa.azurewebsites.net/home/automation
# Select the "Norway" from for category "Where do you plan to travel this year?" (Use select method.)
# Close browser

try:
    browser = webdriver.Chrome()  # instantiate chrome browser
    browser.maximize_window()
    browser.get(website)
    browser.implicitly_wait(15)
    # makes sure page DOM loaded
    dropdown = browser.find_element(By.XPATH, "//label[contains(text(), 'Where do you plan to travel this year?')]/following-sibling::div[@class='form-group']")
    Select(dropdown.find_element(By.TAG_NAME, "select")).select_by_visible_text("Norway")

    browser.close()
    print("text case passed")
except:
    print("text case failed")