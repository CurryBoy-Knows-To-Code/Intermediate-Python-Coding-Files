
class A:
	# now when creating a instance of class a you must pass in the name and age and gender but nothing else
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender
	
	def feature_1(self):
		print("Feature 1")

	def feature_2(self):
		print("Feature 2")



class B(A):
	# now if you want class B to have the same instance attributes of class A and some on its own then you use the super keyword
	# now in the __init_- method you type in every inherited instance attribute you want and then the unique instance attributes

	def __init__(self, name, age, pay):
		# this is how you inherit the instance attributes name and age but not gender
		# this means when creating a object of class B you must pass the name, age and the pay of that object
		super().__init__(name, age)
		self.pay = pay

	def feature_3(self):
		print("Feature 3")

	def feature_4(self):
		print("Feature 4")