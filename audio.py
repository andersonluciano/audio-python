from  __future__ import division
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.signal
from IPython.display import Audio

filename = '1.wav'

fs, wave = scipy.io.wavfile.read(filename)
#Note that this particular file has a single channel. Most audio files will have two (stereo) channels.

print ('Data:', wave)
print ('Sampling rate:', fs)
print ('Audio length:', wave.size/fs, 'seconds')
print ('Lowest amplitude:', wave.min())
print ('Highest amplitude:',wave.max())


plt.plot(abs(wave[:,0]),'r')
plt.show()

a = wave[:,0]
spec = plt.specgram(a, NFFT=int(fs*0.005), Fs=fs, cmap=plt.cm.gray_r, pad_to=256, noverlap=int(fs*0.0025))
plt.show()



filename = '1-1.wav'

fs, wave = scipy.io.wavfile.read(filename)
#Note that this particular file has a single channel. Most audio files will have two (stereo) channels.

print ('Data:', wave)
print ('Sampling rate:', fs)
print ('Audio length:', wave.size/fs, 'seconds')
print ('Lowest amplitude:', wave.min())
print ('Highest amplitude:',wave.max())


a = wave[:,0]
spec = plt.specgram(a, NFFT=int(fs*0.005), Fs=fs, cmap=plt.cm.gray_r, pad_to=256, noverlap=int(fs*0.0025))
plt.show()