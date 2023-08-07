#Exercise 5: Curve fitting. I will be using "curve_fit" function from "scipy.optimize" package because it returns values of parameters 
#in a very convenient manner as opposed to manual coding.
import numpy as np 
import math as math
import scipy.optimize as optimize
import matplotlib.pyplot as plt

#loading input file and separating columns to appropriate lists with data:
data = np.loadtxt('damped_oscillation.txt', float)

time = []
angpos = []

for i in data:
    time.append(i[0])    #Each element in the first column is time, that's why it should be indexed as "0"
    angpos.append(i[1])  #Each element in the second column is an angular position => indexed as "1"

#Defining model - damped oscillation (takes time, t, as a variable; and 5 parameters to be determined later):
def damosc(t, theta0, beta, omega, psi, phi):
    return theta0*np.exp(-beta*t)*np.cos(omega*t + psi) + phi #returns the angular position as a function of time.


#Applying optimization routine from "scipy.optimize" to
#determine "best-fit" parameters for a given model using
# "curve_fit" function, which returns an array with optimized
# parameters (ordered, popt) and their variations (optional, povt):
popt, povt = optimize.curve_fit(damosc, time, angpos)

#Extracting "best-fit" parameters from the "popt" array
#(already ordered in right sequence so I can just index them in
# the same manner - one by one):
theta0 = popt[0]
beta = popt[1]
omega = popt[2]
psi = popt[3]
phi = popt[4]

#Printing the values for all fitting parameters:
print('Optimized theta0:',theta0)
print('Optimized beta:', beta)
print('Optimized omega:', omega)
print('Optimized psi:', psi)
print('Optimized phi:', phi)

#Setting up the list where angular position values will be 
#stored for optimized parameters:
angpos_opt = []
for i in time:
    angpos_opt.append(damosc(i,theta0,beta,omega,psi,phi)) #appending the optimized model angular position for each time, t.

#Plotting the original data overlaying the optimized data:
plt.plot(time, angpos, color='r')
plt.plot(time, angpos_opt, color='b')
plt.title("angular position vs. time")
plt.legend(['original','optimized'])
plt.xlabel('time, sec')
plt.ylabel('ang.pos, rad')
plt.show()

