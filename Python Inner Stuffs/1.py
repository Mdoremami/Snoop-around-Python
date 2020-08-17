#########################################
# 		Object Oriented Programming		#
# 			Mahdi DorEmami				#
#			 	Part VII				#
#########################################


# Cute function properties
def func(*args,**kwargs):
    return 5

a = func(54,214,'wql;jd')
print(a)

def func2(*args,**kwargs):
    return args , kwargs

b = func2('system',5,'b',2 , b='s')
print(b)