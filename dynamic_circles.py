"""
File: dynamic_circles.py 
Author: COMP 120 class
Date: October 12, 2021
Description: GUI program to animate growing and shrinking 
concentric circles.
"""

import tkinter as tk 
from enum import Enum

class DynamicCircles:
    def __init__(self):

        # Constants
        self.CANVAS_SIZE = 400
        self.FIRST_RADIUS = 20
        self.DELTA_RADIUS = 30
        self.DELTA_TIME_MILLS = 500

    def run(self):
        """ Start the simulation """
        self.window.mainloop()

        
if __name__ == "__main__":
    # Create program, and get it started
    program = DynamicCircles()
    program.run()
