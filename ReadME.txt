How to run:
Either run the executable mars_exploration to open a simulation with the warning storm rover,
deliberative_miner and hybrid_drone1.

To choose other configurations, open the .py file mars_exploration with a python
editor like IDLE and execute.

Setup:
In the file mars.py it is possible to change the rover in the function def make_agents . It is
possible to change the rover by commenting and uncommenting one of the lines r.append(....) . 

In the file agent.py, in the first function of the class rover, it is possible to change the 
self.carried_drones and self.carried_miners. It is possible to choose any combination of two
of these agents by replacing the name of the drones and miners, i.e. 

   self.carried_drones = [hybrid_drone2(-1,-1,self.planet),hybrid_drone2(-1,-1,self.planet)]
   self.carried_miners = [deliberative_miner(-1,-1,self.planet),deliberative_miner(-1,-1,self.planet)]

or by commenting and uncommenting one of the predefined combinations.
##################################################################################################
Other commands
"p" - Pauses the simulation, press again to resume
"1" - Changes the simulation velocity to 1 iteration per second
"2"
"3"
.
.
.
"9"
"0" - Faster simulation velocities

"e" - end the simulation
"del" - closes the simulation (same as pressing cross)

