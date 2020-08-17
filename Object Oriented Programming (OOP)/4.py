#########################################
# 		Object Oriented Programming		#
# 			Mahdi DorEmami				#
#			 	Part IV 				#
#########################################

# Inheretence : More Advanced One


class Fruit:
	def __init__(self , Name , Taste):
		self.name = Name
		self.taste = Taste

	def show(self):
		print(f'{self.name} has got some sort of {self.taste} flavor')

	def reformer(self,newname):
		self.oldname = self.name
		self.name = newname
		self.printer = f'{self.oldname} is reformed into {self.name}'
	
	def show(self):	
		print (self.printer)


# After specifying the parent class, let's say we want to pass the old initial attributes and a new one for this specific 
# child class. We will not copy and paste all those 'self.name' and 'self.taste' , etc.
# We will use super() which is like below:
# super() refers to (means) our parent class. The method in front of it is the method we want to pass its arguments
# automatically, so __init__ is the method we want to pass arguments; And we will declare the arguments inside it.
class apple(Fruit):
	def __init__(self , name , taste , color):
		super().__init__(name , taste)
		self.color = color
	
	def reformer(self , NEW_NAME , newcolor):
		super().reformer(NEW_NAME)
		self.oldcolor = self.color
		self.color = newcolor		
		self.printer = f'{self.oldname} with {self.oldcolor} color is reformed into {self.name} with {self.color} color'
	# No need for show as well... Sweet :)


a = apple('Apple','Sweet','Red')
a.reformer('Carrot' , 'Orange')
a2 = Fruit('Apple','Sweet')
a2.reformer('Carrot')

a.show()
a2.show()