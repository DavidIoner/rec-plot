from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from bin import searchfile
from scipy.fftpack import fft

file_name = searchfile.search_fname()

amostragem, dados = wavfile.read(file_name)
tamanho = dados.shape[0] / amostragem
tempo = np.linspace(0., tamanho, dados.shape[0])

largura = 20
altura = 10

plt.rcParams['figure.figsize'] = (largura, altura)
plt.plot(tempo, dados)
plt.magnitude_spectrum(dados, Fs=1/amostragem, scale='dB')
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude[dB]")
plt.show()

def f(filename):
    amostragem, data = wavfile.read(filename) # load the data
    a = data.T[0] # this is a two channel soundtrack, I get the first track
    b = [(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
    c = fft(b) # create a list of complex number
    d = len(c)/2  # you only need half of the fft list
    plt.plot(abs(c[:(d-1)]),'r')
    savefig(filename+'.png',bbox_inches='tight')