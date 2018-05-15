import os
directory = 'car_controller'
filename = 'car_controller.ino'


def openArduinoFile():
    if not os.path.exists(directory):
        os.makedirs(directory)
    global file
    file = open(directory + '/' + filename, "w+")

def endArduinoFile():
    checkFile()
    file.close()

def setup():
    checkFile()
    file.write('void setup() {\n')
    file.write('pinMode(LEFT_FRONT_FORWARD, OUTPUT);\n')
    file.write('pinMode(LEFT_FRONT_BACKWARD, OUTPUT);\n')
    file.write('pinMode(RIGHT_FRONT_FORWARD, OUTPUT);\n')
    file.write('pinMode(RIGHT_FRONT_BACKWARD, OUTPUT);\n')
    file.write('pinMode(LEFT_BACK_FORWARD, OUTPUT);\n')
    file.write('pinMode(LEFT_BACK_BACKWARD, OUTPUT);\n')
    file.write('pinMode(RIGHT_BACK_FORWARD, OUTPUT);\n')
    file.write('pinMode(RIGHT_BACK_BACKWARD, OUTPUT);\n')
    file.write('pinMode(echoUS, INPUT);\n')
    file.write('pinMode(triggerUS, OUTPUT);\n')
    file.write('Serial.begin(9600);\n')
    file.write('}\n')


def defineEngines():
    checkFile()
    file.write('const int LEFT_FRONT_FORWARD = 5;\n')
    file.write('const int LEFT_FRONT_BACKWARD = 4;\n')
    file.write('const int RIGHT_FRONT_FORWARD = 2;\n')
    file.write('const int RIGHT_FRONT_BACKWARD = 6;\n')
    file.write('const int LEFT_BACK_FORWARD = 9;\n')
    file.write('const int LEFT_BACK_BACKWARD = 10;\n')
    file.write('const int RIGHT_BACK_FORWARD = 11;\n')
    file.write('const int RIGHT_BACK_BACKWARD = 12;\n')


def setEngines():
    checkFile()
    file.write('void setEngines(int leftFrontForward, int leftFrontBackward, int rightForntForward, int rightFrontBackward, '
               'int leftBackForward, int leftBackBackward, int rightBackForward, int rightBackBackward) {\n')
    file.write('digitalWrite(LEFT_FRONT_FORWARD , leftFrontForward);\n')
    file.write('digitalWrite(LEFT_FRONT_BACKWARD , leftFrontBackward);\n')
    file.write('digitalWrite(RIGHT_FRONT_FORWARD , rightForntForward);\n')
    file.write('digitalWrite(RIGHT_FRONT_BACKWARD , rightFrontBackward);\n')
    file.write('digitalWrite(LEFT_BACK_FORWARD , leftBackForward);\n')
    file.write('digitalWrite(LEFT_BACK_BACKWARD , leftBackBackward);\n')
    file.write('digitalWrite(RIGHT_BACK_FORWARD , rightBackForward);\n')
    file.write('digitalWrite(RIGHT_BACK_BACKWARD , rightBackBackward);\n')
    file.write('}\n')

def defineUS():
    checkFile()
    file.write('const int echoUS = A5;\n')
    file.write('const int triggerUS= A4;\n')
    file.write('unsigned int timeUS, distanceUS = 50;\n')

def getUS():
    checkFile()
    file.write('int getUS() {\n')
    file.write('digitalWrite(triggerUS, LOW);\n')
    file.write('delayMicroseconds(2);\n')
    file.write('digitalWrite(triggerUS, HIGH);\n')
    file.write('delayMicroseconds(10);\n')
    file.write('digitalWrite(triggerUS, LOW);\n')
    file.write('timeUS = pulseIn(echoUS, HIGH);\n')
    file.write('distanceUS = timeUS / 58;\n')
    file.write('return distanceUS;\n')
    file.write('}\n')

def loop():
    checkFile()
    file.write('void loop() {\n')
    file.write('int distanceUS = getUS();\n')
    file.write('if (distanceUS < 10) {\n')
    file.write('Serial.println((String)"STOP!! " + distanceUS + (String)" cm");\n')
    file.write('setEngines(LOW, LOW, LOW, LOW, LOW, LOW, LOW, LOW);\n')
    file.write(' } else {\n')
    file.write('Serial.println(distanceUS + (String)" cm");\n')
    file.write('setEngines(LOW, HIGH, LOW, HIGH, LOW, HIGH, LOW, HIGH);\n')
    file.write('}\n')
    file.write('}\n')

def checkFile():
    try:
        file
    except NameError:
        openArduinoFile()