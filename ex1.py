import numpy as np
from matplotlib import pyplot as plt

fc = 10**6 #frequencia da portadora
fm = 10**4 #frequencia da moduladora

ac = 10 #amplitude da portadora
am = 1 #amplitude da moduladora

k = 0.6 #fator de sensibilidade

def vetor_tempos(f, ciclos):
    fs = 2 * 10 * f             # freq. de amostragem
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

fft_vals = np.fft.fft(sinal_am(t))

freqs = np.fft.fftfreq(len(t))
freqs *= 2*10**7
limit = 1.1*10**6
mask = (freqs > -limit) == (freqs < limit)


plt.subplot(4, 1, 1)
plt.plot(t, portadora(t), 'r')
plt.ylabel('Amplitude')
plt.xlabel('Portadora')

plt.subplot(4, 1, 2)
plt.plot(t, moduladora(t), 'g')
plt.ylabel('Amplitude')
plt.xlabel('Moduladora')

plt.subplot(4, 1, 3)
plt.plot(t, sinal_am(t), 'b')
plt.ylabel('Amplitude')
plt.xlabel('Sinal AM')

plt.subplot(4, 1, 4)
plt.plot()
plt.plot(freqs[mask], fft_vals[mask], 'b')
plt.ylabel('Amplitude')
plt.xlabel('Sinal AM')

plt.subplots_adjust(hspace=1)
plt.show()
