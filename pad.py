
thing = '\x01\x02pico\x03\x024\x03\x02Hi\x03\x04\x01\x02pico\x03\x025\x03\x02Bye\x03\x04'
easy = ['\x02pico\x03\x024\x03\x02Hi\x03\x04', '\x02pico\x03\x025\x03\x02Bye\x03']
one = []

class Message:
    def __init__(self):
        self.addr = ""
        self.seq = 0
        self.message = "" 

print(thing.rsplit('\x01'))

stuff = '\x21ass' 

for x in thing: 
    pass

#look for \x01 