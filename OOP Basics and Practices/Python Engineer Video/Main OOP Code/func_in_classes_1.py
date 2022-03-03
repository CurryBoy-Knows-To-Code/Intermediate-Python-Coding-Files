# here we are going to create a function inside our class which are also known as methods



class Software_Engineer:
	alias = "Keyboard Warriors"
	  
	def __init__(self, name, age, level, salary):
		self.name = name
		self.age = age
		self.level = level
		self.salary = salary

	# we are going to create a method to say that our developer is wrting some code
	# we are passing the self arguement because each instance name is specific, also we can put as many arguements after that
	def what_is_dev_doing(self):
		# we put self.name because it makes sense
		print("{} is writing code while listening to intense music".format(self.name))


se1 = Software_Engineer("Sanjeev",15,"lead developer",27000)
se2 = Software_Engineer("Joe",28,"junior",7000)

# we call our method,though it seems we are not passing anything we are passing are instance just like the init method
# also for methods like this you must put the brackets at the end to run them
se1.what_is_dev_doing()
se2.what_is_dev_doing()