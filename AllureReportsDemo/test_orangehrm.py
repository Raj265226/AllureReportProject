from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest

@allure.severity(allure.severity_level.MINOR)
class TestHRM:
    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver=webdriver.Chrome(executable_path="E:\Work Files\Webdrives_for_Automation\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status = self.driver.find_element(By.XPATH, "//div[@id='divLogo']//img").is_displayed()
        if status == True:
            assert True,"Test Passed"
        else:
            assert False,"Test Failed"
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip('Skipping test ..Later I will implement')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome(executable_path="E:\Work Files\Webdrives_for_Automation\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        act_title=self.driver.title
        if act_title=="OrangeHRM123":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="testloginScreen",attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

