# here we are going to learn about other special methods mainley: __eq__ and __str__


class Software_Engineer:
	alias = "Keyboard Warriors"
	def __init__(self, name, age, level, salary):
		self.name = name
		self.age = age
		self.level = level
		self.salary = salary


	def what_is_dev_doing(self):
		print("{} is writing code while listening to intense music".format(self.name))

	# we use the dunder method __str__ which is called whenever our object/instance is typed as a string
	# in this one we are gonna show the instance attributes, we pass the self arguement
	def __str__(self):
		return "Name = {}, Age = {}, Level = {}, Salary = {}".format(self.name,self.age,self.level,self.salary)
	
	# now we are going to use the __eq__ which is the equal dunder method which is used to compare instances/objects
	def __eq__(self,other):
		# now if the condition is true then it returns true else it returns false
		return self.name == other.name and self.age == other.age



	


se1 = Software_Engineer("Sanjeev",15,"lead developer",27000)
se2 = Software_Engineer("Joe",28,"junior",7000)
# lets create a instance with the same instance attributes as se1
se3 = Software_Engineer("Sanjeev",15,"lead developer",27000)
# now if we simply print the object name it will run the str dunder method
print(se1)
print(se2)
# here we are comparing the 2 objects as we are basically calling the __eq__ function
print(se1 == se3)

# Recap:
# how are functions created within classes and how they can be used
# the 2 main dunder methods  __str__, __eq__
