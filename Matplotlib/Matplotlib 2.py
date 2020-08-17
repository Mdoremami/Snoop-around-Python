import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np


x = np.arange(0,10)
y1 = np.sort(np.random.randint(0,15,(10)))
y2 = np.sort(np.random.randint(0,15,(10)))


# plt.figure('Simple Bar')
# print(plt.style.available)
# plt.style.use('ggplot')

# # Bar plots...
# width = 0.25
# # These additions and subtractions are just a method for better display
# plt.bar(x-width,y1 , label = 'First output' ,  color = 'b' , width = width)
# plt.bar(x+width,y2 , label = 'Second output' , color = 'r' , width = width)
# # we could simultineously plot linear data as well
# plt.plot(x,y1 , label = 'First output' ,  color = 'g')
# plt.plot(x,y2 , label = 'Second output' , color = 'y')


# # Consider you want to write sth for each of your x... 
# plt.xticks(ticks = x , labels = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight' , 'nine' , 'ten'])
# # Same trick for y :)
# ytick = np.arange(0,15)
# ylabel = np.arange(60,75)

# plt.title('Test Number 1')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()
# plt.grid(True)

# #Saving the plot. Must be done before plt.show()
# plt.savefig('hi.png')
# plt.show()


# Now, horizental bar
# useful for counting sth
y1 = [0,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,0,1]
y2 = [0,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,0]
x = np.arange(len(y1))


plt.figure('Horizental Bar')
plt.style.use('ggplot')

height = 0.1
width = 0.3
plt.subplot(211)
plt.barh(y1 , label = 'First output' ,  color = 'b' , height = height,width = width)
plt.ylabel('Y')
plt.subplot(212)
plt.barh(y2 , label = 'Second output' , color = 'r' , height = height ,width = width)
plt.xlabel('X')
plt.ylabel('Y')

plt.suptitle('Test Number 1')
# plt.legend(loc = 'lower right')
plt.grid(True)
plt.savefig('hi.png')
plt.show()