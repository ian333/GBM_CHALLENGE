import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep




class Amazon_Test(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/google-chrome'
        self.driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver', options=options)
        driver = self.driver
        driver.get('http://amazon.com.mx/')
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    def test_search_pantallas(self):
        """
        Esta Funcion hace una busqueda en http://amazon.com.mx/  , cuenta e imprime todos los productos en la primera pagina
        de resultados de la busqueda Pantallas       

        """
        f=open('Productos.txt','w')

        driver=self.driver
        search_field=driver.find_element_by_id('twotabsearchtextbox')
        search_field.clear()
        search_field.send_keys('pantallas')
        search_field.submit()
        sleep(3)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "s-image")))
        products_list=driver.find_elements_by_css_selector('div[data-component-type="s-search-result"]')
        print(f"en la pagina principal se encontraron {len(products_list)} productos")
        nombre_productos=[ i.text for i in products_list ]
        for i in range(len(nombre_productos)):
            f.write('\n######################################\n')            
            f.write(nombre_productos[i])
            f.write('\n######################################\n')
        f.close()

        
        productos= open('Productos.txt','r').read()
        print(productos)
        f.close()




        
    

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=3, testRunner=HTMLTestRunner(
        output='reportes', report_name='Amazon'))
