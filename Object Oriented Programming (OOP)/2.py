#########################################
# 		Object Oriented Programming		#
# 			Mahdi DorEmami				#
#			 	Part II					#
#########################################

import random

class subcompany:
	def __init__(self, name , emplyee_num , budget , max_employees):
		self.Name = name
		self.empnum = emplyee_num
		self.Max_employees = max_employees
		self.budget = budget
		# we can have attributes without asking them from the user initially
		self.Employees = []
	
	def get_employee_number(self):
		return self.empnum

	def add_employee(self , employee):
		if len(self.Employees) < self.Max_employees:
			self.Employees.append(employee)
			employee.assign_company(self.Name)
			self.empnum += 1
			return True
		return False

	def get_avg_age(self):
		age = 0
		for emp in self.Employees:
			age += emp.get_age()
		return age / len(self.Employees)
	def get_avg_sal(self):
		sal = 0
		for emp in self.Employees:
			sal += emp.get_salary()
		return sal / len(self.Employees)

class emplyee:
	def __init__(self, fname , lname , age , field , salary):
		self.Fname = fname
		self.Lname = lname
		self.Age = age
		self.Field = field
		self.Salary = salary
		self.Subcompany = ''
	def get_salary(self):
		return self.Salary

	def get_age(self):
		return self.Age

	def assign_company(self , subcompanyname):
		self.Subcompany = subcompanyname
	def email_creator(self):
		return self.Fname+'.'+self.Lname+'@'+self.Subcompany.Name+'.org'


Cola = subcompany('Cola' , 0 , 1000000 , 3)
Pepsi = subcompany('Pepsi' , 0 , 3000000 , 5)

e1 = emplyee('Mahdi' , 'DorEmami' , 23 , 'Electrical Engineering' , 20000)
e2 = emplyee('Mehran' , 'DorEmami' , 16 , 'Arts' , 10000)
e3 = emplyee('Alireza' , 'GoleSorkhi' , 17 , 'Medical Science' , 15000)
e4 = emplyee('Peter' , 'Morphin' , 27 , 'Data Scientist' , 35000)
e5 = emplyee('Sarah' , 'Surpop' , 22 , 'Manager' , 50000)
e6 = emplyee('Forru' , 'Morphin' , 57 , 'Janitor' , 5000)
e7 = emplyee('Jack' , 'Ramonds' , 30 , 'Buffet' , 13000)
e8 = emplyee('Paul' , 'Corpenter' , 67 , 'Advertiser' , 13000)
e9 = emplyee('Repo' , 'Matid' , 32 , 'Janitor' , 5000)

Employee_List = [e1,e2,e3,e4,e5,e6,e7,e8,e9]

print(f'Cola Number of Employees: {Cola.get_employee_number()}')
print(f'Pepsi Number of Employees: {Pepsi.get_employee_number()}')

for i in range(9):
	if i<4:
		Cola.add_employee(Employee_List[i])
	else:
		Pepsi.add_employee(Employee_List[i])

print(f'Cola Number of Employees: {Cola.get_employee_number()}')
print(f'Pepsi Number of Employees: {Pepsi.get_employee_number()}')


print(f'Employee 1 subcompany: {e1.Subcompany}')
print(f'Employee 2 subcompany: {e2.Subcompany}')
print(f'Employee 3 subcompany: {e3.Subcompany}')
print(f'Employee 4 subcompany: {e4.Subcompany}')
print(f'Employee 5 subcompany: {e5.Subcompany}')
print(f'Employee 6 subcompany: {e6.Subcompany}')
print(f'Employee 7 subcompany: {e7.Subcompany}')
print(f'Employee 8 subcompany: {e8.Subcompany}')
print(f'Employee 9 subcompany: {e9.Subcompany}')

print(f'Average Age of Cola: {Cola.get_avg_age()}')
print(f'Average Age of Pepsi: {Pepsi.get_avg_age()}')
print(f'Average Salary of Cola: {Cola.get_avg_sal()}')
print(f'Average Salary of Pepsi: {Pepsi.get_avg_sal()}')



