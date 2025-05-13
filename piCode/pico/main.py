from machine import Pin, UART
import sys
import time

sys.path.append('piCode')
from piControl import SerGet, SerSend

uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

serSend = SerSend(uart, 'pico', uart.write, time.sleep)  

while True:

    message = "hello world"
    serSend.send_data("Hi")
    print("sent")

    time.sleep(1) 
