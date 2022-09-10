from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Globals
website = "https://itera-qa.azurewebsites.net/home/automation"

# Test Case 1
# Launch new browser
# Open URL https://itera-qa.azurewebsites.net/home/automation
# Type Name, Mobile number, Email address, Password, Address (Use ID locator )
# Click on Submit button (Use Name locator)
# Close browse

browser = webdriver.Chrome() # instantiate chrome browser
browser.maximize_window()
browser.get(website)
# browser.implicitly_wait(15)

try:
    # makes sure page DOM loaded
    textarea_box = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Textarea practice')]/parent::div"))
    )
    # print(textarea_box.get_attribute('className'))
    # input
    textarea_box.find_element(By.ID, "name").send_keys("John Doe")
    textarea_box.find_element(By.ID, "phone").send_keys("1234567890")
    textarea_box.find_element(By.ID, "email").send_keys("johndoe@gmail.com")
    textarea_box.find_element(By.ID, "password").send_keys("1234567890")
    textarea_box.find_element(By.ID, "address").send_keys("earth")

    # submit
    textarea_box.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    browser.close()
    print("text case passed")
except:
    print("text case failed")