"""
Program: Sailing Manager
Author: TwoSails
Version: 1.0.1
"""

from HandicapSystem import *
from raceResults import Results
from time import sleep

main()
sleep(5)
result = Results(input('File: '), input('Race: '))
result.readFile()
result.readData()
result.ascend()
