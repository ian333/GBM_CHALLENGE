import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class GooglePage(object):

    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://google.com'
        self.search_locator = 'q'

    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'q')))
        return True

    @property
    def keyword(self):
        input_field = self._driver.find_element_by_name('q')
        return input_field.get_attribute('value')

    def open(self):
        self._driver.get(self._url)
        self._driver.maximize_window()

    def type_search(self, keyword):
        input_field = self._driver.find_element_by_name('q')
        input_field.send_keys(keyword)

    def click_submit(self):
        input_field = self._driver.find_element_by_name('q')
        input_field.submit()

    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()

    def open_gbm(self):
        link_gbm = self._driver.find_element_by_partial_link_text("GBM+")
        link_gbm.click()

    def academy_gbm(self):
        academy_button = self._driver.find_element_by_link_text("Academy")
        academy_button.click()

    def change_tab(self):
        self._driver.switch_to.window(self._driver.window_handles[1])

    def download_ebooks(self):
        image_ebook = self._driver.find_element_by_xpath(
            '//*[@id="post-14"]/div/section[2]/div/div/div/div/div[1]/figure/a/img')
        image_ebook.click()
        book = self._driver.find_element_by_partial_link_text('Retail: ')
        book.click()
        download_button=self._driver.find_element_by_xpath('//*[@id="post-6067"]/div/div[7]/div/div/div[1]/div/div/a')
        download_button.click()
        return download_button.text

    def subscribe(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'formulario-login')))
        subscribe_button=self._driver.find_element_by_partial_link_text('¿Aun no tienes usuario? ')
        subscribe_button.click()
    def input_data(self):
        nombre='Sebastian Vazquez'
        correo='sebastianvaz123@hotmail.com'
        telefono='5526743893'
        password='Contraseña_prueba'
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'nombre')))
        name=self._driver.find_element_by_name('nombre')
        name.clear()
        name.send_keys(nombre)
        email=self._driver.find_element_by_name('email')
        email.clear()
        email.send_keys(correo)
        phone=self._driver.find_element_by_name('phone')
        phone.clear()
        phone.send_keys(telefono)
        passw_element=self._driver.find_element_by_name('pass')
        passw_element.clear()
        passw_element.send_keys(password)
        button_priv=self._driver.find_element_by_name('terminos')
        button_priv.click()
        subscribe=self._driver.find_element_by_id('btn-submit-registro')
        subscribe.click()




