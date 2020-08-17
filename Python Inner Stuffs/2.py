#########################################
# 		Object Oriented Programming		#
# 			Mahdi DorEmami				#
#			 	Part VII				#
#########################################

# Decorators

# Decorators are just functions that change other functions. So, we don't need to write all the code again within a function 
# and we can borrow the features of the decorating function (the one indicated by @)
# One way using nested functions
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print(decorate)
print(decorate())

# The other way using decorators
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi)
print(say_hi())


# Another example

def adder_decorator(function):
	def adder(a,b):
		return a+b

	return adder

@ adder_decorator
def subtractor(a,b):
	return a-b

# We decorated (changed) the function 'subtractor' with 'adder_decorator'
print(subtractor(4,5))

