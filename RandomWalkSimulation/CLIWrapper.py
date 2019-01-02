#!/usr/bin/env python3
# Program: Random Walk Simulation CLI Wrapper
# Author: Darren Trieu Nguyen
# Version: 0.6
# Function: Wrapper class housing the CLI for randomWalkSimulation.py

import getopt
import sys
from randomWalkSimulation import simulation

""" Command Line Interface handler for the Random Walk Simulation
"""
class CLInterface:

    """ Initialization function
        Handles options from the CLI
    """
    def __init__(self):

        global version
        version = 0.6
        
        # Initializing global variables
        global turtleQuantity
        global xMult
        global yMult
        global xBound
        global yBound
        global windDirection
        global windWeight

        # Setting default values
        turtleQuantity = 20
        xMult = 1
        yMult = 1
        xBound = 500
        yBound = 500
        windDirection = 0
        windWeight = 0

        # Getting options
        self.main()

        # Declaring and initializing simulation
        sim = simulation(turtleQuantity, 
                xMult, 
                yMult, 
                xBound, 
                yBound,
                windDirection,
                windWeight)

        sys.exit()

    """ Prints usage output
    """
    def usage(self):
        print("Diffusion Simulation Version:", version)
        print("Usage:")
        print("  -h, --help             : Prints usage and options.")
        print("  -v, --version          : Prints version.")
        print("  -p, --pQuan <quantity> : Specifies the amount of particles.")
        print("  --xMult <multiplier>   : Scales the range in which particles"\
            " can be created\n"\
            "                           in horizontally.")
        print("  --yMult <multiplier>   : Scales the range in which particles"\
            " can be created\n"\
            "                           in vertically.")
        print("  --xBound <bound>       : Specifies the distance from the"\
            " origin to the border\n"
            "                           along the x-axis.")
        print("  --yBound <bound>       : Specifies the distance from the"\
            " origin to the border\n"
            "                           along the y-axis.")
        print("  --windDir <angle>      : Specifies the direction of the wind")
        print("  --windWeight <weight>  : Specifies how much weight the wind"\
            " will have")

    """ Main method
        Handles options from the CLI
    """
    def main(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hp:v", [
                "help", 
                "version",
                "pQuan=",
                "xMult=",
                "yMult=",
                "xBound=",
                "yBound=",
                "windDir=",
                "windWeight="])
        except getopt.GetoptError as err:
            print(err)
            self.usage()
            sys.exit(2)
        output = None
        verbose = False
        for o, a in opts:
            if o in ("-v, --version"):
                print("Version:", version)
                sys.exit()
            elif o in ("-h", "--help"):
                self.usage()
                sys.exit()
            elif o in ("-p", "--pQuan"):
                global turtleQuantity
                turtleQuantity = int(a)
            elif o in ("--xMult"):
                global xMult
                xMult = float(a)
            elif o in ("--yMult"):
                global yMult
                yMult = float(a)
            elif o in ("-x", "--xBound"):
                global xBound
                xBound = int(a)
            elif o in ("-y", "--yBound"):
                global yBound
                yBound = int(a)
            elif o in ("--windDir"):
                global windDirection
                windDirection = int(a)
            elif o in ("--windWeight"):
                global windWeight
                windWeight = int(a)
            else:
                assert False, "unhandled option"

interface = CLInterface()
#if __name__ == "__main__":
#    interface.main()

