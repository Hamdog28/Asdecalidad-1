import unittest
#import controlador.DAOBDmuestral.DAOBDmuestral
#from back_end.controlador.DaoDBMuestral import DaoDBMuestral

from back_end.modelo.Imagen import Imagen
from back_end.modelo.Muestra import Muestra
from back_end.modelo.Proyeccion import Proyeccion
from back_end.modelo.Clasificacion import Clasificacion
from back_end.modelo.DistanciaCentroide import DistanciaCentroide
from back_end.controlador.GestorMuestra import GestorMuestra
from back_end.controlador.GestorPCA import GestorPCA
from back_end.controlador.Configuracion import Configuracion

from back_end.controlador.DaoBDPCA import DaoDBPCA


import numpy as np



from selenium import webdriver

class SystemTest(unittest.TestCase):
    driver = webdriver.Chrome("C:\\Users\\olman\\Desktop\\chromedriver_win32\\chromedriver.exe")
    
    def test_1(self):
        print("Test1: entrenamiento")
        SystemTest.driver.get("http://127.0.0.1:8000/inicio/principal")
        SystemTest.driver.find_element_by_css_selector("input.btn.btn-success").click()
        SystemTest.driver.find_element_by_name("cantidad_autovectores").clear()
        SystemTest.driver.find_element_by_name("cantidad_autovectores").send_keys("10")
        SystemTest.driver.find_element_by_name("porcentaje_muestra").clear()
        SystemTest.driver.find_element_by_name("porcentaje_muestra").send_keys("10")
        SystemTest.driver.find_element_by_css_selector("input.btn.btn-success").click()

        
    def test_2(self):
        print("Test2: identificacion")
        SystemTest.driver.get("http://127.0.0.1:8000/inicio/principal")
        SystemTest.driver.find_element_by_xpath("//input[@value='Identificar']").click()
        SystemTest.driver.find_element_by_id("input-1a").clear()
        SystemTest.driver.find_element_by_id("input-1a").send_keys("C:\\Users\\olman\\Documents\\GitHub\\Asdecalidad-1\\website\\src\\website\\inicio\\back_end\\archivos\\otros\\cara1.png")
        SystemTest.driver.find_element_by_xpath("//button[@type='submit']").click()
        
        
        


if __name__ == '__main__':
    unittest.main()