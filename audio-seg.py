from  __future__ import division
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.signal
from scipy import signal

from IPython.display import Audio

filename = '1.wav'

fs, wave = scipy.io.wavfile.read(filename)
#Note that this particular file has a single channel. Most audio files will have two (stereo) channels.

print ('Data:', wave)
print ('Sampling rate:', fs)
print ('Audio length:', wave.size)
print ('Audio length:', wave.size/fs, 'seconds')
print ('Lowest amplitude:', wave.min())
print ('Highest amplitude:',wave.max())

seconds = wave.size/fs
milsec = seconds * 1000


asec = wave.size/seconds

part = []
scipy.io.wavfile.write("1-p.wav",fs,wave[0:int(round(asec))])

tenmilisec = int(round(asec/10))
scipy.io.wavfile.write("1-p.wav",fs,wave[0:tenmilisec])
scipy.io.wavfile.write("2-p.wav",fs,wave[tenmilisec:(tenmilisec*2)])
scipy.io.wavfile.write("3-p.wav",fs,wave[(tenmilisec*2):(tenmilisec*3)])
scipy.io.wavfile.write("4-p.wav",fs,wave[(tenmilisec*3):(tenmilisec*4)])
scipy.io.wavfile.write("5-p.wav",fs,wave[(tenmilisec*4):(tenmilisec*5)])
scipy.io.wavfile.write("6-p.wav",fs,wave[(tenmilisec*5):(tenmilisec*6)])
scipy.io.wavfile.write("7-p.wav",fs,wave[(tenmilisec*6):(tenmilisec*7)])
scipy.io.wavfile.write("9-p.wav",fs,wave[(tenmilisec*7):(tenmilisec*8)])
scipy.io.wavfile.write("8-p.wav",fs,wave[(tenmilisec*8):(tenmilisec*9)])





#
# a = wave[:,0]
# spec = plt.specgram(a, NFFT=int(fs*0.005), Fs=fs, cmap=plt.cm.gray_r, pad_to=256, noverlap=int(fs*0.0025))

# plt.show()

