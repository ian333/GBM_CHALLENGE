import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from google_page import GooglePage




class GoogleTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        """
        Este es un script utilizando POM para una mejor comprension de las pruebas, 
        su proposito es automatizar la descarga del primer ebook de la academia de GBM
        """
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/google-chrome'
        self.driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver', options=options)

    
    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('GBM')
        self.assertEqual('GBM',google.keyword)
        google.open_gbm()
        google.academy_gbm()
        google.change_tab()
        button_text=google.download_ebooks()
        google.subscribe()
        google.input_data()

        self.assertEqual('Descargar',button_text)
        

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=3, testRunner=HTMLTestRunner(
        output='reportes', report_name='Test Google Report'))
