#Exercise 3: Solving the Laplace Equation written in 2D Cartesian coordinates representing heat conductance.
#The finite difference method (FDM) was used to find the solution. The FDM is one of the simplest methods for
#solving DE's, especially those ones which are (almost) impossible to solve analytically.
import matplotlib.pyplot as plt 
import numpy as np

#Grid size:
L = 10

#Number of points:
N = 30

#Boundary conditions of the problem:
T_bottom = 0
T_left = 0
T_right = 0
T_top = 100

#New boundary condition for part (B):
T_right_b = 50

#Initial temperature guess, can be anything:
T_guess = 48

#Dimensions of a Meshgrid:
x = np.linspace(0,L,N)
y = np.linspace(0,L,N)

#Setting up the meshgrid:
Y, X = np.meshgrid(y, x)

#Setting the size of "T" 2D-array:
T = np.zeros((N,N))

#Setting the size of new "T" 2D array for part(b):
T_new = np.zeros((N,N))

#Boundary conditions:
T[(len(Y)-1):, :] = T_top     #Sets up the temperature of the upper side
T[:1, :] = T_bottom           #Sets up the temperature of the bottom side
T[:, (len(X)-1):] = T_right   #Sets up the temperature of the right side
T[:, :1] = T_left             #Sets up the temperature of the left side

#Boundary conditions for part(b):
#Setting BC's:
T_new[(len(Y)-1):, :] = T_top
T_new[:1, :] = T_bottom
T_new[:, (len(X)-1):] = T_right_b   #Only right BC was changed, other BC's stay the same.
T_new[:, :1] = T_left

#Setting initial # of iterations to zero and total number of iterations to be perfromed:
iterations = 0
ntotal = 1e4

#Main triple loop iterating through each i,j - pair, calculating value of temperature, "T", at each i,j - pair,
#and assigning the result to the empty list defined above. Each i-j pair represents the cartesian coordinate, (x,y), on the
#meshgrid of the point for which we are calculating temperature
while iterations < ntotal:
    for j in range(1,N-1):
        for i in range(1,N-1):
            T[i,j] = 0.25*(T[i+1,j] + T[i-1,j] + T[i,j+1] + T[i,j-1])                     #for part(a)
            T_new[i,j] = 0.25*(T_new[i+1,j] + T_new[i-1,j] + T_new[i,j+1] + T_new[i,j-1]) #for part(b) with right BC set up to 50 degrees.
    iterations += 1

#Plotting the colourmap for part (a):
plt.figure()
plt.plot(X, Y, marker='.', markeredgewidth=0.07, color='k', linestyle='none')
plt.title("Figure 1: solution as a colourmap")
plt.xlabel("x, cm")
plt.ylabel("y, cm")
Sol = plt.contour(X,Y,T,50)
plt.colorbar(Sol, shrink=0.8, extend='both')
plt.show()

#Plotting the colourmap for part(b):
plt.figure()
plt.plot(X, Y, marker='.', markeredgewidth=0.07, color='k', linestyle='none')
plt.title("Figure 2: solution as a colourmap")
plt.xlabel("x, cm")
plt.ylabel("y, cm")
Sol_new = plt.contour(X,Y,T_new,50)
plt.colorbar(Sol_new, shrink=0.8, extend='both')
plt.show()
