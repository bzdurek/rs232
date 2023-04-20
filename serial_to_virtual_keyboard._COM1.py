import serial
from pynput.keyboard import Key, Controller


ser = serial.Serial(
    port='COM1',    # Number of COM port, change for your system
    baudrate=9600,  # Port speed
    timeout=1       # Wait for read
)




print("OK, It work's waiting for data from COM1")

keyboard = Controller()

try:
	while(ser.is_open):

		if(ser.in_waiting>0):
            
			rxLine=ser.readline().decode("ascii").strip()
			keyboard.type(rxLine)
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
            
except:
	print("Program closed")	
