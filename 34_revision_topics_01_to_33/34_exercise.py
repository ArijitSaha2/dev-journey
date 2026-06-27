# Revision Exercise 34
# Create classes Robot and Car.
# Give both a start() method that prints different messages.
# Create one Robot object and one Car object.
# Call start() using both objects.

import time

class Robot:
    def start(self):
        print("Starting up....please wait....few seconds.....")
        time.sleep(2)
        print("Robot Activated")

class Car:
    def start(self):
        print("Car Ready to go")

robot1 = Robot()
car1 = Car()

robot1.start()
car1.start()