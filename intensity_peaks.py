from pylab import *
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import wave
import numpy as np

file = "BlownAwayDraft07a.wav"

# OPEN FILE #
spf = wave.open(file,'r')
f = spf.getframerate()
original_sound = spf.readframes(-1)
original_sound = fromstring(original_sound, 'Int16')

# FFT CALCULATION #
t_window = .3
t_overlap = .011
num_samples_per_window = f * t_window
num_samples_per_overlap = f * t_overlap

spectrogram = []
last_idx = 0

end_loop = False

while not end_loop:
    #if we are towards the end of input file only take the number of samples that are left
    num_samples =  len( original_sound ) - 1 - last_idx 
    
    if num_samples < num_samples_per_window:
        num_samples_per_window = num_samples
        end_loop = True

    #take snapshot of signal in time bin 
    sound_info = original_sound[ last_idx:last_idx + num_samples_per_window ]
    
    # CALCULATE FFT FOR WINDOW #
    window = np.hanning( len(sound_info ) ) 
    sound_window = []
    for s, w in zip( sound_info, window ):
       sound_window.append( s * w )

    ft_w = fft( sound_window )
    ft_wm = map( abs, ft_w ) #take magnitude

    #plot FFT for signal in given time window
    x = np.arange(0, f/2, f/len(ft_wm) )
    ft_half = ft_wm[: len(ft_wm)/2]

    plt.plot( x, ft_half)
    plt.show()
    
    #save fft for given time bin (this will be a spectogram)
    spectrogram.append( ft_half) 
    last_idx = last_idx + num_samples_per_window - num_samples_per_overlap
    
        
spec_peaks = []

for freq_array in spectrogram : 
    spec_peaks.append( max( freq_array ) )


'''
window = np.hanning( len(sound_info ) ) 
sound_window = []
for s, w in zip( sound_info, window ):
   sound_window.append( s * w )

ft_w = fft( sound_window )
ft_wm = map( abs, ft_w )

x = np.arange(0, f/2, f/len(ft_wm) )
ft_half = ft_wm[: len(ft_wm)/2]
plt.plot( x, ft_half)
plt.show()
'''

