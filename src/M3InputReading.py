import os
from M4InputChecking import *
import logging
import sys
import datetime


def input_array():

    input_data = {}
    readingError = False;

    try:
        with open(os.path.join("Input", "input.txt")) as f:
            for line in f:
                try:
                    (key, val) = line.split()
                    input_data[str(key)] = float(val)
                except:
                    error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "Could not read the input file.")
                    logging.error(str(error_message))
                    readingError = True
                    sys.exit()
    except:
        if not readingError:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "Input file not found.")
            logging.error(str(error_message))
        sys.exit()

    if verify_input(input_data):
        return input_data


