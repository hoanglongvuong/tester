
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.lazada.vn/")
        textSearch = driver.find_element(By.XPATH, "//*[@id=\"q\"]")
        textSearch.send_keys("Áo sơ mi")

        btnSearch = driver.find_element(By.XPATH, "//*[@id=\"topActionHeader\"]/div/div[2]/div/div[2]/form/div/div[2]/button")
        btnSearch.click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()