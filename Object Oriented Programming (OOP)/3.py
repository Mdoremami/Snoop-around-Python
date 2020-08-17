#########################################
# 		Object Oriented Programming		#
# 			Mahdi DorEmami				#
#			 	Part III					#
#########################################

# Inheretence : Cloning a parent class into different children classes each containing all the same attributes and methods
# 				of the parent class, plus the ability for each child to overwrite or add more methods and attributes
#				of their own


class Fruit:
	def __init__(self , Name , Taste):
		self.name = Name
		self.taste = Taste

	def show(self):
		print(f'{self.name} has got some sort of {self.taste} flavor')

# We have to specify the parent class in paranthesis
class apple(Fruit):
	def is_healthy(self):
		print('I don''t know')
	# Changed this method of the parent in this child
	def show(self):
		print('Changed :(')

class orange(Fruit):
	def is_jucy(self):
		print('Yep 100 %')
	def show(self):
		print('Changed :)')

class watermelone(Fruit):
	pass

Kiwi = Fruit('Kiwi' , 'Sore')
a1 = apple('Red_Apple' , 'Sore')
a2 = apple('Yellow_Apple' , 'Sweet') 
o = orange('Orange' , 'Sweet')
Kiwi.show()
a1.show()
a2.show()
o.show()
a1.is_healthy()
a2.is_healthy()
o.is_jucy()

Water_Melone = watermelone('Water_Melone' , 'Extra Sweet')
Water_Melone.show()