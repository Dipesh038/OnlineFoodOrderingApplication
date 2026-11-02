from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    for password, result in [("pizza123", "Welcome!"), ("wrong", "Login failed")]:
        driver.get("http://127.0.0.1:8000"); WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("student")
        driver.find_element(By.ID, "password").send_keys(password); driver.find_element(By.ID, "login").click()
        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "message"), result))
