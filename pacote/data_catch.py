from selenium.webdriver.common.by import By
from openpyxl import Workbook, load_workbook
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


    def CapturaDados(self):
        logradouro = self.__navegador.find_element('xpath', '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').accessible_name
        bairro = self.__navegador.find_element('xpath', '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').accessible_name
        localidade = self.__navegador.find_element('xpath', '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').accessible_name
        cep = self.__navegador.find_element('xpath', '//*[@id="resultado-DNEC"]/tbody/tr[1]/td[4]').accessible_name

        self.__navegador.find_element(by=By.ID, value="btn_nbusca").click()
        return [cep,logradouro,bairro,localidade]
    

    def ReadPlanilha(self):
        planilha = load_workbook(self.__caminho_plan + "cep.xlsx")
        sheet = planilha.active
        return sheet["A:A"]