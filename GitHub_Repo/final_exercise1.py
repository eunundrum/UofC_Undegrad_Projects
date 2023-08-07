#Exercise 1: Finding minima of functions
import matplotlib.pyplot as plt 

#Given paramaters and constants:
eps = 0.997 #kJ/mol
sigma = 3.40 #Angstrom

#Lennard-Jones potential definition:
def pot(r):
    res = 4*eps*((sigma/r)**12-(sigma/r)**6) #potential function
    return res #returns the value of potential at given "r"

#Derivative of Lennard-Jones potential (needed for Newton-Raphson method):
def pot_der(r):
    res = 4*eps*(-12*sigma**12/r**13 + 6*sigma**6/r**7) #derivative of potential function
    return res #returns the value of the potential derivative at given "r"

#Second derivative of Lennard-Jones potential (also needed for Newton-Raphson method):
def pot_secder(r):
    res = 4*eps*(156*sigma**12/r**14 - 42*sigma**6/r**8) #second derivative of potential function
    return res #returns the value of the second potential derivative at the given "r"

#Implementation of Newton-Raphson method to determine the minima of Lennard-Jones function:
r0 = 0.33 #initial guess for "r", which should be chosen wisely, because otherwise NR method just fails to find the true value, try r = 100 for instance.
tol = 0.001 #tolerance value 0f 0.01 is preferred because decreasing the tol value even more improves the result just by less that 1%
nsteps = 0 #counter

#printing the initial value of "r" input:
print("The initial r guess:", r0,"nm")

#Lists where V(r), F(r) and "r" values will be stored for plotting:
pot_list = []
r_list = []
Force = []

while abs(pot_der(r0)) > tol:
    r0 = r0 - pot_der(r0)/pot_secder(r0)
    nsteps += 1

#The following while basically loops through particular "r" values, finds the corresponding V(r) and F(r) and appends everything to appropriate lists.
r = 3.3 #Initial guess, also has to be chosen carefully as V(r) skyrockets for small "r".
while r < 10:
    pot_list.append(pot(r)) #appending V(r) to list with potentials
    Force.append(-pot_der(r)) #appending F(r) to list with forces
    r_list.append(r) #appending "r" to list with "r's"
    r += 0.001 #step interval


#Printing the value of "r" for which function is minimum and number of steps it took the program to execute:
print("The function minimum was found to be at the following value of r:", r0,"nm")
print("The minimum was found in", nsteps, "steps.")

#Plotting V(r) vs. r:
plt.plot(r_list, pot_list, color='r')
plt.xlabel("r,nm")
plt.ylabel("V(r)")
plt.title("V(r) vs. r")
plt.scatter(r0, pot(r0), s = 12, color='b') #point characterizing the equilibrium properties of the molecule
plt.legend(['V(r)','Minima'])
plt.show()

#Plotting F(r) vs. r:
plt.plot(r_list, Force, color='b')
plt.xlabel("r,nm")
plt.ylabel("F(r)")
plt.title("F(r) vs. r")
plt.scatter(r0, -pot_der(r0), s = 12, color = 'r') #point characterizing the equilibrium properties of the molecule
plt.legend(['F(r)',"Minima"])
plt.show()
