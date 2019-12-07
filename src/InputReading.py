from DataStructure import DataStructure
from InputChecking import verifyInputs

import os

def inputArray():
    inputData = DataStructure()
    
    filepath = "/home/ubuntu/environment/Peter Module 3/input.txt"
    if os.path.exists(filepath):
        try:
            fh = open(filepath)
            line = fh.readline()
            while line:
                contents = line.split(",")
                key = contents[0]
                value = contents[1]
                inputData.add(key,value)
                line = fh.readline()
            fh.close()
    
            if verifyInputs(inputData):
                return inputData
        except:
            print("Error: Could not read the input file.")
    else:
        print("Input file not found.")
    
inputArray()

