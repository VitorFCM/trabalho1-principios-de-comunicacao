import numpy as np
from matplotlib import pyplot as plt

fc = 10**6 #frequencia da portadora
fm = 10**4 #frequencia da moduladora

ac = 10 #amplitude da portadora
am = 1 #amplitude da moduladora

k = 0.6 #fator de sensibilidade

def portadora(t):
    return ac * np.cos(2 * np.pi * fc * t)

def moduladora(t):
    return am * np.cos(2 * np.pi * fm * t)

def sinal_am(t):
    return (1 + k * moduladora(t)) * portadora(t)

t = np.linspace(0, 0.001, 10 ** 7)


plt.subplot(3, 1, 1)
plt.plot(portadora(t), 'r')
plt.ylabel('Amplitude')
plt.xlabel('Portadora')
plt.xlim(0, 0.001)

plt.subplot(3, 1, 2)
plt.plot(moduladora(t), 'g')
plt.ylabel('Amplitude')
plt.xlabel('Moduladora')
plt.xlim(0, 0.001)

plt.subplot(3, 1, 3)
plt.plot(sinal_am(t), 'b')
plt.ylabel('Amplitude')
plt.xlabel('Sinal AM')
plt.xlim(0, 0.001)

# plt.plot(t, portadora(t), color='red')
plt.subplots_adjust(hspace=1)
plt.show()
