#########################################
# 		Object Oriented Programming		#
# 			Mahdi DorEmami				#
#			 	Part I					#
#########################################

# So, some basic components first. we have a class, and we have object instances of the class.
# In below, classy0 and 'classy1' are 'classes', and 'd' is a class object instance which is like a clone of a class with all
# the attributes and methods (data and functions respectively) of the class.

class classy1:
	# You can define only methods in the class
	# Every method must have the argument called self (Actually, it doesn't matter what you name it... You can name
	# it anything else :) but 'self', is just an unwritten standard between programmers)
	def bomber(self):
		print('bomber')

	def adder(self, x, y):
		return x+y
# See that it works to name sth different than self.
class classy0:
	def bomber(fooxer):
		print('bomber')

	def adder(fooxer, x, y):
		return x+y

d = classy0()
d.bomber()
print(d.adder(2,3))
# running d.adder(2,3) is like running classy0(d,2,3) --> So that 'self' in methods is actually the instance object we are 
# passing in
print(classy0.adder(d,2,3))
print(d.adder('abs' , 'tract'))






# You can create a method with attributes (data) to store as well.. Like this below adder
# Now, special __init__ method, has a few features. 1) It doesn't return anything, so it returns None... But
# printing function and other sorts of functions work inside it.
# 2) It will require its inputs to be passed at the first moment you want to create an object of the class
class classy2:
	# The only special features of __init__ are that it initially wants atts and doesn't return an output
	def __init__(self , fname , lname):
		self.First_Name = fname
		self.Last_Name = lname
		print(fname+lname)

	def adder(self , x, y):
		self.xer = x
		self.yer = y
		return x+y

	def get_atts(self):
		return self.First_Name , self.Last_Name , self.xer , self.yer

	# We can also change the attributes of different methods in new methods
	def name_edit(self , first , last):
		self.First_Name = first
		self.Last_Name = last

	def adder_edit(self , xnew , ynew):
		self.xer = xnew
		self.yer = ynew

d = classy2('Mahdi' , 'DorEmami')
print('1)', d.First_Name , '\n')
print('2)', d.Last_Name , '\n')
print('3)', d.adder(3,5) , '\n')
print('4)', d.xer , d.yer , '\n')
print('5)', d.get_atts() , '\n')
print('6)', type(d) , '\n')
print('7)', dir(d) , '\n')
d.name_edit('Bob' , 'Ross')
d.adder_edit(8,9)
print('8)', d.First_Name , '\n')
print('9)', d.Last_Name , '\n')
print('10)', d.xer , d.yer , '\n')


