import numpy as np
from matplotlib import pyplot as plt

fc = 10**6 #frequencia da portadora
fm = 10**4 #frequencia da moduladora

ac = 1 #amplitude da portadora
am = 1 #amplitude da moduladora

k = 1 #fator de sensibilidade

def portadora(t):
    return ac * np.cos(2 * np.pi * fc * t)

def moduladora(t):
    return am * np.cos(2 * np.pi * fm * t)

def forma_padrao(t):
    return (1 + k * moduladora(t)) * portadora(t)

t = np.linspace(-100, 100, 2000)

plt.plot(t, portadora(t), color='red')
plt.show()
