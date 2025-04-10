// NANO B -- REMOTE LED LIGHT - SLAVE
// enable output after short delay setup serial

class recieve {
  public: 
    bool stx; 
    bool addr; 
    bool seq; 
    bool ext; 
    int lastSeq; 
    String expected[5] = {"stx", "addr", "seq", "message", "ext"}; 
    String stxString = "start of text"; 
    String extString = "end of text"; 
};

void setup() {
  // make the built in an output
  pinMode(LED_BUILTIN, OUTPUT);

  char startFlash = 0;  // flash test onboard
  while (startFlash <= 2) {
    startFlash++;
    digitalWrite(LED_BUILTIN, HIGH);
    delay(500);   
    digitalWrite(LED_BUILTIN, LOW); 
    delay(500);
    }
    
   digitalWrite(LED_BUILTIN, LOW); // cleanup and run
   Serial.begin(9600);  // initialize serial:
   Serial1.begin(9600); 
}


void loop() {  // the loop function runs over and over again forever
  while (Serial1.available() > 0) {  // if there's any serial available, read it:  
    // Serial.println("available");
    int led = Serial1.read();    // look for the valid integer in the incoming serial stream:
    Serial.write(led);
      // look for the newline. That's the end of your command:
      if (led == 104) { digitalWrite(LED_BUILTIN, HIGH); }
      else if(led == 105) { digitalWrite(LED_BUILTIN, LOW); }
    }
  
}
