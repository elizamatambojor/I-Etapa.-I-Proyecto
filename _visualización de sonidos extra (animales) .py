#!/usr/bin/env python
# coding: utf-8

# # Sonido de León 

# In[1]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("León.wav")
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


# # Sonido de Grillos

# In[2]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("Grillos.wav")
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


# # Sonido de Caballo 

# In[3]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("Caballo.wav")
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




