# Function that reads ultrasound sensor and stops the car if the distance to an object is less than 0cm
def get_US():
    print('Ultrasound sensor manager')
    distance = 11
    while distance > 10:
        try:
            distance = int(input('Enter distance: '))
        except ValueError:
            print('Not a number')
    print('STOP! You\'re to close to an obstacle')

# Function that allows you to set the engine forward or backward
def set_engine():
    direction = -1
    print('Engine direction manager')
    while direction != 0:
        try:
            direction = int(input('Enter direction: '))
            if direction == 1:
                print('Backward')
            elif direction == 2:
                print('Forward')
        except ValueError:
            print('Not a number')

def car_controller():
    value = -1
    while value != 0:
        print('Choose the program you want to use typing its number')
        print('0. End program')
        print('1. Get Ultrasound')
        print('2. Set Engine direction')
        try:
            value = int(input('Input: '))
            if value == 1:
                get_US()
            elif value == 2:
                set_engine()
        except ValueError:
            print('Not a number')
    print('Program ended! Bye!')

car_controller()

