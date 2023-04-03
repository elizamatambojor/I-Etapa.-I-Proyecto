#!/usr/bin/env python
# coding: utf-8

# #  Suma de audios 

# In[12]:


import pydub 
from pydub import AudioSegment
audio1 = AudioSegment.from_wav(r"piano-G6.wav")
audio2 = AudioSegment.from_wav(r"piano-G5.wav")
output = audio2.overlay(audio1,position = 0)
output.export(r"output.wav", format="wav") 


# # Resultado de la suma de audios 

# In[14]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("output.wav")
signal = raw.readframes(-1)
signal = np.frombuffer(signal, dtype ="int16")
f_rate = raw.getframerate()
time = np.linspace(
	0, # start
	len(signal) / f_rate,
	num = len(signal)
)
plt.figure(1)
plt.title("Sound Wave")
plt.xlabel("Time")
plt.plot(time, signal)
plt.show()


# In[ ]:




