import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np

# Pie Charts

slices = {'Python' : 100 , 'Java' : 50 , 'C++' : 85 , 'c' : 120}

print(slices.values())

plt.pie(slices.values() , labels = slices.keys() , autopct = '%.4f' ,
 wedgeprops = {'edgecolor' : 'w'} , shadow = True) #wedgeprops are for edge settings...
plt.show()											# Shadow, makes it 3D
plt.pie(slices.values() , labels = slices.keys() , autopct = '%.4f' ,
 wedgeprops = {'edgecolor' : 'w'} , startangle = 90)# You can set a starting angle as well
plt.show()
# We can do quite a few things, we can emphasize on sth for example!!
# explode method will do it for us, the value 0 means no change and values between 0 and 1 show the level of change
exploded = [0.2,0,0,0]
plt.pie(slices.values() , labels = slices.keys() , autopct = '%.4f' , wedgeprops = {'edgecolor' : 'w'} , explode = exploded) 
plt.show()

