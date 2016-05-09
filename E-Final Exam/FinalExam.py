import pylab
"""Polyfit"""
a = 1.0
b = 2.0
c = 4.0
yVals = []
xVals = range(-20, 20)
for x in xVals:
    yVals.append(a*x**2 + b*x + c)
yVals = 2*pylab.array(yVals)
xVals = pylab.array(xVals)
try:
    a, b, c, d = pylab.polyfit(xVals, yVals, 3)
    print a, b, c, d
except:
    print 'fell to here'

"""Mean and Variance"""
import numpy as np
a=[0,1,2,3,4,5,6,7,8]
b=[5,10,10,10,15]
c=[0,1,2,4,6,8]
d=[6,7,11,12,13,15]
e=[9,0,0,3,3,3,6,6]
print np.mean(a),np.std(a)
print np.mean(b),np.std(b)
print np.mean(c),np.std(c)
print np.mean(d),np.std(d)
print np.mean(e),np.std(e)

"""possible mean and var"""
def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)

print possible_mean(a),possible_variance(a)
print possible_mean(b),possible_variance(b)
print possible_mean(c),possible_variance(c)
print possible_mean(d),possible_variance(d)
print possible_mean(e),possible_variance(e)