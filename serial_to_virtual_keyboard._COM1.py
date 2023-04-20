#pip3 install pynput pyserial

import serial
from pynput.keyboard import Key, Controller


ser = serial.Serial(
    port='COM1',    # Numer portu szeregowego (zmień na odpowiedni dla Twojego systemu)
    baudrate=9600,  # Prędkość transmisji danych
    timeout=1       # Czas oczekiwania na odczyt danych
)




print("OK, działa czekam na dane z COM1")

keyboard = Controller()

try:
	while(ser.is_open):

		if(ser.in_waiting>0):
            
			rxLine=ser.readline().decode("ascii").strip()
			keyboard.type(rxLine)
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
            
except:
	print("Koniec pracy programu")