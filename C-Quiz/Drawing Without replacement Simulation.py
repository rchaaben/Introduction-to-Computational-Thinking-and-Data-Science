def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    count=0
    for i in range(numTrials):
        balls=['r','r','r','r','g','g','g','g']
        taken=[]
        for i in range(3):
            k=random.choice(range(8-i))
            taken.append(balls[k])
            balls.remove(balls[k])
        if taken[0]==taken[1] and taken[1]==taken[2]:
            count+=1
    return float(count)/float(numTrials)  