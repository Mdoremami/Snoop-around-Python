#########################################
# 		Object Oriented Programming		#
# 			Mahdi DorEmami				#
#			 	Part V					#
#########################################

# We can have static attributes that are called 'class attributes' which is like a global variable.

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
w2 = worker('Tom' , 14 , 8500)

# See that base_salary is unique for the class
# You can change it in different methods though...
w1.salary_comparae()
w2.salary_comparae()
w1.base_salary = 40000
print(worker.base_salary)
print(w1.base_salary)
print(w2.base_salary)
worker.base_salary = 80000
print(worker.base_salary)
print(w1.base_salary)
print(w2.base_salary)

# See that these two don't work
# print(w1.bomber)
# print(w2.bomber)

# Now, about class methods; We can have class methods as well.

class worker2:
	base_salary = 10000

	def __init__(self , name , age , salary):
		self.name = name
		self.age = age
		self.salary = salary
		# If you pass this to classmethod, it wouldn't work
		self.baby = 5
		# This will not work
		# bomber = 5
		print(f'The base salary is {worker2.show()} for all the workers')
	# Without this decorator, we can use it by self.show(); Meaning it's dependant to the object instance 
	# But with this decorator, we can use it like worker2.show() which is independant to the object and it's dependant to the 
	# class
	# It's easier to use it anywhere by typing worker2.show(), meaning we don't need to remember instances like w1 or w2, and we
	# can generally call these classmethods by the class name itself.
	# Also, it doesn't work with attributes inside another method. Only atts in itself or classattributes
	@classmethod
	def show(cls):
		# cls.baby = 5
		return cls.base_salary


	def salary_comparae(self):
		if self.salary >= worker2.base_salary:
			print(f'This worker receives {self.salary} $ as payment and it\'s {self.salary - worker2.base_salary} $ more than base salary')
		else:
			print(f'This worker receives {self.salary} $ as payment and it\'s {worker2.base_salary - self.salary} $ less than base salary')
		

w1 = worker2('Andy' , 20 , 10500)
w2 = worker2('Tom' , 14 , 8500)
w1.salary_comparae()
w2.salary_comparae()



# More onto classmethod:
class A(object):
    def foo(self, x):
        print ("executing foo(%s, %s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print ("executing class_foo(%s, %s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print ("executing static_foo(%s)" % x)   

a = A()

# Below is the usual way an object instance calls a method. The object instance, a, is implicitly passed as the first argument.
a.foo(1)
# With classmethods, the class of the object instance is implicitly passed as the first argument instead of self.
a.class_foo(1)

# You can also call class_foo using the class. In fact, if you define something to be a classmethod, 
# it is probably because you intend to call it from the class rather than from a class instance. 
# A.foo(1) would have raised a TypeError, but A.class_foo(1) works just fine:
A.class_foo(1)

# With staticmethods, neither self (the object instance) nor cls (the class) is implicitly passed as the first argument.
# They behave like plain functions except that you can call them from an instance or the class:
a.static_foo(1)
A.static_foo('hi')
# Staticmethods are used to group functions which have some logical connection with a class to the class.




### A more general explanation

# @staticmethod function is nothing more than a function defined inside a class.
# It is callable without instantiating the class first. It’s definition is immutable via inheritance.

# @classmethod function also callable without instantiating the class, but its definition follows Sub class, 
# not Parent class, via inheritance. That’s because the first argument for @classmethod function must always be cls (class).