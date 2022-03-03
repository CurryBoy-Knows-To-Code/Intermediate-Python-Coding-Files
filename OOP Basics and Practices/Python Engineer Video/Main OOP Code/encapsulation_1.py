# here we are going to look at encapsulation for attributes



# Encapsulation is the mechanism of hiding ways of implementing data
# this means that  instance variables are kept private and there is only 1 accessor method from the outside which can access or change thse instance variables
# we do this by getters and setters which are public methods

# instance methods can also be private so that it can only be used internally and not from the outside


class Software_Engineer:
	# lets make it so that the salary, address and number of bugs solved is private, which means that no can see this
	def __init__(self, name, age):
		self.name = name
		self.age = age
		# now we are going to create 2 internal attribute
		# by convention we use 1 underscore at the start to show it is private
		self._salary = None
		self._num_of_bugs_solved = 0

	# lets create 2 methods where one can access the private instance variable salary and the other one to set the salary 
	# this function is a getter 
	def get_salary(self):
		return self._salary
	# and this one is a setter
	def set_salary(self, value):
		# lets enforce some constraints
		if value < 1000:
			self._salary = 1000
		elif value > 20000:
			self._salary = 20000
		else:
			self._salary = value



# lets create a instance for this class
se1 = Software_Engineer("Sanjeev Giritharan", 15)
# we can still print out the private attributes
print(se1._num_of_bugs_solved)

# now lets set the salary for our instance, which means you will be able to modify it from the outside
se1.set_salary(38987)
# lets print the salary with the set salary function
print(se1.get_salary())






