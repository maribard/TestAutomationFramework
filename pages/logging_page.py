import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoggingPage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait



    def login(self, email):
        element_log = self.wait.until(EC.presence_of_element_located((By.ID, "email")))
        element_log.clear()
        element_log.send_keys(email)

    def password(self, password):
        element_pass = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        element_pass.send_keys(password)

    def click_login(self):
        element_click = self.wait.until(EC.presence_of_element_located((By.ID, "login")))
        element_click.click()
        current_url = self.driver.current_url
        return current_url