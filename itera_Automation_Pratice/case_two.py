from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Globals
website = "https://itera-qa.azurewebsites.net/home/automation"

# Launch new browser
# Open URL https://itera-qa.azurewebsites.net/home/automation
# Select the Gender(Use ID locator)
# Check the Check Box "Tuesday" and "Friday" for category ‘Which days of the week are best to start something new?'(Use ID locator)
# Close browser

try:
    browser = webdriver.Chrome()  # instantiate chrome browser
    browser.maximize_window()
    browser.get(website)
    browser.implicitly_wait(15)
    # makes sure page DOM loaded
    button_box = browser.find_element(By.XPATH, "//div[contains(text(), 'CheckBox & Radio Button practice')]/parent::div")

    # print(textarea_box.get_attribute('className'))
    # radio button
    button_box.find_element(By.CSS_SELECTOR, "input[type='radio'][id='female']").click()

    # checkbox
    button_box.find_element(By.CSS_SELECTOR, "input[type='checkbox'][id='tuesday']").click()
    button_box.find_element(By.CSS_SELECTOR, "input[type='checkbox'][id='friday']").click()
    # submit
    browser.close()
    print("text case passed")
except:
    print("text case failed")