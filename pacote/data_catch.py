from selenium.webdriver.common.by import By
import time


class DataCatch:
    def __init__(self, navegador):
        self.__caminho_plan = "C:/Users/leona/Documents/projetos/extracao_cep/input/"
        self.__plan_output = "C:/Users/leona/Documents/projetos/extracao_cep/outut/"
        self.__navegador = navegador


    def PesquisaCep(self, cep):
        self.__navegador.find_element(by=By.ID, value="endereco").send_keys(cep)
        time.sleep(2)
        self.__navegador.find_element(by=By.ID, value="btn_pesquisar").click()
        time.sleep(2)