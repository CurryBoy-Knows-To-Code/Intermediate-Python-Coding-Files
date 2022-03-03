# now we are going to see how we can overide and extend our classes
# by extending our classes i mean by writing unique methods specific to that class

class Employee:
	def __init__(self, first_name, last_name, age, email, phone_number, salary):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.email = email
		self.phone_number = phone_number
		self.salary = salary


	def what_emp_do(self):
		print("{} is working ...".format(self.first_name))





# these 2 classes can also have their own methods
class Software_Engineer(Employee):
	# now are going to create our own init method for this class which will get the same instance attributes before as well as the salary and level

	def __init__(self, first_name, last_name, age, email, phone_number, level, salary):
		# we refer to the parent class instance attributes by using the keyword super()
		# inside the brackets you put the instance attributes you already put, so for this one you would put: first_name, last_name, age, email, phone_number, salary
		# with this you can have classes with differnt instance attributes to make each class unique
		super().__init__(first_name, last_name, age, email, phone_number, salary)
		self.level = level

	# lets write a unique method specific to software engineers
	def debugging(self):
		print("{} is debugging some code".format(self.first_name)) 
	



class Designer(Employee):
	# now lets create a instance attributes that are from the employee class but with also a uniques one so that it is different to the software engineer classmethod
	def __init__(self, first_name, last_name, age, email, phone_number, experience, salary):
		super().__init__(first_name, last_name, age, email, phone_number, salary)
		self.num_years_experience = experience
	# here we are creating a method uniques to the designer class
	def drawing(self):
		print("{} is drawing some plans".format(self.first_name))

	

# in total you need to enter 8 arguements excluding self to create a instance of the software_engineer class
se1 = Software_Engineer("Sanjeev","Giritharan","15","sanju2506g@gmail.com","8220819435","lead",27000)
se1.debugging()
# now in this instance we also pass 8 arguements, a instancee created in the Designer class doesnt have the instance atribute level
de1 = Designer("Bob","Crachit","15","Bobloves69@outlook.com","14256734590","10 years",5000)
de1.drawing()


# Polymorphism gives us a way to use a class like its parent class but still each child class has its own method
# Recap:
# how does inheritence works and how we can overide and extend our classes
# how and why is the super keyword used 
# what is polymorphism