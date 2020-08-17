from collections import Counter

Lister = ['python' , 'java' , 'c++']

c = Counter(Lister)

print(c)

# We can update the counter as well

c.update(['python' , 'c#' , 'c' , 'c++' , 'python' , 'Assembly' , 'Assembly' , 'c#' , 'c#' , 'python'])

print(c)

# Gives the #number most commons
print(c.most_common(2))

pp = [1,3,4,6]
pp.reverse()
print(pp)