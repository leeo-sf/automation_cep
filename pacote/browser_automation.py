from selenium import webdriver
from data_catch import DataCatch
import time


class Automation:
    def __init__(self, url):
        self.__navegador = webdriver.Chrome()
        time.sleep(2)
        self.__navegador.maximize_window()
        time.sleep(2)
        self.__navegador.get(url)
        self._capturaDados = DataCatch(self.__navegador)