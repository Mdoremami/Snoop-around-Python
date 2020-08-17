import matplotlib.pyplot as plt
import numpy as np
import os
from itertools import count
from matplotlib.animation import FuncAnimation
from pandas import read_csv
path = 'E:\\My Projects\\2019 Works\\Python\\Sublime\\Matplotlib'
os.chdir(path)


# Subplots
# We could have passed a tupple like (ax1,ax2) instead of ax since ax now is a list of two plt.plots
fig , ax = plt.subplots(nrows = 2 , ncols = 1)
x = np.arange(10)
y1 = [10,3,1,15,1,16,16,16,16,20]
y2 = [3,14,15,1,16,3,5,23,1,5]

ax[0].plot(x,y1 , color = 'blue')
ax[1].plot(x,y2 , color = 'red')
ax[0].set_title('Channel 1')
ax[0].set_xlabel('X')
ax[0].set_ylabel('Y')
ax[1].set_title('Channel 2')
ax[1].set_xlabel('X')
ax[1].set_ylabel('Y')
plt.tight_layout()
plt.show()

# You can avoid repeatitions... Like, one title with 'suptitle' , shared x with 'sharex=True'
fig , ax = plt.subplots(nrows = 2 , ncols = 1 , sharex= True)
plt.suptitle('Hi')
plt.xlabel('X')
ax[0].plot(x,y1 , color = 'blue')
ax[1].plot(x,y2 , color = 'red')
ax[0].set_ylabel('Channel 1')
ax[1].set_ylabel('Channel 2')
# plt.tight_layout() --> Doesn't work well with suptitle
plt.show()


# We can do it with seperated figs
fig1 , ax1 = plt.subplots()
fig2 , ax2 = plt.subplots()
plt.xlabel('X')
ax1.plot(x,y1 , color = 'blue')
ax2.plot(x,y2 , color = 'red')
ax1.set_title('Channel 1')
ax2.set_title('Channel 2')
ax1.set_ylabel('Y')
ax2.set_ylabel('Y')
plt.tight_layout()
plt.show()

