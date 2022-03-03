# here we look about class atributes and how are they used
class Software_Engineer:
	# here we have created a class atribute and it not unique to each instance of this class
	# it is the same for each instance even if you change it 
	alias = "Keyboard Warriors"
	def __init__(self, name, age, level, salary):

		self.name = name
		self.age = age
		self.level = level
		self.salary = salary


se1 = Software_Engineer("Sanjeev",15,"lead developer",27000)
print(se1.name,se1.age)

# we can print our class attribute in 2 ways
print(se1.alias)# --> the class atribute is part of each instance, its like a common instance attribute to each instance
print(Software_Engineer.alias)

# we are going to create a new instance called 'se2'
se2 = Software_Engineer("Joe",28,"junior",7000)
# here we can see the the uniques instance attributes of the 2 instances but they have a common class atribute
print(se2.name,se2.age)
print(se2.alias)
print(Software_Engineer.alias)

# Recap
# How to create a class and what it is
# How to create a instance and what it is
# How to define instance attributes 
# How to use class attributes and how are they differnet to instance methods
