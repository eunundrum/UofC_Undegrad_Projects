#Exercise 2: Non-linear systems of equations. Solving Lorentz System.
#The "odeint" function from "scipy" package is used to intergrate the system
#of ODE's.
import matplotlib.pyplot as plt 
import scipy.integrate as scint
import numpy as np 
import pylab
from mpl_toolkits.mplot3d.axes3d import Axes3D


#Initial Conditions and constants:
initial_state = [0.1,0.0,0.0]

sigma = 10.0
rho = 28.0
beta = 8.0/3.0

#derivative of the main function, f(x,y,z,t), analysis of which is done in this lab:
def fun(state,t):
    x,y,z = state                #assigning the value of a tuple with three entries, "state", to the x,y,z.
    dxdt = sigma*(y - x)         #derivative of x wrt to t.
    dydt = x*(rho - z) - y       #derivative of y wrt to t.
    dzdt = x*y - beta*z          #derivative of z wrt to t.
    dfdt = [dxdt, dydt, dzdt]    #the function returns the result of taking derivative of "f(x,y,z,t)" wrt to t in the form of a tuple with three entries.
    return dfdt
 
#Timeline over which the system of DE's is solved:
t = np.linspace(0.0,50.0, num = 5000) #5K data points is chosen to make phase plots representation look smoother.

#Applying odeint function to solve the Loretnz system, which returns a 3D list with values of x,y,z 
#corresponding to the time, t, under consideration.
f_sol = scint.odeint(fun,initial_state,t)

#The piece of code below extracts the values of x,y,z from "f_sol" 3D array of data
# and appends them to appropriate lists, where those values are stored.
x_list = []
y_list = []
z_list = []
for i in f_sol:
    x_list.append(i[0]) #first entry in each element of the list is always "x"
    y_list.append(i[1]) #second entry in each element of the list is always "y"
    z_list.append(i[2]) #third entry in each element of the list is always "z"   

#Plotting "x-y" phase space plot:
plt.plot(x_list, y_list)
plt.title("x-y phase space")
plt.show()

#Plotting "x-z" phase space plot:
plt.plot(x_list, z_list)
plt.title("x-z phase space")
plt.show()

#Plotting "y-z" phase space plot:
plt.plot(y_list, z_list)
plt.title("y-z phase space")
plt.show()


#Part (b): adding randomness to the code and replotting the phase space plots:
#Initial Condition + random:
initial_state_rn = [0.1,0.0,0.0] + np.random.randn(3)*(1e-10)

#Solving the system:
f_sol_ran = scint.odeint(fun,initial_state_rn,t)

#Similar to the code in part (a).
x_list_rn = []
y_list_rn = []
z_list_rn = []
for i in f_sol:
    x_list_rn.append(i[0]) 
    y_list_rn.append(i[1]) 
    z_list_rn.append(i[2])    

#Plotting "x-y" phase space plot:
plt.plot(x_list_rn, y_list_rn)
plt.title("x-y phase space, fluctuations induced")
plt.show()

#Plotting "x-z" phase space plot:
plt.plot(x_list_rn, z_list_rn)
plt.title("x-z phase space, fluctuations induced")
plt.show()

#Plotting "y-z" phase space plot:
plt.plot(y_list_rn, z_list_rn)
plt.title("y-z phase space, fluctuations induced")
plt.show()