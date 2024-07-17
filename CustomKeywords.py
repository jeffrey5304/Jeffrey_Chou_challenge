

from robot.api.deco import keyword
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class CustomKeywords:

    def __init__(self):
        self.driver = None

    @keyword
    def open_browser(self, url, browser='chrome'):
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise ValueError(f"Browser '{browser}' is not supported.")
        self.driver.get(url)
        self.driver.maximize_window()

    @keyword
    def close_browser(self):
        if self.driver:
            self.driver.quit()

    @keyword
    def click_button(self, locator):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(),'{locator}')]")))
        button.click()

    @keyword
    def fill_user_details(self, first_name, last_name, username, password, customer, role, email, cell):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "FirstName"))).send_keys(first_name)
        wait.until(EC.presence_of_element_located((By.NAME, "LastName"))).send_keys(last_name)
        wait.until(EC.presence_of_element_located((By.NAME, "UserName"))).send_keys(username)
        wait.until(EC.presence_of_element_located((By.NAME, "Password"))).send_keys(password)
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='15']"))).click()
        wait.until(EC.presence_of_element_located((By.NAME, "RoleId"))).send_keys(role)
        wait.until(EC.presence_of_element_located((By.NAME, "Email"))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.NAME, "Mobilephone"))).send_keys(cell)

    @keyword
    def validate_user_added(self, username):
        wait = WebDriverWait(self.driver, 10)
        users = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//td[contains(text(),'{username}')]")))
        assert len(users) > 0, f"User '{username}' not found in the table."

    @keyword
    def delete_user(self):
        wait = WebDriverWait(self.driver, 10)
        delete_button = wait.until(EC.presence_of_element_located((By.XPATH, f"//html/body/table/tbody/tr[3]/td[11]/button/i")))
        delete_button.click()
        wait.until(EC.presence_of_element_located((By.XPATH, f"//html/body/div[2]/div[3]/button[2]"))).click()

        
        #alert = wait.until(EC.alert_is_present())
        #alert.accept()

    @keyword   
    def validate_user_deleted(self, username):
        users = self.driver.find_elements(By.XPATH, f"//td[contains(text(),'{username}')]")
        assert len(users) == 0, f"User '{username}' still exists in the table."


   
   




