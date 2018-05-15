const int LEFT_FRONT_FORWARD = 5;
const int LEFT_FRONT_BACKWARD = 4;
const int RIGHT_FRONT_FORWARD = 2;
const int RIGHT_FRONT_BACKWARD = 6;
const int LEFT_BACK_FORWARD = 9;
const int LEFT_BACK_BACKWARD = 10;
const int RIGHT_BACK_FORWARD = 11;
const int RIGHT_BACK_BACKWARD = 12;
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
void setEngines(int leftFrontForward, int leftFrontBackward, int rightForntForward, int rightFrontBackward, int leftBackForward, int leftBackBackward, int rightBackForward, int rightBackBackward) {
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
digitalWrite(triggerUS, LOW);
delayMicroseconds(2);
digitalWrite(triggerUS, HIGH);
delayMicroseconds(10);
digitalWrite(triggerUS, LOW);
timeUS = pulseIn(echoUS, HIGH);
distanceUS = timeUS / 58;
return distanceUS;
}
void loop() {
int distanceUS = getUS();
if (distanceUS < 10) {
Serial.println((String)"STOP!! " + distanceUS + (String)" cm");
setEngines(LOW, LOW, LOW, LOW, LOW, LOW, LOW, LOW);
 } else {
Serial.println(distanceUS + (String)" cm");
setEngines(LOW, HIGH, LOW, HIGH, LOW, HIGH, LOW, HIGH);
}
}
