import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd
#Format above appropriatly
from scipy.fft import fft





#1 C
#Number of
K = 20
Sampindexes = np.arange(0, K, 1)
sampfreq = 1/128

x1 = np.cos(42*np.pi*Sampindexes*sampfreq)
x2 = np.cos(44*np.pi*Sampindexes*sampfreq)


#Plot the sampled signals x1 and x2

#Do as above but using ax instead
fig, ax = plt.subplots()
ax.stem(x1, label='21 Hz',markerfmt='ro', linefmt='r', basefmt='r')
ax.set_xticks(np.arange(0, 20, 1))
#Do above but set marker color to red
ax.stem(x2, label='22 Hz', markerfmt='bo', linefmt='b', basefmt='b')
ax.legend()
plt.show()


#2 a
L = K
X1 = fft(x1)
X2 = fft(x2)
#X1 = fft(x1, n=256)
#X2 = fft(x2, n = 256)

fl = np.arange(0,int(L/2))/L * 128
X1new = []
X2new = []
for x in range(0,int(L/2)):
#for x in range(0,int(256/2)):
    X1new.append(abs(X1[x])*1/K) 
    X2new.append(abs(X2[x])*1/K) 
#Plot the frequency domain signals X1f and X2f
fig, ax = plt.subplots()


#plt.plot(fl, abs(X1), label='42pi')
ax.stem(fl, X1new, label='21 Hz',markerfmt='ro', linefmt='r', basefmt='r')
#plt.plot(fl, abs(X2), label='44pi')
ax.stem(fl, X2new, label='22 Hz', markerfmt='bo', linefmt='b', basefmt='b')
plt.legend()
plt.show()

#2 b 
X1 = fft(x1, n=256)
X2 = fft(x2, n = 256)
X1new = []
X2new = []
for x in range(0,int(256/2)):
    X1new.append(abs(X1[x])*1/K) 
    X2new.append(abs(X2[x])*1/K) 
fig, ax = plt.subplots()


fl = np.arange(0,int(256/2))/256 * 128
#plt.plot(fl, abs(X1), label='42pi')
ax.stem(fl, X1new, label='21 Hz',markerfmt='ro', linefmt='r', basefmt='r')
#plt.plot(fl, abs(X2), label='44pi')
ax.stem(fl, X2new, label='22 Hz', markerfmt='bo', linefmt='b', basefmt='b')
plt.title("Zero Padded")
plt.legend()
plt.show()

#3 a

x3 = np.sin(42*np.pi*Sampindexes*sampfreq)+np.sin(44*np.pi*Sampindexes*sampfreq)
X3_unpadded = fft(x3)
X3_padded = fft(x3, n = 256)

X3unpadded = []
X3padded = []
for x in range(0,int(L/2)):
    X3unpadded.append(abs(X3_unpadded[x])*1/K) 
for x in range(0,int(256/2)):
    X3padded.append(abs(X3_padded[x])*1/K) 
#Length unpadded is

funpadded = np.arange(0,int(L/2))/L * 128
fpadded = np.arange(0,int(256/2))/256 * 128
#Plot the frequency domain signals X1f and X2f
fig, ax = plt.subplots()
ax.stem(funpadded, X3unpadded, label='X3unpadded',markerfmt='ro', linefmt='r', basefmt='r')
ax.stem(fpadded, X3padded, label='X3padded', markerfmt='bo', linefmt='b', basefmt='b')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()


#3 b
#Solution to getting a better resolution is to increase the number of samples

#Generate new sampindexies with 2x as many samples
K = 88
Sampindexes = np.arange(0, K, 1)
x3 = np.sin(42*np.pi*Sampindexes*sampfreq)+np.sin(44*np.pi*Sampindexes*sampfreq)

X3_improved_padded = fft(x3, n = 256)
X3_new = []
for x in range(0,int(256/2)):
    X3_new.append(abs(X3_improved_padded[x])*1/K)

fpadded = np.arange(0,int(256/2))/256 * 128
fig, ax = plt.subplots()
ax.stem(fpadded, X3_new, label='X3_new', markerfmt='bo', linefmt='b', basefmt='b')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
