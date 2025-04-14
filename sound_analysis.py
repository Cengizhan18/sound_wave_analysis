# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 22:28:05 2025

@author: kahra
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Dosya yolu
file_path = r"C:\Users\kahra\Desktop\125hz.wav"

# WAV dosyasını oku
fs, data = wavfile.read(file_path)

# Stereo ise tek kanalı al (sol kanal)
if len(data.shape) == 2:
    data = data[:, 0]

# Zaman vektörü oluştur
time = np.linspace(0, len(data) / fs, num=len(data))

# Plot
plt.figure(figsize=(12, 4))
plt.plot(time, data, linewidth=1)
plt.title("125 Hz Sound Wave (.wav)")
plt.xlabel("Time (second)")
plt.ylabel("Amplitude")

# 1 ms aralıklarla grid
plt.xticks(np.arange(0, time[-1], 0.005))
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.xlim(0, 0.05)  

plt.show()
