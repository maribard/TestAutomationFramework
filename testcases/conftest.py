from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.chrome.webdriver import webdriver
import pytest
import time

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome('C:/Users/m.bardyn/AppData/Local/Temp/Temp1_chromedriver_win32.zip/chromedriver.exe')
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 2)
    driver.maximize_window()
    driver.set_page_load_timeout(3)
    driver.get('https://testarena.pl/demo')
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    time.sleep(2)
    driver.quit()




