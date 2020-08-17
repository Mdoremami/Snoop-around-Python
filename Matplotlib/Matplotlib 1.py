import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np

###


x = np.arange(0,10)
y1 = np.sort(np.random.randint(0,15,(10)))
y2 = np.sort(np.random.randint(0,15,(10)))


# prints all available styles
print(plt.style.available)
# You can use any styles you actually like.
plt.style.use('ggplot')
# There's also a funny style as well... You can use this with different 'plt.style's as well.
plt.xkcd()


# Labels are good for legending... without them, you should write
# each plot's label in the legend like :
# plt.legend(['First output' , 'Second	output'])
plt.plot(x,y1 , label = 'First output' , marker = 'D' , color = 'blue', linestyle = '--' , linewidth = 4) 
plt.plot(x,y2 , label = 'Second output' , marker ='*' , color = 'r' , linestyle = ':' , linewidth = 2)
# Linestyles{':' , '-.' , '--' , '-'}
# Colors : 'b(blue' , 'g(green)' , 'r(red)' , 'c(cian)' , 'm(magenta)' , 'y(yellow)' , 'k(black)' , 'w(white)'
# You can do #nnnnnn hex code instead of a color where first two 'n's are hex value for red, then green, then blue.
# markers : '_','|','o','p','D','d','+','>','<','^','v',',','.','1','2','3','4','s','h','H','x'
plt.title('Test Number 1')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

#Saving the plot. Must be done before plt.show()
plt.savefig('hi.png')

plt.show()



