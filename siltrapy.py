# coding:UTF-8
# Resolucion de pantalla 1600 x 900
import pyautogui
import time
import subprocess

def abrirSiltra():
	#Ejecutamos programa Siltra
	print 'Ejecutando Siltra 30 segundos'
	subprocess.call(['java', '-jar', 'C:\SILTRA\siltra.jar'])
	time.sleep(30)

def modificarAutorizado(autorizado):
	#Modificamos el autorizado
	print 'Modificamos el autorizado'
	pyautogui.hotkey('Alt','o')
	time.sleep(1)
	pyautogui.hotkey('Alt','P')
	time.sleep(1)
	pyautogui.typewrite(autorizado)
	time.sleep(1)



def guardarConfiguracion():
	#Guardamos la configuracion
	print 'Guardamos la configuracion'
	pyautogui.click(x=1229,y=210)
	time.sleep(1)
	pyautogui.click(x=889,y=468)
	time.sleep(1)
	pyautogui.press('enter')
	time.sleep(1)
	pyautogui.click(x=1073,y=730)#Volver a inicio
	time.sleep(1)
	#print pyautogui.position()

def envioRecepcion():
	print 'Ir a Envio Recepcion'
	pyautogui.click(x=1018,y=177)
	#pyautogui.hotkey('alt','R')
	time.sleep(1)
	pyautogui.click(x=963,y=199) #Boton enviar o recibir
	#pyautogui.hotkey('alt', 'E', interval=0.1)
	#pyautogui.keyDown('Alt')
	#pyautogui.press('E')
	#time.sleep(0.5)
	#pyautogui.keyUp('Alt')
	time.sleep(3)
	#pyautogui.press('enter')
	#time.sleep(1)
	print pyautogui.position()

#Ejecutamos la peticion Envio/Recepcion
#print 'Ejecutamos la peticion Envio/Recepcion'
#pyautogui.hotkey('Alt','I')
#pyautogui.click(x=1065,y=762)
#time.sleep(1)
#pyautogui.hotkey('Alt','R')
#time.sleep(1)

#pyautogui.hotkey('Alt','E')
#time.sleep(10)

def cerrarSiltra():
	#Salimos de Siltra 
	print 'Salimos de Siltra '
	pyautogui.click(x=1206,y=728)
	time.sleep(1) 
	pyautogui.press('enter')


abrirSiltra()
modificarAutorizado('00104892')
guardarConfiguracion()
envioRecepcion()
cerrarSiltra()