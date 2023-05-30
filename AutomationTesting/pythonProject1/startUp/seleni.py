import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class SWdriver(unittest.TestCase):
    def setUp(self):
        options = Options()
        service = Service('D:/kai/python')
        self.driver = webdriver.Chrome(service=service, options=options)

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
        self.driver.quit()
