/**** 7/5/2016 ****/
/**** ramzi.chaaben@telecom-bretagne.eu ****/

In this problem set, I coded a simulation to compare how much time a group of Roomba-like robots will take to clean the floor of a room using two different strategies.

===> Classes:
* Position:
Stores the x- and y-coordinates of a robot in a room.
* RectangularRoom:
Represents the space to be cleaned and keeps track of which tiles have been cleaned.
* Robot:
Stores the position and direction of a robot.
* StandardRobot:
is a Robot with the standard movement strategy.
* RandomWalkRobot:
is a robot with the "random walk" movement strategy: it chooses a new direction at random at the end of each time-step.

===> Functions:
* runSimulation:
runs a complete robot simulation.
* showPlot1 & showPlot2 : Data plotting.