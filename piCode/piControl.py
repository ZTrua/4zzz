import serial
import time 

class serMessage:
    def __init__(self): 
        pass

class SerSend:
    def __init__(self, serial, addr, write): 
        # serial is the serial object. write is the function that writes
        self.ser = serial
        self.addr = addr
        self.write = write

    def stx(self): 
        self.write("start of text")

    def addr(self, addr): 
        self.write(self.addr)

    def seq(self):
        self.write("seq")
    
    def etx(self): 
        self.write("end of text")

    def send_data(self, message):
        self.stx() 
        self.addr() 
        self.seq() 
        self.write(message)
        self.etx() 

class SerGet: 
    def __init__(self):
        stx = False
        addr = False
        seq_flag = False 
        ext = False 
        stx_string = "start of text" 
        ext_string = "end of text"
        state = ["stx", "addr", "seq", "message", "ext"] 
        current_state = 0
        seq = 361

    def update_seq(self): 
        # increase sequence number with 360 rollover 

        if self.seq == 361: 
            self.seq = 0
        elif self.seq == 360: 
            self.seq = 0
        elif self.seq > 361: 
            self.ser_error("seq error", "too high")
        else: 
            self.seq = self.seq + 1

        return self.seq
        
    
    def read_serial(self, message): 
        # read the message recieved by the serial and interpret it 
        if self.message == self.stx_string: 
            pass

    def ser_error(self, message, details): 
        pass
    