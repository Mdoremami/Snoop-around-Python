import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np

# Stack Charts

# Consider comparing 4 students' studying hours in one month
# It shows everyone's range and volatality very well
Days = np.arange(30)
student1 = [5,6,5,4,3,5,6,7,5,4,10,5,6,9,8,7,5,6,5,4,5,5,5,5,5,4,5,6,4,5]
student2 = [10,10,9,7,4,8,4,4,1,2,3,6,4,7,3,2,1,5,1,1,0.5,0.5,2,2,1,3,4,2,1,0]
student3 = [1,2,1,2,3,1,2,5,4,4,5,4,5,6,6,6,6,6,3,2,5,1,5,5,7,8,8,8,8,8,]
student4 = [5,5,5,5,5,5,6,6,6,4,4,4,5,6,6,6,6,6,6,4,4,4,4,4,4,4,6,4,6,4]
labels = ['student1' , 'student2' , 'student3' , 'student4']
plt.stackplot(Days,student1,student2,student3,student4 , labels = labels)
plt.legend()
plt.show()