import threading
import unittest
import sys

sys.path.append('../')

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

import app
import evaluator

def get_website_handler():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://127.0.0.1:3433")
    driver.implicitly_wait(20)
    return driver

class TestApp(unittest.TestCase):
    def __init__(self, arg):
        threading.Thread(
            target=app.start_servers,
            args=(evaluator.SimpleEvaluator(),
            3433,
            31234,
        ), daemon=True).start()

        super().__init__(arg)

    def test_click(self):
        driver = get_website_handler()

        button = driver.find_element(By.ID, 'calculate')
        text_input = driver.find_element(By.ID, 'expression')

        test_cases = [
            ["5+5", "10"],
            ["5*5", "25"],
            ["5-4", "1"],
            ["21/7", "3"],
            ["5+5*5-5", "25"],
            ["10-1-1-1-1-1", "5"],
        ]

        item_id = 0
        for test_case in test_cases:
            expression = test_case[0]
            answer = test_case[1]

            text_input.clear()
            text_input.send_keys(expression)
            button.click()
            li = driver.find_element(By.ID, f"{item_id}")

            self.assertEqual(li.text, f"{expression} = {answer}")

            item_id += 1

        driver.close()