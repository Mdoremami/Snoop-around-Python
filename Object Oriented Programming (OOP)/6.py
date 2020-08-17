#########################################
# 		Object Oriented Programming		#
# 			Mahdi DorEmami				#
#			 	Part VI					#
#########################################

# These double underscore methods like __init__ are called magic functions that are inside python.
# We can change them for our classes.

# Consider __repr__ magic function that it will return the location of the object

class worker:
	base_salary = 10000

	def __init__(self , name , age , salary):
		self.name = name
		self.age = age
		self.salary = salary
		# This will not work
		# bomber = 5
	def salary_comparae(self):
		if self.salary >= worker.base_salary:
			print(f'This worker receives {self.salary} $ as payment and it\'s {self.salary - worker.base_salary} $ more than base salary')
		else:
			print(f'This worker receives {self.salary} $ as payment and it\'s {worker.base_salary - self.salary} $ less than base salary')

w1 = worker('Andy' , 20 , 10500)


class worker2(worker):
	def __init__(self , name , age , salary):
		super().__init__(name , age , salary)

	def __repr__(self):
		return '{} , {} years old with {} $ as salary'.format(self.name , self.age , self.salary)

	def __len__(self):
		return 200

w2 = worker2('Tom' , 14 , 8500)

# We changed the magic function in our worker2 class... Fantastic.
print(repr(w1))
print(repr(w2))

# Also, we can do more... like magic functions __add__ or __len__
print('hi'.__len__())
print(len('hi'))

print(len(w1.name))
print(w1.name.__len__())

print(len(w2.name))
print(w2.name.__len__())

# You must be asking what the fuck... it didn't work... But that's not it... These magic function alterations, only work
# on objects themselves not the attributes
# So, below, len(w1) gives an error but:
print(len(w2))
print(w2.__len__())

# and they have got a lot of properties that it might not be easy to deal with... For example, this len magic function, must
# return an integer back not any other types...
