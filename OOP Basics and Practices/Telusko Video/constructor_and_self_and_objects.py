class Computer:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# lets create a method that updates the age
	def update_age(self, new_age):
		self.age = new_age



# lets create an object
comp1 = Computer("Sanjeev", 15)
# when creating this object, it has its own memory location and address in a special memory called heap memory, the size of the object depends on the number of attributes it has
# this prints out the memory address of comp1, and when re-running the program you get a new memory space allocated
print(id(comp1))
# lets print the age of our comp1 object
print(comp1.age)
comp1.update_age(26)
print(comp1.age)
# here when we call the method update age we change the age to age we pass(26), also when calling the method we are actually passing 2 arguemts which is the instance to self and the age to new_age