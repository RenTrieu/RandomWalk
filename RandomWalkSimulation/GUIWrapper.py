#!/usr/bin/env python3
# Program: Random Walk Simulation GUI Wrapper
# Author: Darren Trieu Nguyen
# Version: 0.6
# Function: Wrapper class housing the GUI for randomWalkSimulation.py

from tkinter import *
import sys
from randomWalkSimulation import simulation

""" Graphical User Interface handler for the Random Walk Simulation
"""
class GUInterface:

    global sim

    """ Initialization function for the GUI
    """
    def __init__(self, master):

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

        # GUI
        self.master = master
        master.title("Diffusion Simulation Control Panel")

        self.label = Label(master, text="Control Panel")
        self.label.pack()

        frame = Frame(master)
        frame.pack()
        
        # Declaring and initializing sliders
        # Setting their default values
        turtleQuantityScale = Scale(frame, 
                label="Particle Quantity",
                tickinterval=100,
                to=500)
        turtleQuantityScale.pack(side = LEFT)
        turtleQuantityScale.set(turtleQuantity)

        xMultScale = Scale(frame,
                label="X - Multiplier",
                tickinterval=1,
                to=5)
        xMultScale.pack(side = LEFT)
        xMultScale.set(xMult)

        yMultScale = Scale(frame,
                label="Y - Multiplier",
                tickinterval=1,
                to=5)
        yMultScale.pack(side = LEFT)
        yMultScale.set(yMult)

        xBoundScale = Scale(frame,
                label="X Bound",
                tickinterval=200,
                to=1000)
        xBoundScale.pack(side = LEFT)
        xBoundScale.set(xBound)

        yBoundScale = Scale(frame,
                label="Y Bound",
                tickinterval=200,
                to=1000)
        yBoundScale.pack(side = LEFT)
        yBoundScale.set(yBound)

        windDirectionScale = Scale(frame,
                label="Wind Direction",
                tickinterval=90,
                to=360)
        windDirectionScale.pack(side = LEFT)
        windDirectionScale.set(windDirection)

        windWeightScale = Scale(frame,
                label="Wind Weight",
                tickinterval=20,
                to=100)
        windWeightScale.pack(side = LEFT)
        windWeightScale.set(windWeight)

        # Setting up buttons
        self.start_button = Button(master, 
                text="Start Simulation", 
                command=lambda: self.startSimulation(turtleQuantityScale,
                    xMultScale,
                    yMultScale,
                    xBoundScale,
                    yBoundScale,
                    windDirectionScale,
                    windWeightScale))
        self.start_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    """ Starts the simulation, passing the values shown on the sliders to
        the new instance of the simulation
    """
    def startSimulation(self, 
            turtleQuantityScale,
            xMultScale,
            yMultScale,
            xBoundScale,
            yBoundScale,
            windDirectionScale,
            windWeightScale):
        
        # Assigning the slider values to the actual variables
        turtleQuantity = turtleQuantityScale.get()
        xMult = xMultScale.get()
        yMult = yMultScale.get()
        xBound = xBoundScale.get()
        yBound = yBoundScale.get()
        windDirection = windDirectionScale.get()
        windWeight = windWeightScale.get()

        # If a previous simulation display is still open, forces it closed
        # TODO Fix this
        try:
            sim.closeSimulation()
            print("Reset Simulation")
        except NameError:
            pass

        # Initiates a new simulation
        sim = simulation(turtleQuantity, 
                xMult, 
                yMult, 
                xBound, 
                yBound,
                windDirection,
                windWeight)


root = Tk()
gui = GUInterface(root)
root.mainloop()
