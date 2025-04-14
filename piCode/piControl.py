import serial
import time 

class SerSend:
    def __init__(self, serial, addr): 
        self.ser = serial
        self.addr = addr

    def stx(self): 
        self.ser.write("start of text")

    def addr(self, addr): 
        self.ser.write(self.addr)

    def seq(self):
        self.ser.write("seq")
    
    def etx(self): 
        self.ser.write("end of text")

    def send_data(self, message):
        self.stx() 
        self.addr() 
        self.seq() 
        self.seq.write(message)
        self.etx() 

class SerGet: 
    def __init__(self):
        stx = False
        addr = False
        seq = False 
        ext = False 
        stx_string = "start of text" 
        ext_string = "end of text"
        expected = ["stx", "addr", "seq", "message", "ext"] 