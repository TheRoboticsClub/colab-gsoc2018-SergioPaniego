const int FORWARD = 2;
const int BACKWARD = 6;
const int echoUS = A5;
const int triggerUS= A4;

unsigned int timeUS, distanceUS = 50;

void setup() {
  pinMode(FORWARD, OUTPUT);
  pinMode(BACKWARD, OUTPUT);
  pinMode(echoUS, INPUT);
  pinMode(triggerUS, OUTPUT);
  Serial.begin(9600);
}

void loop() {
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

  //Send result to serial monitor
  if (distanceUS < 10) {
    Serial.print("STOP!! ");
    Serial.print(distanceUS);
    Serial.println(" cm");
    stopEngine();
  } else {
    Serial.print(distanceUS);
    Serial.println(" cm");
    forwardEngine();
  }
}

void forwardEngine(){
    digitalWrite(FORWARD , LOW);
    digitalWrite(BACKWARD , HIGH);
}

void stopEngine() {
  digitalWrite(FORWARD , LOW);
  digitalWrite(BACKWARD , LOW);
}


