import time
import pytest
import os

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_CapstoneProjectTests:

    @pytest.fixture
    def getDriver(self):
        driver = webdriver.Chrome()
        driver.get('https://the-internet.herokuapp.com/')
        return driver
        time.sleep(2)
        driver.quit()

    def test_CheckBoxes(self, getDriver):
        driver = getDriver
        currentPath = os.getcwd()
        filePath = currentPath + '\Sample.txt'
        print(filePath)
        driver.find_element(By.XPATH, "//a[text()='Checkboxes']").click()
        time.sleep(2)
        headertext = driver.find_element(By.XPATH, "//*[@id='content']/div/h3").text
        assert headertext == "Checkboxes"
        checkbox2 = driver.find_element(By.XPATH, "//*[@id='checkboxes']/input[2]").is_selected()
        assert checkbox2 == True
        driver.back()
        driver.find_element(By.XPATH, "//a[text()='File Upload']").click()
        assert driver.find_element(By.XPATH, "//*[@id='content']/div[1]/h3").text == "File Uploader"
        driver.find_element(By.XPATH, "//*[@id='file-upload']").send_keys(filePath)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='file-submit']").submit()
        time.sleep(2)
        uploadedFileName = driver.find_element(By.XPATH, "//*[@id='uploaded-files']").text
        assert uploadedFileName == "Sample.txt"

