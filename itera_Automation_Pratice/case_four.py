from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Globals
website = "https://itera-qa.azurewebsites.net/home/automation"

# Launch new browser
# Open URL https://itera-qa.azurewebsites.net/home/automation
# Select the Radio button (2 years) for category Years of experience in test automation (Find elements by using Xpath method.)
# Check the Check Box ‘Selenium Webdriver’ and TestNG for category ‘Which automation tools/frameworks do you use?'(Find elements by using Xpath method)
# Close browser

try:
    browser = webdriver.Chrome()  # instantiate chrome browser
    browser.maximize_window()
    browser.get(website)
    browser.implicitly_wait(15)
    # makes sure page DOM loaded
    xpath_box = browser.find_element(By.XPATH,
                                      "//div[contains(text(), 'CheckBox & Radio Button practice Xpath')]/parent::div")
    first_group = xpath_box.find_element(By.XPATH,"//label[contains(text(), 'Years of experience in test automation')]/parent::div")
    sec_group = xpath_box.find_element(By.XPATH,"//label[contains(text(), 'Which automation tools/frameworks do you use?')]/parent::div")

    first_group.find_element(By.XPATH, "//label[@for='2years']").click()
    sec_group.find_element(By.XPATH, "//label[@for='selenium']").click()
    sec_group.find_element(By.XPATH, "//label[@for='testng']").click()

    browser.close()
    print("text case passed")
except:
    print("text case failed")