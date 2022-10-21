from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import variables


def init():
    navegador = webdriver.Chrome()
    navegador.get(variables.ROUTE_NAVEGATOR)

    time.sleep(10)

    navegador.find_element(By.XPATH, variables.ELEMENT_BOX_USER).send_keys(variables.USER_BOX)
    navegador.find_element(By.XPATH, variables.BUTTON_NEXT).click()

    time.sleep(10)

    navegador.find_element(By.XPATH, variables.ELEMENT_BOX_EMAIL).send_keys(variables.USER_EMAIL)
    navegador.find_element(By.XPATH, variables.BUTTON_LOGIN).click()

    time.sleep(10)

    navegador.find_element(By.XPATH, variables.ELEMENT_EMAIL_PASSWORD).send_keys(variables.USER_EMAIL_PASSWORD)
    navegador.find_element(By.XPATH, variables.BUTTON_LOGIN_EMAIL).click()

    time.sleep(10)

    navegador.find_element(By.XPATH, variables.BUTTON_ACCEPT_CONNECT).click()

    time.sleep(20)

    navegador.find_element(By.XPATH, variables.BUTTON_MENU).click()

    time.sleep(10)

    navegador.find_element(By.XPATH, variables.BUTTON_MENU_2).click()

    time.sleep(10)

    navegador.find_element(By.XPATH, variables.BUTTON_MENU_3).click()

    time.sleep(10)

    navegador.find_element(By.XPATH, variables.BUTTON_POINT).click()

    time.sleep(25)

    navegador.close()