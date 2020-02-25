"""
Program: Race Results - part of a sailing manager
Author: TwoSails
Version: 1.0.0

"""
# File Format in CSV: race, sailNumber, helm, boatName, correctedTime


class Results:
    def __init__(self, filename, race):
        self.ascending = []
        self.sailors = {}
        self.times = {}
        self.data = {}
        self.filename = filename
        self.race = race

    def readFile(self):  # Reads the whole file
        with open(self.filename, 'r') as file:
            line = file.readline()
            while line != '' and line != ' ':
                field = line.split(',')
                race = field[0]
                sailNumber = field[1]
                helm = field[2]
                boatName = field[3]
                correctedTime = field[4]
                # print(race, sailNumber, helm, boatName, correctedTime)
                self.data[helm] = race, helm, sailNumber, boatName, correctedTime
                line = file.readline()

    def readData(self):  # Selects necessary data required for working out positions
        with open(self.filename, 'r') as file:
            line = 0
            fileLine = file.readline()
            while fileLine != '':
                field = fileLine.split(',')
                if field[0] == self.race:
                    sailor = field[2]
                    time = float(field[4])
                    self.sailors[sailor] = line
                    self.times[time] = sailor
                line += 1
                fileLine = file.readline()

    def ascend(self):  # Prints the race results in ascending order
        # print(self.times)
        for i in sorted(self.times.keys()):
            self.ascending.append(self.times[i])
            # print((i, self.times[i]), end=' ')
        # print('\n' + str(self.ascending))
        for x in self.ascending:
            try:
                self.data[x]
                print(str(self.data[x]).replace('(', '').replace(', ', '').replace(')', '').replace("'' ", ', ').replace("'", "")[:-2])
            except KeyError:
                print('Ascend Function: Error -->', x, 'does not exist')
