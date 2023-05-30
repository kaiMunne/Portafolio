import time
from page_objects.page_obj import LoginPage
from startUp.seleni import SWdriver


class TestLogin(SWdriver):

    def setUpClass(self):
        driver = self.driver
        self.driver.get(LoginPage.get_base_url())
        home_page = LoginPage(driver)
        time.sleep(5)
        home_page.login()
        mensaje_exitoso = driver.find_element_by_class("loading-profile")
        assert mensaje_exitoso.text == "Bienvenido, Pablo"

    