import os
import glob
from pathlib import Path
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import shutil

# Configuração do Selenium
chrome_options = Options()
chrome_options.add_argument("--start-maximized") 
chrome_options.add_argument("--disable-notifications")


# Configurando o diretório de download e o nome do arquivo
download_dir = str(Path.home() / "HD_Externo" / "Conecta"/ "Raw_Data")
chrome_options.add_experimental_option("prefs",
                                       {"download.default_directory": download_dir,
                                        "download.prompt_for_download": False })

# Driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)

# Acessa Site
driver.get("https://conectacampinas.exati.com.br/")
sleep(1)
driver.maximize_window()

#%% ###################################### Login

wait = WebDriverWait(driver,60)
user_box = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="userInfo.password"]')))

# User
user_box = driver.find_element(By.XPATH,"//input[@id = 'userInfo.username']")
user_box.send_keys("xxxxxxxxx")
sleep(1)

# Password
password_box = driver.find_element(By.XPATH,'//*[@id="userInfo.password"]')
password_box.send_keys("xxxxxxxxx")
sleep(1)

# Logar
login_box = driver.find_element(By.XPATH,'//span[. = " Acessar "]')
login_box.click()

print("Login Successfully")
#%% ###################################### Atendimento 


# Menu Principal
menu_principal = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@class = 'v-app-bar__nav-icon ml-0 v-btn v-btn--icon v-btn--round theme--light v-size--default black--text']")))
menu_principal.click()
sleep(1)

# Guia Atendimento
guia_atendimentos = driver.find_element(By.XPATH,'//h4[. =" Atendimentos "]')
guia_atendimentos.click()
sleep(1)

# Espera Loadar os dados
espera_load_dados = wait.until(EC.presence_of_element_located((By.XPATH,'//button[@class = "v-btn v-btn--bottom v-btn--fab v-btn--outlined v-btn--round v-btn--tile theme--light v-size--small dark--text dark--text"]')))
sleep(1)

# Menu 3 pontos
menu_download = driver.find_element(By.XPATH,"//button[@class = 'v-btn v-btn--bottom v-btn--fab v-btn--has-bg v-btn--round v-btn--tile theme--light v-size--small mono-grey-2 mono-grey-40--text']")
menu_download.click()
sleep(1)

# Botao Exportar
exportar_box =  driver.find_element(By.XPATH,"//div[. = ' Exportar para ' and  @class ='v-list-item v-list-item--link theme--light' ]")
exportar_box.click()
sleep(1)

# Tipos Download
menu_tipos_download = driver.find_element(By.XPATH,"//div[. = 'Exportar para']")
menu_tipos_download.click()
sleep(1)

# csv Select
csv_select = driver.find_element(By.XPATH,"//div[. = 'CSV' and @class = 'v-list-item v-list-item--link theme--light']")
csv_select.click()
sleep(1)

# Baixa
download_at =  driver.find_element(By.XPATH,'//div[. = " Exportação "]/button/span')
download_at.click()

# Verifica Se Baixou
def baixou():
    arquivo = os.path.exists(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
    while arquivo == False:
        arquivo = os.path.exists(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
baixou()

# Renomeia
old_name = str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
new_name =  str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{"atendimentos"}.csv')
shutil.move(old_name,new_name)

# Fecha Guia
fecha_guia = driver.find_element(By.XPATH,"//button[@class ='ml-1 mr-1 v-btn v-btn--icon v-btn--round theme--light v-size--default gray--text']")
fecha_guia.click()
print("atendimentos.csv Successfully")

#%% ###################################### Solicitações 

# Menu Principal
menu_principal = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@class = 'v-app-bar__nav-icon ml-0 v-btn v-btn--icon v-btn--round theme--light v-size--default black--text']")))
menu_principal.click()
sleep(1)

# Guia Solicitações
guia_solicitacoes = driver.find_element(By.XPATH,'//h4[. =" Solicitações "]')
guia_solicitacoes.click()
sleep(1)

# Pesquisar (load all data)
pesquisar = driver.find_element(By.XPATH,"//button[@class = 'v-btn v-btn--bottom v-btn--fab v-btn--outlined v-btn--round v-btn--tile theme--light v-size--small dark--text dark--text']")
pesquisar.click()

# Espera Loadar os dados
espera_load_dados = wait.until(EC.presence_of_element_located((By.XPATH,'//button[@class = "v-btn v-btn--bottom v-btn--fab v-btn--outlined v-btn--round v-btn--tile theme--light v-size--small dark--text dark--text"]')))
sleep(1)

# Menu 3 pontos
menu_download = driver.find_element(By.XPATH,"//button[@class = 'v-btn v-btn--bottom v-btn--fab v-btn--has-bg v-btn--round v-btn--tile theme--light v-size--small mono-grey-2 mono-grey-40--text']")
menu_download.click()
sleep(1)

# Botao Exportar
exportar_box =  driver.find_element(By.XPATH,"//div[. = ' Exportar para ' and  @class ='v-list-item v-list-item--link theme--light' ]")
exportar_box.click()
sleep(1)

# Tipos Download
menu_tipos_download = driver.find_element(By.XPATH,"//div[. = 'Exportar para']")
menu_tipos_download.click()
sleep(1)

# csv Select
csv_select = driver.find_element(By.XPATH,"//div[. = 'CSV' and @class = 'v-list-item v-list-item--link theme--light']")
csv_select.click()
sleep(1)

# Baixa
download_at =  driver.find_element(By.XPATH,'//div[. = " Exportação "]/button/span')
download_at.click()

# Verifica Se Baixou
def baixou():
    arquivo = os.path.exists(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
    while arquivo == False:
        arquivo = os.path.exists(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
baixou()

# Renomeia
old_name = str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
new_name =  str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{"solicitacoes"}.csv')
shutil.move(old_name,new_name)

# Fecha Guia
fecha_guia = driver.find_element(By.XPATH,"//button[@class ='ml-1 mr-1 v-btn v-btn--icon v-btn--round theme--light v-size--default gray--text']")
fecha_guia.click()

print("solicitacoes.csv - Successfully")

#%% ###################################### Painel de Ocorrências 

# Menu Principal
menu_principal = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@class = 'v-app-bar__nav-icon ml-0 v-btn v-btn--icon v-btn--round theme--light v-size--default black--text']")))
menu_principal.click()
sleep(1)

# Guia Painel de Ocorrências
guia_solicitacoes = driver.find_element(By.XPATH,'//h4[. =" Painel de Ocorrência "]')
guia_solicitacoes.click()
sleep(1)

# Pesquisar (load all data)
pesquisar = driver.find_element(By.XPATH,"//button[@class = 'v-btn v-btn--bottom v-btn--fab v-btn--outlined v-btn--round v-btn--tile theme--light v-size--small dark--text dark--text']")
pesquisar.click()

# Espera Loadar os dados
espera_load_dados = wait.until(EC.presence_of_element_located((By.XPATH,'//button[@class = "v-btn v-btn--bottom v-btn--fab v-btn--outlined v-btn--round v-btn--tile theme--light v-size--small dark--text dark--text"]')))
sleep(1)

# Menu 3 pontos
menu_download = driver.find_element(By.XPATH,"//button[@class = 'v-btn v-btn--bottom v-btn--fab v-btn--has-bg v-btn--round v-btn--tile theme--light v-size--small mono-grey-2 mono-grey-40--text']")
menu_download.click()
sleep(1)

# Botao Exportar
exportar_box =  driver.find_element(By.XPATH,"//div[. = ' Exportar para ' and  @class ='v-list-item v-list-item--link theme--light' ]")
exportar_box.click()
sleep(1)

# Tipos Download
menu_tipos_download = driver.find_element(By.XPATH,"//div[. = 'Exportar para']")
menu_tipos_download.click()
sleep(1)

# csv Select
csv_select = driver.find_element(By.XPATH,"//div[. = 'CSV' and @class = 'v-list-item v-list-item--link theme--light']")
csv_select.click()
sleep(1)

# Baixa
download_at =  driver.find_element(By.XPATH,'//button[@class = "v-btn v-btn--bottom v-btn--has-bg theme--light v-size--default primary white--text"]')
download_at.click()

# Verifica Se Baixou
def baixou():
    arquivo = os.path.exists(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
    while arquivo == False:
        arquivo = os.path.exists(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
baixou()

# Renomeia
old_name = str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
new_name =  str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{"painel_ocorrencias"}.csv')
shutil.move(old_name,new_name)

# Fecha Guia
fecha_guia = driver.find_element(By.XPATH,"//button[@class ='ml-1 mr-1 v-btn v-btn--icon v-btn--round theme--light v-size--default gray--text']")
fecha_guia.click()

print("painel_ocorrencias.csv - Successfully")

#%% ###################################### Painel de Monitoramento

# Menu Principal
menu_principal = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@class = 'v-app-bar__nav-icon ml-0 v-btn v-btn--icon v-btn--round theme--light v-size--default black--text']")))
menu_principal.click()
sleep(1)

# Guia Painel de Monitoramento
guia_solicitacoes = driver.find_element(By.XPATH,'//h4[. =" Painel de monitoramento "]')
guia_solicitacoes.click()
sleep(1)

# Pesquisar (load all data)
pesquisar = driver.find_element(By.XPATH,"//button[@class = 'v-btn v-btn--bottom v-btn--fab v-btn--outlined v-btn--round v-btn--tile theme--light v-size--small dark--text dark--text']")
pesquisar.click()

# Espera Loadar os dados
espera_load_dados = wait.until(EC.presence_of_element_located((By.XPATH,'//button[@class = "v-btn v-btn--bottom v-btn--fab v-btn--outlined v-btn--round v-btn--tile theme--light v-size--small dark--text dark--text"]')))
sleep(1)

# Menu 3 pontos
menu_download = driver.find_element(By.XPATH,"//button[@class = 'v-btn v-btn--bottom v-btn--fab v-btn--has-bg v-btn--round v-btn--tile theme--light v-size--small mono-grey-2 mono-grey-40--text']")
menu_download.click()
sleep(1)

# Botao Exportar
exportar_box =  driver.find_element(By.XPATH,"//div[. = ' Exportar para ' and  @class ='v-list-item v-list-item--link theme--light' ]")
exportar_box.click()
sleep(1)

# Tipos Download
menu_tipos_download = driver.find_element(By.XPATH,"//div[. = 'Exportar para']")
menu_tipos_download.click()
sleep(1)

# csv Select
csv_select = driver.find_element(By.XPATH,"//div[. = 'CSV' and @class = 'v-list-item v-list-item--link theme--light']")
csv_select.click()
sleep(1)

# Baixa
download_at =  driver.find_element(By.XPATH,'//button[@class = "v-btn v-btn--bottom v-btn--has-bg theme--light v-size--default primary white--text"]')
download_at.click()

# Verifica Se Baixou
def baixou():
    arquivo = os.path.exists(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
    while arquivo == False:
        arquivo = os.path.exists(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
baixou()

# Renomeia
old_name = str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
new_name =  str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{"painel_monitoramento"}.csv')
shutil.move(old_name,new_name)

# Fecha Guia
fecha_guia = driver.find_element(By.XPATH,"//button[@class ='ml-1 mr-1 v-btn v-btn--icon v-btn--round theme--light v-size--default gray--text']")
fecha_guia.click()

print("painel_monitoramento.csv - Successfully")

#%% ###################################### Materiais Aplicados

# Menu Principal
menu_principal = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@class = 'v-app-bar__nav-icon ml-0 v-btn v-btn--icon v-btn--round theme--light v-size--default black--text']")))
menu_principal.click()
sleep(1)

# Guia Painel de Monitoramento
guia_solicitacoes = driver.find_element(By.XPATH,'//h4[. =" Materiais aplicados "]')
guia_solicitacoes.click()
sleep(1)

# Pesquisar (load all data)
pesquisar = driver.find_element(By.XPATH,"//button[@class = 'v-btn v-btn--bottom v-btn--fab v-btn--outlined v-btn--round v-btn--tile theme--light v-size--small dark--text dark--text']")
pesquisar.click()

# Espera Loadar os dados
espera_load_dados = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class = "v-btn v-btn--bottom v-btn--fab v-btn--outlined v-btn--round v-btn--tile theme--light v-size--small dark--text dark--text"]')))
sleep(1)

# Menu 3 pontos
menu_download = driver.find_element(By.XPATH,"//button[@class = 'v-btn v-btn--bottom v-btn--fab v-btn--has-bg v-btn--round v-btn--tile theme--light v-size--small mono-grey-2 mono-grey-40--text']")
menu_download.click()
sleep(1)

# Botao Exportar
exportar_box =  driver.find_element(By.XPATH,"//div[. = ' Exportar para ' and  @class ='v-list-item v-list-item--link theme--light' ]")
exportar_box.click()
sleep(1)

# Tipos Download
menu_tipos_download = driver.find_element(By.XPATH,"//div[. = 'Exportar para']")
menu_tipos_download.click()
sleep(1)

# csv Select
csv_select = driver.find_element(By.XPATH,"//div[. = 'CSV' and @class = 'v-list-item v-list-item--link theme--light']")
csv_select.click()
sleep(1)

# Baixa
download_at =  driver.find_element(By.XPATH,'//button[@class = "v-btn v-btn--bottom v-btn--has-bg theme--light v-size--default primary white--text"]')
download_at.click()

# Verifica Se Baixou
def baixou():
    arquivo = os.path.exists(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
    while arquivo == False:
        arquivo = os.path.exists(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
baixou()

# Renomeia
old_name = str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
new_name =  str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{"materiais_aplicados"}.csv')
shutil.move(old_name,new_name)

# Fecha Guia
fecha_guia = driver.find_element(By.XPATH,"//button[@class ='ml-1 mr-1 v-btn v-btn--icon v-btn--round theme--light v-size--default gray--text']")
fecha_guia.click()

print("materiais_aplicados.csv - Successfully")

#%% ###################################### Ordens De Serviço


# Menu Principal
menu_principal = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@class = 'v-app-bar__nav-icon ml-0 v-btn v-btn--icon v-btn--round theme--light v-size--default black--text']")))
menu_principal.click()
sleep(1)

# Guia Painel de Monitoramento
guia_solicitacoes = driver.find_element(By.XPATH,'//h4[. =" Ordens de serviço "]')
guia_solicitacoes.click()
sleep(1)

# Filtro
filtro = driver.find_element(By.XPATH,"//button[@class = 'v-btn v-btn--bottom v-btn--fab v-btn--has-bg v-btn--round v-btn--tile theme--light v-size--small primary white--text']")
filtro.click()

# Filtro - Status 
filtro_status = driver.find_element(By.XPATH,"//div[. ='Todos ativos' and @class = 'v-select__selections'] ")
filtro_status.click()

# Filtro - Status Todos
filtro_status_all = driver.find_element(By.XPATH,"//div[. ='Todos' and @class = 'v-list-item__title']")
filtro_status_all.click()

# Filtro Aplicar
filtro_aplicar = driver.find_element(By.XPATH,"//span[. =' Aplicar ']")
filtro_aplicar.click()

# Espera Filtro - Fechar
menu_principal = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@class = 'v-icon notranslate v-icon--link material-icons theme--light mono-grey-40--text']")))
menu_principal.click()

# Espera Loadar os dados
espera_load_dados = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class = "v-btn v-btn--bottom v-btn--fab v-btn--outlined v-btn--round v-btn--tile theme--light v-size--small dark--text dark--text"]')))
sleep(1)

# Menu 3 pontos
menu_download = driver.find_element(By.XPATH,"//button[@class = 'v-btn v-btn--bottom v-btn--fab v-btn--has-bg v-btn--round v-btn--tile theme--light v-size--small mono-grey-2 mono-grey-40--text']")
menu_download.click()
sleep(1)

# Botao Exportar
exportar_box =  driver.find_element(By.XPATH,"//div[. = ' Exportar para ' and  @class ='v-list-item v-list-item--link theme--light' ]")
exportar_box.click()
sleep(1)

# Tipos Download
menu_tipos_download = driver.find_element(By.XPATH,"//div[. = 'Exportar para']")
menu_tipos_download.click()
sleep(1)

# csv Select
csv_select = driver.find_element(By.XPATH,"//div[. = 'CSV' and @class = 'v-list-item v-list-item--link theme--light']")
csv_select.click()
sleep(1)

# Baixa
download_at =  driver.find_element(By.XPATH,'//button[@class = "v-btn v-btn--bottom v-btn--has-bg theme--light v-size--default primary white--text"]')
download_at.click()

# Verifica Se Baixou
def baixou():
    arquivo = os.path.exists(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
    while arquivo == False:
        arquivo = os.path.exists(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
baixou()

# Renomeia
old_name = str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
new_name =  str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{"ordens_servico"}.csv')
shutil.move(old_name,new_name)

# Fecha Guia
fecha_guia = driver.find_element(By.XPATH,"//button[@class ='ml-1 mr-1 v-btn v-btn--icon v-btn--round theme--light v-size--default gray--text']")
fecha_guia.click()

print("ordens_servico.csv - Successfully")

#%% ###################################### Ocorrências para Autorizar

# Menu Principal
menu_principal = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@class = 'v-app-bar__nav-icon ml-0 v-btn v-btn--icon v-btn--round theme--light v-size--default black--text']")))
menu_principal.click()
sleep(1)

# Guia Painel de Monitoramento
guia_solicitacoes = driver.find_element(By.XPATH,'//h4[. =" Ocorrências para autorizar "]')
guia_solicitacoes.click()
sleep(1)

# Pesquisar (load all data)
pesquisar = driver.find_element(By.XPATH,"//button[@class = 'v-btn v-btn--bottom v-btn--fab v-btn--outlined v-btn--round v-btn--tile theme--light v-size--small dark--text dark--text']")
pesquisar.click()

# Espera Loadar os dados
espera_load_dados = wait.until(EC.presence_of_element_located((By.XPATH,'//button[@class = "v-btn v-btn--bottom v-btn--fab v-btn--outlined v-btn--round v-btn--tile theme--light v-size--small dark--text dark--text"]')))
sleep(1)

# Menu 3 pontos
menu_download = driver.find_element(By.XPATH,"//button[@class = 'v-btn v-btn--bottom v-btn--fab v-btn--has-bg v-btn--round v-btn--tile theme--light v-size--small mono-grey-2 mono-grey-40--text']")
menu_download.click()
sleep(1)

# Botao Exportar
exportar_box =  driver.find_element(By.XPATH,"//div[. = ' Exportar para ' and  @class ='v-list-item v-list-item--link theme--light' ]")
exportar_box.click()
sleep(1)

# Tipos Download
menu_tipos_download = driver.find_element(By.XPATH,"//div[. = 'Exportar para']")
menu_tipos_download.click()
sleep(1)

# csv Select
csv_select = driver.find_element(By.XPATH,"//div[. = 'CSV' and @class = 'v-list-item v-list-item--link theme--light']")
csv_select.click()
sleep(1)

# Baixa
download_at =  driver.find_element(By.XPATH,'//button[@class = "v-btn v-btn--bottom v-btn--has-bg theme--light v-size--default primary white--text"]')
download_at.click()

# Verifica Se Baixou
def baixou():
    arquivo = os.path.exists(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
    while arquivo == False:
        arquivo = os.path.exists(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
baixou()

# Renomeia
old_name = str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{datetime.now().strftime("%d-%m-%Y")}.csv')
new_name =  str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{"ocorrencias_autorizar"}.csv')
shutil.move(old_name,new_name)

# Fecha Guia
fecha_guia = driver.find_element(By.XPATH,"//button[@class ='ml-1 mr-1 v-btn v-btn--icon v-btn--round theme--light v-size--default gray--text']")
fecha_guia.click()

print("ocorrencias_autorizar.csv - Successfully")


#%% ###################################### Atendimento Quanto Ao Prazo

# Menu Principal
menu_principal = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@class = 'v-app-bar__nav-icon ml-0 v-btn v-btn--icon v-btn--round theme--light v-size--default black--text']")))
menu_principal.click()
sleep(1)

# Guia Painel de Monitoramento
guia_solicitacoes = driver.find_element(By.XPATH,'//h4[. =" Atendimentos quanto ao prazo "]')
guia_solicitacoes.click()
sleep(1)

# Menu Relatorio
menu_download = driver.find_element(By.XPATH,"//button[@class = 'v-btn v-btn--has-bg theme--light v-size--default']")
menu_download.click()
sleep(1)

# Excel
excel = driver.find_element(By.XPATH,"//div[. = 'Excel' and @class = 'v-list-item__content']")
excel.click()
sleep(1)

# Espera Download
driver.implicitly_wait(1)
load = wait.until(EC.invisibility_of_element_located((By.XPATH,'//div[@class = "v-progress-circular v-progress-circular--visible v-progress-circular--indeterminate black--text"]')))
driver.implicitly_wait(1)

# Menu Baixados
header = wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//button[@class = "mx-1 v-btn v-btn--icon v-btn--round theme--light v-size--large white--text"]')))
menu_baixados = header[1]
menu_baixados.click()
sleep(1)

# Baixa 
baixar_relatorio = wait.until(EC.visibility_of_element_located((By.XPATH,'//button[@class = "v-btn v-btn--icon v-btn--round theme--light v-size--default primary--text"]')))
baixar_relatorio.click()
sleep(1)


# Renomeia
old_name = glob.glob(str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data") +'/*' + 'Consultar' +'*' )[0]
new_name =  str(Path.home() / "HD_Externo" / "Conecta" / "Raw_Data" /  f'{"sgi_atendimento_atendimentos_prazo"}.xlsx')
shutil.move(old_name,new_name)

# Fecha Guia
fecha_guia = driver.find_element(By.XPATH,"//button[@class ='ml-1 mr-1 v-btn v-btn--icon v-btn--round theme--light v-size--default gray--text']")
fecha_guia.click()


print("sgi_atendimento_atendimentos_prazo.csv - Successfully")
#%% ###################################### FIM

driver.close()
driver.quit()


print("FIM")
