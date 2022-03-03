# here we are going to look about properties, how they can be used with getters and setters
# using decorators is a more pythonic way of using getters and setters


class Software_Engineer:

	def __init__(self):
		self._salary = None
	
	# here you use a inbuilt decorator called property
	# so for our method you give it the name that we want, dont put the underscore
	@property
	def salary(self):
		return self._salary

	# here you give it the same name as the method you are going to use
	# then you type the@methods_name.setter
	@salary.setter
	def salary(self,value):
		self._salary = value
	



se1 = Software_Engineer()

# now using the decorators you can simply type
se1.salary = 6000
print(se1.salary)
