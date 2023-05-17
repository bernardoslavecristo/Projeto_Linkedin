import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

df = pd.read_excel('C:\\Users\\Bernardo\\Desktop\\Programacao_computacao\\Projeto_Linkedin\\Relatorio_PA_V1.xlsx', engine='openpyxl')
nomes = df['nome'].tolist()
