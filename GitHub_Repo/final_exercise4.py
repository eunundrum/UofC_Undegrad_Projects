#Exercise 4: Fourier Transform analysis. Given data file with data points for time and amplitude is used as an input.
import numpy as np 
import matplotlib.pyplot as plt 

#Loading data file:
data = np.loadtxt('superposition_signal.txt', float)

#Extracting data points for time (sec) and amplitude (arb.units) from given data file:
time = []
ampl = []

for i in data:
    time.append(i[0])  #Each element in the first column is time, that's why it should be indexed as "0"
    ampl.append(i[1])  #Each element in the second column is amplitude => indexed as "1"

#Defyining the signal function (not really necessary, but I compared results at the end of the program
# by subtituting experimentally obtained frequencies into this function just to make sure that obtained
#  frequencies fit into given data from the input file):
def sig(v1,v2,v3,t):
    return (1/3)*(np.cos(2*np.pi*v1*t) + np.cos(2*np.pi*v2*t) + np.cos(2*np.pi*v3*t))  #returns amplitude of the signal at some time for specific frequencies 

#frequency spectrum (chosen carefully, otherwise not all frequency components might be visible):
f = np.linspace(0,1, len(time))

#Applying "np.fft.fft" on given amplitude data set to obtain frequencies
#distribution over the frequency spectrum of the signal.
fourier = np.fft.fft(ampl)

#Now we need to obtain a power spectrum, i.e. we need to take absolute value of each frequency 
#in the spectrum and represent only positive part of each frequency over the frequency spectrum.
power = np.abs(fourier)

#Extracting number of frequency component, n, corresponding to the particular frequency amplitude
#in the power spectrum. Needs to be multiplied by the number of elements in the given array of data (len(time)),
#in order to account for (number of elements)/cycle. Otherwise, the final frequencies will be different.
fr = np.fft.fftfreq(len(ampl))*len(time)

#Choosing frequencies corresponding to prominent amplitudes on the power spectrum only from the
# positive side, f>0, because negative frequencies are just mirrored true
# frequencies (refer to the "figure 1" being plotted):
print("The f1 frequency is:",110,"Hz")
print("The f2 frequency is:",220,"Hz")
print("The f3 frequency is:",440,"Hz")



#Finally, it is time to plot frequency (positive part, aka power spectrum) distribution and
#corresponding signal amplitudes over chosen frequency spectrum.
plt.plot(fr, power, color='b')
plt.title("Figure 1: Power spectrum of the signal")
plt.xlabel("Frequency,Hz")
plt.ylabel("Amplitude, arb.units")
plt.show()

#Plotting the model signal with frequencies obtained through application of fourier transform
#superimposed with the original data from the input file just to compare how accurately I was able to
# determine frequencies, not part of the assignment. Presented just for clarification).
plt.plot(f, sig(110,220,440,f), color='b')
plt.plot(time,ampl,color='r')
plt.title("Figure 1: Amplitude vs. time")
plt.legend(['experimental','original'])
plt.xlabel("timeline,sec")
plt.ylabel("Amplitude, arb.units")
plt.show()