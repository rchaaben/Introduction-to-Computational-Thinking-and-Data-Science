/**** 7/5/2016 ****/
/**** ramzi.chaaben@telecom-bretagne.eu ****/

For this problem I'm going to simulate the growth of fox and rabbit population in a forest!

The following facts are true about the fox and rabbit population:

- The maximum population of rabbits is determined by the amount of vegetation in the forest, which is relatively stable.

- There are never fewer than 10 rabbits; the maximum population of rabbits is 1000.

- For each rabbit during each time step, a new rabbit will be born with a probability of prabbit reproduction
prabbit reproduction=1.0−current rabbit populationmax rabbit population
In other words, when the current population is near the maximum, the probability of giving birth is very low, and when the current population is small, the probability of giving birth is very high.

- The population of foxes is constrained by number of rabbits.

- There are never fewer than 10 foxes.

- At each time step, after the rabbits have finished reproducing, a fox will try to hunt a rabbit with success rate of pfox eats rabbit
pfox eats rabbit=current rabbit populationmax rabbit population
In other words, the more rabbits, the more likely a fox will eat one.

- If a fox succeeds in hunting, it will decrease the number of rabbits by 1 immediately. Remember that the population of rabbits is never lower than 10.

- Additionally, if a fox succeeds in hunting, then it has a 1/3 probability of giving birth in the current time-step-.

- If a fox fails in hunting then it has a 10 percent chance of dying in the current time-step.

- If the starting population is below 10 then you should do nothing. You should not increase the population nor set the population to 10. 
Start with 500 rabbits and 30 foxes.

- At the end of each time step, record the number of foxes and rabbits.
