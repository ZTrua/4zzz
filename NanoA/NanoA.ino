// NANA A - LOCAL LED LIGHT - MASTER
// enable output after short delay setup serial

class Carrage {
public:
  int seqNo = 361;

  Carrage(int x) {

  }

  void updateSeq() {
    if (seqNo == 361) {
      seqNo = 0;
    } else if (seqNo == 360) {
      seqNo = 0;
    } else {
      seqNo++;
    }
  }

  void stx() {
    // start of tex message
    Serial1.println("start of text");
  }

  void addr() {
    // the address, what device is this?
    Serial1.println("address");
  }

  void seq() {
    // the sequence of the message
    Serial1.println(seqNo);
    updateSeq();
  }

  void etx() {
    // end of text message
    Serial1.println("end of text");
  }

  void sendData(String s) {
    stx();
    addr();
    seq();
    Serial1.println(s);
    etx();
  }
};


class DoorControl : public Carrage {


public:

  bool doorIsOpen;
  bool recievingOpenSignal;
  int address;
  int8_t sequence = 255;
  int doorPin;
  int buttonPin;

  DoorControl(int x, int y): Carrage(doorPin){
    // constructor
    doorPin = x;
    buttonPin = y;
  }

  int readButton() {
    return digitalRead(buttonPin);
  }

  void openDoor() {
    // opens the door
    digitalWrite(doorPin, LOW);
  }

  void closeDoor() {
    // locks the door
    digitalWrite(doorPin, HIGH);
  }
};

DoorControl nano(3, 4);

void setup() {
  // make the built in an output
  pinMode(LED_BUILTIN, OUTPUT);

  char startFlash = 0;  // flash test onboard
  while (startFlash <= 4) {
    startFlash++;
    digitalWrite(LED_BUILTIN, HIGH);
    delay(250);
    digitalWrite(LED_BUILTIN, LOW);
    delay(250);
  }

  digitalWrite(LED_BUILTIN, LOW);  // cleanup and run
  Serial.begin(9600);              // initialize serial:
  Serial1.begin(9600);


  pinMode(nano.doorPin, OUTPUT);
  pinMode(nano.buttonPin, INPUT);
}


void loop() {                       // the loop function runs over and over again forever
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  Serial1.println("h");             // Send a Serial ON to NANO B
  delay(1000);                      // wait for a second

  nano.sendData("message");


  digitalWrite(LED_BUILTIN, LOW);  // turn the LED off by making the voltage LOW
  Serial1.println("i");            // Send a Serial OFF to NANO B
  delay(1000);                     // wait for a second
}
