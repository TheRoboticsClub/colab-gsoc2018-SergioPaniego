import os


def create_arduino_file(filename):
    filename_parts = filename.split('.ino')
    if not os.path.exists(filename_parts[0]):
        os.makedirs(filename_parts[0])
    global file
    file = open(filename_parts[0] + '/' + filename_parts[0] + '.ino', "w+")

def end_arduino_file():
    check_file()
    file.close()

def setup():
    check_file()
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


def define_engines():
    check_file()
    file.write('const int LEFT_FRONT_FORWARD = 5;\n')
    file.write('const int LEFT_FRONT_BACKWARD = 4;\n')
    file.write('const int RIGHT_FRONT_FORWARD = 2;\n')
    file.write('const int RIGHT_FRONT_BACKWARD = 6;\n')
    file.write('const int LEFT_BACK_FORWARD = 9;\n')
    file.write('const int LEFT_BACK_BACKWARD = 10;\n')
    file.write('const int RIGHT_BACK_FORWARD = 11;\n')
    file.write('const int RIGHT_BACK_BACKWARD = 12;\n')


def set_engines():
    check_file()
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

def define_US():
    check_file()
    file.write('const int echoUS = A5;\n')
    file.write('const int triggerUS= A4;\n')
    file.write('unsigned int timeUS, distanceUS = 50;\n')

def get_US():
    check_file()
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
    check_file()
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

def check_file():
    try:
        file
    except NameError:
        create_arduino_file('ardu')