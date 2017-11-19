from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\olman\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.get("http://127.0.0.1:8000/inicio/principal")
driver.find_element_by_css_selector("input.btn.btn-success").click()
driver.find_element_by_name("cantidad_autovectores").clear()
driver.find_element_by_name("cantidad_autovectores").send_keys("10")
driver.find_element_by_name("porcentaje_muestra").clear()
driver.find_element_by_name("porcentaje_muestra").send_keys("10")
driver.find_element_by_css_selector("input.btn.btn-success").click()