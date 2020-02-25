"""

Program: Handicap system, part of a sailing manager
Author: TwoSails
Version: 1.0.0

Notes:
    corrected-time = (elapsed/PY) x 1000
"""
import configHandicaps as configBoat

# Variables
seriesName = input('Race series: ')
raceName = input('Race name (eg 1 will be [seriesName-1]): ')
filename = seriesName + ".txt"
boats = []
handicaps = configBoat.handicaps
print(handicaps)


# Functions
def fileHandling(file, sail, helm, name, correctTime, race):
    with open(file, 'a') as file:
        data = str(race + ", " + sail + ", " + helm + ", " + name + ", " + str(correctTime) + "\n")
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


def main():
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

        fileHandling(filename, sailNumber, sailor, nameBoat, convertedTime, raceName)
