#!/usr/bin/env python3
# Program: Random Walk Simulation
# Author: Darren Trieu Nguyen
# Version: 0.6
# Function: To simulate brownian motion
# Note: Branched from Diffusion Simulation v.0.6

import turtle
import tkinter
import time
import random
import sys

""" Main class
"""
class simulation:
    
    """ Initialization function - Initializes the screen and randomizes the
        turtles
    """
    def __init__(self, 
            turtleQuantity, 
            xMult, 
            yMult, 
            xBoundInput, 
            yBoundInput,
            windDirectionInput,
            windWeightInput):

        # Constants (will be able to be manipulated later)
        global xBound
        global yBound
        global windDirection
        global windWeight

        xBound = xBoundInput
        yBound = yBoundInput
        windDirection = windDirectionInput
        windWeight = windWeightInput

        global radius
        radius = 7

        global turtleList
        turtleList = []

        # Initializing the screen and background
        window = turtle.Screen()
        window.bgcolor("white")
        window.title("Drawing Board")

        # Labeling borders
        turtle.setworldcoordinates(-xBound, -yBound, xBound, yBound)

        # Drawing borders
        turtle.tracer(False)
        borderTurtle = turtle.Turtle()
        borderTurtle.hideturtle()
        borderTurtle.penup()
        borderTurtle.setx(-xBound)
        borderTurtle.sety(-yBound)
        borderTurtle.pendown()

        borderTurtle.setx(xBound)
        borderTurtle.sety(yBound)
        borderTurtle.setx(-xBound)
        borderTurtle.sety(-yBound)

        # Loading turtles
        self.createNTurtles(xMult, yMult, turtleQuantity)
        turtle.update()
    
        simLoop = 1
        while (simLoop == 1):
            try:
                self.boardUpdate()
            except tkinter.TclError:
                pass
                simLoop = 0

        try:
            turtle.done()
            turtle.bye()
        except turtle.Terminator:
            pass

    """ Creates a turtle
    """
    def createTurtle(self, xMult, yMult):
        turtle1 = turtle.Turtle()
        turtle1.shape("circle")
        turtle1.color("blue")
        turtle1.penup()
        turtle1.setx(random.randint(-100, 100) * xMult)
        turtle1.sety(random.randint(-100, 100) * yMult)
        turtle1.setheading(random.randint(0, 360))
        
        turtleList.append(turtle1)

    """ Create a specific number of turtles
    """
    def createNTurtles(self, xMult, yMult, quantity):
        for n in range(1, quantity):
            self.createTurtle(xMult, yMult)

    """ Updates the board
    """
    def boardUpdate(self):
        for turtle1 in turtleList:
            turtle1.setheading(self.randomDirection(windDirection, windWeight))
            for turtle2 in turtleList:
                if ((not (turtle1 is turtle2)) 
                        and self.checkCollision(turtle1, turtle2)):
                    self.collisionDirection(turtle1, turtle2)
            if ((self.checkBorderCoords(turtle1.xcor(), 
                turtle1.ycor()) == True)):
                self.ricochetDirection(turtle1)
            turtle1.forward(1)
        turtle.update()

    """ Chooses and returns a random direction, factoring in wind direction and
        weights given to the wind
    """
    def randomDirection(self, windDirection, weight):
        if (random.randint(0, 100) < weight):
            return random.randint(windDirection - 45, windDirection + 45)
        else:
            return random.randint(0, 360)

    """ Checks to see if a turtle is outside the borders
        Returns True if the turtle is outside the borders
        Returns False otherwise
    """
    def checkBorder(self, turtleObject):
        if (((turtleObject.xcor() + radius) >= xBound)
                or ((turtleObject.xcor() - radius) <= -xBound)
                or ((turtleObject.ycor() + radius) >= yBound)
                or ((turtleObject.ycor() - radius) <= -yBound)):
            return True
        else:
            return False

    """ Checks to see if a turtle's planned coordinates causes the turtle
        to overlap with the edge of the screen
        Returns True if the coords are past the border
        Returns False otherwise
    """
    def checkBorderCoords(self, xcor, ycor):
        if (((xcor + radius) >= xBound)
                or ((xcor - radius) <= -xBound)
                or ((ycor + radius) >= yBound)
                or ((ycor - radius) <= -yBound)):
            return True
        else:
            return False

    """ Checks to see if a turtle is outside the board completely
        Returns True if the turtle is outside the board completely
        Returns False otherwise
    """
    def checkStuck(self, turtleObject):
        if (((turtleObject.xcor() + radius) >= xBound)
                or ((turtleObject.xcor() - radius) <= -xBound)
                or ((turtleObject.ycor() + radius) >= yBound)
                or ((turtleObject.ycor() - radius) <= -yBound)):
            return True
        else:
            return False

    """ Checks to see if a turtle is overlapping with another turtle
        Returns True if a turtle is overlapping with another turtle
        Returns False otherwise
    """
    def checkCollision(self, turtle1, turtle2):
        if (((((turtle1.xcor() + radius) >= (turtle2.xcor() - radius))
                and ((turtle1.xcor() - radius) <= (turtle2.xcor() - radius)))
                or (((turtle1.xcor() - radius) <= (turtle2.xcor() + radius))
                and ((turtle1.xcor() + radius) >= (turtle2.xcor() + radius))))
                and ((((turtle1.ycor() + radius) >= (turtle2.ycor() - radius))
                and ((turtle1.ycor() - radius) <= (turtle2.ycor() - radius)))
                or (((turtle1.ycor() - radius) <= (turtle2.ycor() + radius))
                and ((turtle1.ycor() + radius) >= (turtle2.ycor() + radius))))
                ):
            return True
        else:
            return False

    """ Changes direction based off of turtle collision
    """
    def collisionDirection(self, turtle1, turtle2):
        turtle1.setheading(turtle1.towards(turtle2.xcor(), 
            turtle2.ycor()) + 180)
        turtle2.setheading(turtle2.towards(turtle1.xcor(), 
            turtle1.ycor()) + 180)

    """ Changes the direction of a turtle as if it ricocheted off of a wall
    """
    def ricochetDirection(self, turtleObject):
        if (turtleObject.xcor() + radius >= xBound):
            turtleObject.setheading(180 - turtleObject.heading())
        if (turtleObject.ycor() + radius >= yBound):
            turtleObject.setheading(360 - turtleObject.heading())
        if (turtleObject.xcor() - radius <= -xBound):
            turtleObject.setheading(180 - turtleObject.heading())
        if (turtleObject.ycor() - radius <= -yBound):
            turtleObject.setheading(360 - turtleObject.heading())

    """ Forces the simulation display closed
    """
    def closeSimulation(self):
        turtle.clear()
        turtle.update()
        turtle.bye()

