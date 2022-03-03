# classes are used for more complex data structures and they contain functions that describes the behaviour of our class
# a class is basically a blueprint of our data structure


# we use the keyword class to create a class then its class name
# here we have created a class called 'Software_Engineer'
class Software_Engineer:
	# here we are going to use a special method called the __init__():   --> initialise our object's Attributes
	# as the first arguements it is always 'self' which pass the instances name,after that we can pass as many arguements
	def __init__(self, name, age, level, salary):
		# to  initialise it you do self.variable = corresponding arguement
		# these are the instance attributes specific to our instance
		self.name = name
		self.age = age
		self.level = level
		self.salary = salary
		




# this is our instance 'se1' --> Software_Engineer1
se1 = Software_Engineer("Sanjeev",15,"lead developer",27000)

# you can access cetain instance attributes
print(se1.name,se1.age)