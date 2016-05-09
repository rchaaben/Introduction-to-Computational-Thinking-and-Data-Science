/**** 7/5/2016 ****/
/**** ramzi.chaaben@telecom-bretagne.eu ****/

In this problem set, using Python and Pylab I designed and implemented a stochastic simulation of patient and virus population dynamics, and reach conclusions about treatment regimens based on the simulation results.

===> Classes:
* SimpleVirus:
Representation of a simple virus (does not model drug effects/resistance).
* Patient:
Representation of a simplified patient. The patient does not take any drugs and his/her virus populations have no drug resistance.
* ResistantVirus:
Representation of a virus which can have drug resistance.
* TreatedPatient:
Representation of a patient. The patient is able to take drugs and his/her virus population can acquire resistance to the drugs he/she takes.
* RandomWalkRobot:
is a robot with the "random walk" movement strategy: it chooses a new direction at random at the end of each time-step.

===> Functions:
* simulationWithoutDrug:
runs a complete Without Drug simulation.
* simulationWithDrug : 
runs a complete With Drug simulation.
* simulationDelayedTreatment:
runs a complete With delayed Drug simulation.