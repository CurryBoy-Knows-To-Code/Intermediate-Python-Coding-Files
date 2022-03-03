# now we are going to see how we can inherit our classes
# inheritance is when a class inherits the methods and attributes of a another class, this will make the class a child class and the inhereted class the base/parent class
# the emplopyee class wil be our parent class
class Employee:
	def __init__(self, first_name, last_name, age, email, phone_number):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.email = email
		self.phone_number = phone_number

	# lets create a method
	def what_emp_do(self):
		print("{} is working ...".format(self.first_name))




# these 2 classes below will inherit class employee making these 2 child classes
# this is done by classname(base/parent class):
class Software_Engineer(Employee):
	pass

class Designer(Employee):
	pass
 




# lets create a instance for our software_engineer class
# it works because this child class inherits the parent class 
# these 2 instances inherits the attributes of our base class
se1 = Software_Engineer("Sanjeev","Giritharan",15,"sanj@gmail.com",8220819435)
# we call the method for our se1
se1.what_emp_do()

de1 = Designer("Toby","marcina",28,"bot@yahoo.com",8820202002)
de1.what_emp_do()
