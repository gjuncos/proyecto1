from django.shortcuts import render
from django.http import HttpResponse
from app.whatsapp.models import Contacto
import time
import sys,os, inspect
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Create your views here.


#va a mostar en una pagina solo index
def index(request):
	return render(request,'whatsapp/index.html')

def contactos_list(request):
	contacto= Contacto.objects.all()
	contexto = {'contactos':contacto}
	return render(request,'whatsapp/index.html',contexto)

def enviar_mensaje(contactos):
	carpeta = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe() ))[0]))
	pat = os.path.join(carpeta,"chromedriver.exe")
	print(pat)
	contador=0
	resultado = None
	browser = webdriver.Chrome(pat)
	#"C:\\Users\\Alumno\\Desktop\\Proyecto\\venv\\chromedriver.exe"
	browser.get("https://web.whatsapp.com")
	browser.implicitly_wait(30)
	print("logueate")
	input("Presione una tecla para continuar")

	for c in contactos:
		browser.execute_script("window.open()")
		browser.switch_to_window(browser.window_handles[1])
		browser.get('https://api.whatsapp.com/send?phone='+c.telefono)



		enviar=browser.find_element_by_xpath('//*[@id="action-button"]')
		enviar.click()
		time.sleep(30)
		no_encontrado=browser.find_element_by_xpath('/html/body').text


		if "El número de teléfono compartido a través de la dirección URL es inválido" in no_encontrado or "Enviar mensaje a" in no_encontrado or no_encontrado in "Enlace incorrecto" or "Phone number shared via url is invalid" in no_encontrado:
			resultado = "MENSAJE NO ENVIADO"
			print(resultado)
	
		else:
			msg_box=browser.find_element_by_xpath("//div[@contenteditable='true']")
			#telefono es la tabla
			mens = "hola esto es una prueba desde una pagina"
			msg_box.send_keys(mens)
			msg_box.send_keys(Keys.RETURN)
			resultado = "MENSAJE ENVIADO"
			contador +=1
			print(resultado)
			print(contador)
		browser.close()
		browser.switch_to_window(browser.window_handles[0])



def contactos_list_enviar(request):
	contacto= Contacto.objects.all()
	contexto = {'contactos':contacto}

	#enviar_mensaje(contacto)

	return render(request,'whatsapp/enviar.html',contexto)



