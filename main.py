
#program to find roots of an equation using particle swarm optimization algorithim. 
#written in python3

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
import particle

SWARM = {}               #swarm is list of particle objects
GLOBAL_BEST_X = 0        #the best X so far found. 
GLOBAL_BEST_RESULT = 0   #the best result so far found. 


#make each individual particle for the swarm
def makeParticles():
    for i in range(100):    #make 100 particles for the swarm
        SWARM[i] = Particle.Particle()
     
#if a particle gets a better result then set global best to that new result
def checkGlobalBestResult(particle):
    global GLOBAL_BEST_X,GLOBAL_BEST_RESULT                   #tell python these are global variables
    if(abs(particle.best_result) < abs(GLOBAL_BEST_RESULT)):  #check particle's current result against the global best result
        print("\nnew best X "   + str(particle.best_x))
        print("new best result is " + str(particle.best_result) + "\n")
        GLOBAL_BEST_X = particle.best_x
        GLOBAL_BEST_RESULT = particle.best_result

def particleSwarm():
    limit = 20000                                            #limit number of total possible iterations to prevent a possible infinite loop
    while abs(GLOBAL_BEST_RESULT) > 0.000001 and limit > 0:   #while root hasnt been found and while limit hasn't been reached
        for i in SWARM: #for each particle in swarm
            SWARM[i].getNewVelocity(GLOBAL_BEST_X)    #get new velocity for this particle
            SWARM[i].getNewX()                        #get a new x value for this particle
            SWARM[i].solveEquation()                  #try to sovle the equation with the x value of this particle
            SWARM[i].checkBestResult()                #check the current result of the particle with its best result
            #SWARM[i].printInfo()                      #prints information about particle for each iteration
            checkGlobalBestResult(SWARM[i])           #check particles best result against global best result
        limit -= 1                                    #decrement limit by 1 for each iteration of the loop
        print("\nglobal best x is: " + str(GLOBAL_BEST_X))          #the global best x for this iteration
        print("global best result is: " + str(GLOBAL_BEST_RESULT))  #the global best result for this iteration
        print("limit is: " + str(limit) + "\n")


random.seed()                                  #seed the random number generator
makeParticles()                                #make the particles which make up the swarm
GLOBAL_BEST_X = SWARM[0].current_x             #initalize global best x to first particle's x
GLOBAL_BEST_RESULT = SWARM[0].current_result   #initalize global best result to first particle's result
particleSwarm()                                #start process of particle swarm optimization
print("best x is : " + str(GLOBAL_BEST_X))
print("best result is: " + str(GLOBAL_BEST_RESULT))
