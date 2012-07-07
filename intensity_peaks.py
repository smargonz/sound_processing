from pylab import *
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import wave
import numpy as np
import os

for files in os.listdir("."):
    if files.endswith(".wav")
        song = files
        song_name_split = song.split(".")
        song_name_file = song_name_split[0] + ".wav"

        # OPEN FILE #
        spf = wave.open(song_name_file,'r')
        f = float( spf.getframerate() )
        original_sound = spf.readframes(-1)
        original_sound = fromstring(original_sound, 'Int16')

        # FFT CALCULATION #
        t_window = .3
        t_overlap = .011
        num_samples_per_window = ceil(f * t_window)
        num_samples_per_overlap = ceil(f * t_overlap)

        spectrogram = []
        last_idx = 0
        i=0
        end_loop = False

        while not end_loop:
            #print i
            #i=i+1
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
            ft_half = ft_wm[: len(ft_wm)/2]
            x = np.arange(0, f/2, f/(len(ft_half)*2) )

            #plt.plot( x, ft_half)
            #plt.show()
            
            #save fft for given time bin (this will be a spectogram)
            spectrogram.append( ft_half) 
            last_idx = ceil(last_idx + num_samples_per_window - num_samples_per_overlap)
                
    spec_peaks = []

    f = open( song_name_split[0] + ".txt",'w')

    # find highest peaks in song 
    for freq_array in spectrogram : 
        max_peak = max( freq_array )
        spec_peaks.append( max_peak )
        
    f.write( str(spec_peaks) )  


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

