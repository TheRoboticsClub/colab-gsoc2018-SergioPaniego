// Car engines declaration
const int LEFT_FRONT_FORWARD = 5;
const int LEFT_FRONT_BACKWARD = 4;

const int RIGHT_FRONT_FORWARD = 2;
const int RIGHT_FRONT_BACKWARD = 6;

const int LEFT_BACK_FORWARD = 9;
const int LEFT_BACK_BACKWARD = 10;

const int RIGHT_BACK_FORWARD = 11;
const int RIGHT_BACK_BACKWARD = 12;

// Ultrasonic sensor declaration
const int echoUS = A5;
const int triggerUS= A4;

unsigned int timeUS, distanceUS = 50;

void setup() {
  pinMode(LEFT_FRONT_FORWARD, OUTPUT);
  pinMode(LEFT_FRONT_BACKWARD, OUTPUT);
  pinMode(RIGHT_FRONT_FORWARD, OUTPUT);
  pinMode(RIGHT_FRONT_BACKWARD, OUTPUT);
  pinMode(LEFT_BACK_FORWARD, OUTPUT);
  pinMode(LEFT_BACK_BACKWARD, OUTPUT);
  pinMode(RIGHT_BACK_FORWARD, OUTPUT);
  pinMode(RIGHT_BACK_BACKWARD, OUTPUT);
  
  pinMode(echoUS, INPUT);
  pinMode(triggerUS, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int distanceUS = getUS();
  //Send result to serial monitor
  if (distanceUS < 10) {
    Serial.println((String)"STOP!! " + distanceUS + (String)" cm");
    // Stop engines
    setEngines(LOW, LOW, LOW, LOW, LOW, LOW, LOW, LOW);
  } else {
    Serial.println(distanceUS + (String)" cm");
    // Forward engines
    setEngines(LOW, HIGH, LOW, HIGH, LOW, HIGH, LOW, HIGH);
  }
}

void setEngines(int leftFrontForward, int leftFrontBackward, int rightForntForward, int rightFrontBackward, 
                int leftBackForward, int leftBackBackward, int rightBackForward, int rightBackBackward) {
  digitalWrite(LEFT_FRONT_FORWARD , leftFrontForward);
  digitalWrite(LEFT_FRONT_BACKWARD , leftFrontBackward);
  
  digitalWrite(RIGHT_FRONT_FORWARD , rightForntForward);
  digitalWrite(RIGHT_FRONT_BACKWARD , rightFrontBackward);
  
  digitalWrite(LEFT_BACK_FORWARD , leftBackForward);
  digitalWrite(LEFT_BACK_BACKWARD , leftBackBackward);
  
  digitalWrite(RIGHT_BACK_FORWARD , rightBackForward);
  digitalWrite(RIGHT_BACK_BACKWARD , rightBackBackward);            
}

int getUS() {
  // Trigger pulse
  digitalWrite(triggerUS, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerUS, HIGH);
  // Pulse lasts at least 10 mS
  delayMicroseconds(10);
  digitalWrite(triggerUS, LOW);
  // Measure time in high state on echo pin.
  // The pulse is proportional to the mean distance
  timeUS = pulseIn(echoUS, HIGH);

  // Sound speed is 340 m/s | 29 ms/cm
  // We divide the pulse time by 58, time the sound wave takes to cover 1 cm
  distanceUS = timeUS / 58;
  return distanceUS;
}
