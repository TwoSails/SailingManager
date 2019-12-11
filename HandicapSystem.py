"""

Program: Handicap system, part of a sailing manager
Author: TwoSails
Version: 1.0.0

Notes:
    corrected-time = (elapsed/PY) x 1000
"""
import configHandicaps as configBoat

# Variables
filename = input('Race name: ')
filename = filename + ".txt"
boats = []
handicaps = configBoat.handicaps
print(handicaps)
# Portsmouth Yardsticks
boatOne = 1438
boatTwo = 1000
boatThree = 1350


# Functions
def fileHandling(filename, sailNumber, sailor, nameBoat, convertedTime):
    with open(filename, 'a') as file:
        data = str(sailNumber + ", " + sailor + ", " + nameBoat + ", " + str(convertedTime) + "\n")
        file.write(data)


class Boat:
    def __init__(self, handicap, hours, minutes, seconds):
        self.handicap = handicap
        self.timeHours = hours
        self.timeMinutes = minutes
        self.timeSecond = seconds
        self.totalTime = 0
        self.correctedTime = 0

    def convert(self):
        self.timeHours = (self.timeHours * 60) * 60
        self.timeMinutes = (self.timeMinutes * 60) * 60
        self.totalTime = self.timeMinutes + self.timeHours + self.timeSecond

        return self.totalTime

    def calculate(self):
        self.correctedTime = (self.totalTime / self.handicap) * 1000
        print(round(self.correctedTime, 0))
        return self.correctedTime


randomValue = int(input('How many boats are in the race? '))

for x in range(1, randomValue + 1):
    nameBoat = input('What boat do you want? ')
    sailNumber = input('Enter the sail number: ')
    sailor = input('Sailor: ')
    boatHandicap = int(handicaps[nameBoat])

    print("{0} handicap is {1}".format(nameBoat, boatHandicap))

    timeHours = int(input('Hours taken (integer): '))
    timeMinutes = int(input('Minutes taken (integer): '))
    timeSecond = int(input('Seconds taken (integer): '))

    boat = Boat(boatHandicap, timeHours, timeMinutes, timeSecond)
    boat.convert()
    convertedTime = boat.calculate()

    fileHandling(filename, sailNumber, sailor, nameBoat, convertedTime)

