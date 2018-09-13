from  __future__ import division
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.signal
from scipy import signal

from IPython.display import Audio

filename = '2-p.wav'

fs, wave = scipy.io.wavfile.read(filename)
#Note that this particular file has a single channel. Most audio files will have two (stereo) channels.

print ('Data:', wave)
print ('Sampling rate:', fs)
print ('Audio length:', wave.size)
print ('Audio length:', wave.size/fs, 'seconds')
print ('Lowest amplitude:', wave.min())
print ('Highest amplitude:',wave.max())

print(wave)




#
# a = wave[:,0]
# spec = plt.specgram(a, NFFT=int(fs*0.005), Fs=fs, cmap=plt.cm.gray_r, pad_to=256, noverlap=int(fs*0.0025))

# plt.show()

