from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import handtest_server
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def getWebsiteHandler():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://127.0.0.1:3433")
    driver.implicitly_wait(20)
    return driver

class TestInBrowser(unittest.TestCase):
    def __init__(self, arg):
        handtest_server.RunThreads()
        super().__init__(arg)

    def test_click(self):
        driver = getWebsiteHandler()

        button = driver.find_element(By.ID, 'calculate')
        text_input = driver.find_element(By.ID, 'expression')

        expressions = ["5+5", "5*5", "5-4", "21//7", "5+5*5-5", "10-1-1-1-1-1"]
        answer = ["10", "25", "1", "3", "25", "5"]

        item_id = 0
        for expression in expressions:
            text_input.clear()
            text_input.send_keys(expression)
            button.click()
            li = driver.find_element(By.ID, f"{item_id}")

            self.assertEqual(li.text, f"{expression} = {answer[item_id]}")

            item_id += 1

        driver.close()