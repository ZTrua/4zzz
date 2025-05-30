try:
    from machine import Pin, UART
    
    from piControl import SerSend
except RuntimeError: 
    print("Error") 

import time

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1.0)
ser.reset_input_buffer() 
sent = SerSend(ser, "Rasp4", ser.write)
print("Serial Ok") 

try: 
    while True: 
        time.sleep(0.01)
        if ser.in_waiting > 0: 
            line = ser.read().decode('utf-8') 
            print(line) 
        
except KeyboardInterrupt: 
    print("Close Serial Communication") 
    ser.close() 

