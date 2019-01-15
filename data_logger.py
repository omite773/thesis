import os
import sys
import time
from datetime import datetime
import math
import subprocess

import arduino_handler



########### Function which handles the opening and saving of data #############
def append_log():
    if os.path.isdir("/home/pi/thesis/data_log/"):

        try:
            # Opens the log file
            file = open("home/pi/thesis/data_log/data_log.csv", "a")
        except IOError as e:
            # Some error logging for good measure
            print("There were trouble opening the log file")
            return 2

        # If log file is empty fill the first line with parameter names and units
        if os.stat("home/pi/thesis/data_log/data_log.csv").st_size == 0:
            file.write('Date, Time, Temperature [C]\n')

        # Write the measured parameter values into the log file
        file.write(datetime.now().strtime('%Y-%m-%d') +"," + datetime.now().strtime('%H:%M') + "," + str(temperature) + "," + "\n")

     else:
         # Error which is shown if log file could not be found i.e. directory not found
         print("Log dir not present")


         
            
