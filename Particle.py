
"""particle class for particle swarm optimization"""
"""class is for each individual particle which makes up the particle swarm. """


# Copyright (C) <2020>  <github username: return5>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import random


class Particle:
    """class for making particle objects as part of a swarm."""
    C_1 = 1.5        #cognitive coefficient. 
    C_2 = 1.5        #social coefficient
    INERTIAL_W = .8  #interia coefficient
    MIN_X = -100     #minimum possible value for x to take
    MAX_X = 100      #maximum possible value for x to take.

    def __init__(self):
        """init particle object."""
        self.current_x = random.uniform(self.MIN_X,self.MAX_X)  #current x value for particle.initialize to a random number within range of MIN_X and MAX_X
        self.best_x = self.current_x                 #current best x value the particle has found
        self.current_result = 100                    #result of plugging in current x into the equation
        self.solveEquation()                         #solve equation with current x to get true current result
        self.best_result = self.current_result       #best result particle has found
        self.velocity = random.uniform(-5,5)         #how far the particle should move per iteration. initalize to random value

    def checkBestResult(self):
        """if current x gives a better result than best x then set best to current."""
        if(abs(self.current_result) < abs(self.best_result)):
            self.best_result = self.current_result
            self.best_x = self.current_x

    def solveEquation(self):
         """attempt to solve the equation with the current_x for this particle. set the current result to the esult of the equation
        equation here is 3x^3 -x^2 + 7x + 3891.3369
        correct x for this equation is 4.2...
        self.current_result = (3*self.current_x**3) - (self.current_x**2) +( 7*self.current_x) - 234.024
        """

    def printInfo(self):    
        """prints the relevant information for that particle"""
        print("x: " + str(self.current_x) + " best_result: " + str(self.best_result) + " velocity: " + str(self.velocity))

    def getNewX(self):
        """get new x value for the particle. checks to make sure the new x value is inside the range of MIN_x and MAX_X"""
        self.current_x = self.current_x + self.velocity
        if(self.current_x < self.MIN_X):
            self.current_x = self.MIN_X
        elif(self.current_x > self.MAX_X):
            self.current_x = self.MAX_X


    def getNewVelocity(self,GLOBAL_BEST_X):
        """get new velocity for the particle. 
        first part of algorithim is the weight of the current velocity
        second part is how far the current result is from best result weighted by the cognitive coefficient with some randomness thrown in
        third part is how far current best x is from global x  weighted by the social coefficient with some randomness thrown in.
        """
        self.velocity =  (self.INERTIAL_W * self.velocity) + (self.C_1 * random.uniform(0,2) * (self.best_x - self.current_x)) + (self.C_2 * random.uniform(0,2) * (GLOBAL_BEST_X - self.current_x))
