import PythonExamples.PyToArAPIExample as api

# Create file
api.create_arduino_file('car_controller')

# Variables declaration and setup
api.define_engines()
api.define_US()
api.setup()

# Functions
api.set_engines()
api.get_US()

# Loop
api.loop()

# End file
api.end_arduino_file()