from machine import Pin, UART
import sys
import time

sys.path.append('piCode')
from piControl import SerGet, SerSend

rdData = bytes()

uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), stop=1) 

print("Setup")

while True:
    
    while uart.any() > 0:
        
        print(uart.read())
        
        
    
        
        
    

    