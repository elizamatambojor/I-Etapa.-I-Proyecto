#!/usr/bin/env python
# coding: utf-8

# # Gráficas de Piano 

# In[1]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("piano-G3.wav")
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


# In[1]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("piano-C4.wav")
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


# In[2]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("piano-G4.wav")
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


# In[3]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("piano-C5.wav")
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


# In[4]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("piano-G5.wav")
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


# In[5]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("piano-C6.wav")
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


# In[47]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("piano-G6.wav")
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


# # Gráficas de Flauta 

# In[49]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("flute-C4.wav")
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


# In[23]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("flute-G4.wav")
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


# In[24]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("flute-C5.wav")
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


# In[25]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("flute-G5.wav")
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


# In[26]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("flute-C6.wav")
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


# In[27]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("flute-G6.wav")
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


# # Gráficas de Trompeta 

# In[28]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("trumpet-G3.wav")
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


# In[29]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("trumpet-C4.wav")
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


# In[30]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("trumpet-G4.wav")
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


# In[31]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("trumpet-C5.wav")
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


# In[32]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("trumpet-G5.wav")
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


# In[33]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("trumpet-C6.wav")
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


# # Gráficas de Violín 

# In[46]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys

raw = wave.open("violin-C4.wav")
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


# In[35]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("violin-G4.wav")
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


# In[45]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("violin-C5.wav")
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


# In[37]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("violin-G5.wav")
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


# In[43]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("violin-C6.wav")
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


# In[42]:


# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
raw = wave.open("violin-G6.wav")
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




