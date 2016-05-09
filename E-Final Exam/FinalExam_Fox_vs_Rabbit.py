import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    global MAXRABBITPOP
    # TO DO
    Prob_repro=1.0-float(CURRENTRABBITPOP)/float(MAXRABBITPOP)
    Prob_repro_sample=random.random()
    if Prob_repro_sample<Prob_repro:
        CURRENTRABBITPOP+=1
        
    pass
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    global MAXRABBITPOP
    # TO DO
    Prob_hunt=float(CURRENTRABBITPOP)/float(MAXRABBITPOP)
    Prob_hunt_sample=random.random()
    if Prob_hunt_sample<Prob_hunt:
        if CURRENTRABBITPOP>10:
            CURRENTRABBITPOP-=1
            Prob_birth=float(1)/float(3)
            Prob_birth_sample=random.random()
            if Prob_birth_sample<Prob_birth:
                CURRENTFOXPOP+=1
    else:
        Prob_death=random.random()
        if Prob_death<0.9 and CURRENTFOXPOP>10:
            CURRENTFOXPOP-=1
                
    pass
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations=[]
    fox_populations=[]
    # TO DO
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)
    
(rabbit_populations, fox_populations)=runSimulation(200)
print (rabbit_populations, fox_populations)
pylab.figure(1)
pylab.plot(range(200),rabbit_populations)
pylab.figure(2)
pylab.plot(range(200),fox_populations)
coeff = pylab.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
coeff1 = pylab.polyfit(range(len(fox_populations)), fox_populations, 2)
pylab.figure(3)
pylab.plot(pylab.polyval(coeff, range(len(rabbit_populations))))
pylab.figure(4)
pylab.plot(pylab.polyval(coeff1, range(len(fox_populations))))
pylab.show()