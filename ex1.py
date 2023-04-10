import numpy as np
from matplotlib import pyplot as plt

fc = 10**6 #frequencia da portadora
fm = 10**4 #frequencia da moduladora

ac = 10 #amplitude da portadora
am = 1 #amplitude da moduladora

k = 0.6 #fator de sensibilidade

def vetor_tempos(f, ciclos):
    fs = 2 * 10 * f             # freq. de amostragem
    N = int(round(ciclos * (fs / f)))
    t_f = ciclos * (1 / f)
    A = int(t_f * fs)           # nro de amostras
    return np.linspace(0, t_f, A)

def portadora(t):
    return ac * np.cos(2 * np.pi * fc * t)

def moduladora(t):
    return am * np.cos(2 * np.pi * fm * t)

def sinal_am(t):
    return (1 + k * moduladora(t)) * portadora(t)

t = vetor_tempos(fc, 200)

plt.subplot(3, 1, 1)
plt.plot(portadora(t), 'r')
plt.ylabel('Amplitude')
plt.xlabel('Portadora')
#plt.xlim(0, xlim)

plt.subplot(3, 1, 2)
plt.plot(moduladora(t), 'g')
plt.ylabel('Amplitude')
plt.xlabel('Moduladora')
#plt.xlim(0, xlim)

plt.subplot(3, 1, 3)
plt.plot(sinal_am(t), 'b')
plt.ylabel('Amplitude')
plt.xlabel('Sinal AM')
#plt.xlim(0, xlim)

# plt.plot(t, portadora(t), color='red')
plt.subplots_adjust(hspace=1)
plt.show()
