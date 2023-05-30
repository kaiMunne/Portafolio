import time
from data.hmm_data import HMM_Data
from selenium.webdriver.common.by import By

base_url = "https://testeo.hmmglobal.com/login"


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.usuario_id = 'username'
        self.contraseña_id = 'password'
        self.ingresar_id = 'button-signin'

    def login(self):
        data = HMM_Data()
        user, password = data.data_login(self)
        username_input = self.driver.find_element_by_id(self.usuario_id)
        username_input.send_keys(user)
        password_input = self.driver.find_element_by_id(self.contraseña_id)
        password_input.send_keys(password)
        login_button = self.driver.find_element_by_id(self.ingresar_id)
        login_button.click()

    @staticmethod
    def get_base_url():
        return base_url
