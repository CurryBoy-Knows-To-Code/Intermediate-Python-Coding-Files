# a class is a design for a object, which means it is like a blueprint  
# object == instance
# classes are allow us to create our own "data type" with its own behaviors 
# lets create a computer class and object
# class names must be in cammel case format 
# use the keyword class to create one 
class Computer:
	# indentation under the class is where all the stuff  belongs to that specific class
	# where in this class you define the attributes(instance or class) and methods(functions)
	# we define our attributes using the __init__ method, this is a dunder method shown by the leading and trailing underscores
	# it initialises the instance attributes
	# the self arguement always takes in the instance but after the self you can pass as many attributes you want
	
	def __init__(self, cpu, ram_cap, storage_cap):
		# this is how we set up our instance attributes
		self.cpu = cpu
		self.ram_cap = ram_cap
		self.storage_cap = storage_cap
	
	# lets create a method which shows all the attributes
	def config(self):
		print(f"CPU = {self.cpu}, RAM CAPACITY = {self.ram_cap}, STORAGE CAPACITY = {self.storage_cap}")



# now to create a instance you give it a name then the objects class name(pass attributes here)
comp1 = Computer("i5", "16Gb", "1Tb")
# we can access our attributes using object.attribute
print(comp1.cpu)
# to call a method you do instance.methodName()
comp1.config()
# this means objects will hab=ve its own methods and variables