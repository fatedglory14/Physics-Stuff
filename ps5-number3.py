from scipy import *
from matplotlib import *
from numpy import *

NX = 5
NY = 5
maxdiff = 1e-6
diff = 1.0 # must start bigger than 'maxdiff'
V = zeros((NY,NX),float) # fill 'V' with zeros
# Enter the boundary conditions for 'V' other than 0
for i in arange(0,NX,1): # j from 0 to NY-1
    V[NX-1,i] = 20.
    V[0,i] = 100.
print V # print the starting values
itera = 0
while diff > maxdiff: # repeat until 'diff' is small
    diff = 0.0 # reset for each iteration
    # Loop over all of the interior points
    for i in arange(1,NY-1,1): # i from 1 to NY-2
        for j in arange(1,NX-1,1): # j from 1 to NX-2
            newVij = (V[i-1,j]+V[i+1,j]
                      +V[i,j-1]+V[i,j+1])/4.0
            lastdiff = abs(newVij-V[i,j])
            if lastdiff > diff:
                diff = lastdiff
            V[i,j] = newVij
    print V
    itera += 1
print V
print itera
