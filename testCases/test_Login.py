import time

from pageObjects.LoginPage import OrangeHRM_Login
from Utilities.Logger import LogGenerator


# folder#file#class

class Test_Login:
    log = LogGenerator.loggen()

    def test_page_title_001(self, setup):
        self.log.info("Testcase test_page_title_001 is started")
        self.log.info("Opening browser")
        self.driver = setup  # open browser # url orangehrm
        self.log.info("Page Title is " + self.driver.title)
        if self.driver.title == "OrangeHRM":
            self.log.info("Taking screenshot")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("C:\\Users\\dound\\PycharmProjects\\OrangeHRM\\ScreenShots\\test_page_title_001_pass.png")
            self.driver.close()
            self.log.info("Testcase test_page_title_001 is passed")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\dound\\PycharmProjects\\OrangeHRM\\ScreenShots\\test_page_title_001_fail.png")
            self.driver.close()
            self.log.info("Testcase test_page_title_001 is failed")
            assert False

    def test_login_002(self, setup):
        self.log.info("Testcase test_login_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lp = OrangeHRM_Login(self.driver)
        self.log.info("Entering Username")
        self.lp.Enter_Username("Admin")
        self.log.info("Entering password")
        self.lp.Enter_Password("admin123")
        self.log.info("Clicking in login button")
        self.lp.Click_login()
        # print(self.lp.Login_Status())
        self.log.info("Checking login status")
        if self.lp.Login_Status() == True:
            self.log.info("taking screenshot")
            self.driver.save_screenshot("C:\\Users\\dound\\PycharmProjects\\OrangeHRM\\ScreenShots\\test_login_002_pass.png")
            self.log.info("Clicking on Menu button")
            self.lp.Click_Menu()
            self.log.info("Clicking on logout button")
            self.lp.Click_Logout()
            self.driver.close()
            self.log.info("Testcase test_login_002 is passed")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\dound\\PycharmProjects\\OrangeHRM\\ScreenShots\\test_login_002_fail.png")
            self.driver.close()
            self.log.info("Testcase test_login_002 is failed")
            assert False


# pytest -v -n=2 --html=Reports/OrangeHRMreport.html --alluredir="Allure-results"