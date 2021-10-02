from time import sleep
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common import by
from urllib3.packages.six import assertCountEqual
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By




class Mercado_libre_Test(unittest.TestCase):
    def setUp(self):
        print("""
 
        This test script makes a search in Mercado Libre Colombia for a Playstation 3
        and stablish the locacion in bogota then filter by new products
         and finally sets the view from the lower price to the higher price

        """)
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/brave-browser'
        self.driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver', options=options)
        driver = self.driver
        driver.get('http://amazon.com.mx/')
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    def test_search_ps4(self):
        """
        Esta Funcion hace una busqueda en Mercado Libre Colombia y establece como ubicacion Bogota
        Filtra los productos nuevos y los ordena de mayor precio a menor precio

        """

        driver=self.driver
        search_field=driver.find_element_by_id('twotabsearchtextbox')
        search_field.clear()
        search_field.send_keys('Pantallas')
        search_field.submit()
        sleep(3)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "s-image")))
        products_list=driver.find_elements_by_css_selector('div[data-component-type="s-search-result"]')
        print(len(products_list))
        nombre_productos=[ i.text for i in products_list ]
        for i in range(len(nombre_productos)):
            print(nombre_productos[i],sep='\n')
            print()




        
    

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main(verbosity=3, testRunner=HTMLTestRunner(
        output='reportes', report_name='Amazon'))
