from selenium import webdriver
import time


class Automation:
    def __init__(self, url):
        self.__navegador = webdriver.Chrome()
        time.sleep(2)
        self.__navegador.maximize_window()
        time.sleep(2)
        self.__navegador.get(url)
        # data_cacth