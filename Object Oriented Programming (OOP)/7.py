#########################################
# 		Object Oriented Programming		#
# 			Mahdi DorEmami				#
#			 	Part VII				#
#########################################

import numpy as np

# Decorators in OOP

# Imagine, we forgot to have id_number as one of the attributes, and we already signed thousands of people into the system with
# this class. We want to generate random ids but the function is having multiple lines and can't do it all for all individuals
# seperately... What we do is to define a new method in the parent or a child class, and turn the 'method' into 'attribute' by 
# '@ property' decorator and 'setter' method.

# That's what we want to do for each person
# x = np.arange(111,999)
# y = np.arange(11,99)
# xprime = np.random.permutation(x)
# yprime = np.random.permutation(y)
# z = []
# for i in range(len(x)):
# 	for j in range(len(y)):
# 		z.append(str(xprime[i]) + '-' + str(yprime[j]))
# print(z)
# p1.id_number = z[0]
# p2.id_number = z[1]
# etc...

# So we do like this (commented area is the solution for the problem, so let them be comments to see the main class and
# uncomment them to solve the problem)


class id:

	# x = np.arange(111,999)
	# y = np.arange(11,99)
	# xprime = np.random.permutation(x)
	# yprime = np.random.permutation(y)
	# z = []
	# for i in range(len(x)):
	# 	for j in range(len(y)):
	# 		z.append(str(xprime[i]) + '-' + str(yprime[j]))

	def __init__(self , FULLNAME , AGE , COUNTRY):
		self.fullname = FULLNAME
		self.age = AGE
		self.country = COUNTRY

	def id_presentor(self):
		return f'{self.fullname} is {self.age} years old and is originally from {self.country}'

	# @ property
	# def id_NUM(self):
	# 	return '{}'.format(self.id_number)

	# @ id_NUM.setter
	# def id_num_set(self , person_number):
	# 	self.id_number = id.z[person_number]


p1 = id('Matt_Still' , 29 , 'United States')

# p1.id_num_set = 2

# print(p1.id_number)




