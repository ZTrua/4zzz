
class serMessage:
    def __init__(self): 
        pass

class SerSend:
    def __init__(self, serial, addr, write, time): 
        # serial is the serial object. write is the function that writes
        self.ser = serial
        self.addr = addr
        self.write = write
        self.seq = 361
        self.time = time

    def stx(self): 
        self.write("\x01")
        #self.time(0.1)

    def addre(self):
        self.write("\x02")
        self.write(self.addr)
        self.write("\x03")
        #self.time(0.1)

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
        self.write("\x02")    
        self.write(str(self.seq)+ " ")
        self.write("\x03")
        #self.time(0.1)

    
    def etx(self): 
        self.write("\x03")
        #self.time(0.1)
        
        
    def write_msg(self, message):
        self.write("\x02")
        self.write(message)
        self.write("\x03")
        #self.time(0.1)

    def send_data(self, message):
        self.stx()
        
        self.addre()
        
        self.update_seq()
        
        self.write_msg(message)
        
        self.etx()
        
        

class SerGet: 
    def __init__(self):
        stx = False
        addr = False
        seq_flag = False 
        etx = False 
        stx_string = "\x02"
        etx_string = "\x03"
        state = ["stx", "addr", "seq", "message", "etx"] 
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
    