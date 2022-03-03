# inheritance is where a class takes in the methods and attributes of another class while having its own unique methods
# the inherited class is called the child class and class which was not inherited is the base/parent class


# this is the base class where a instance of this class can only access feature1 and feature2 methods
class A:
	def feature1(self):
		print("feature 1 method")

	def feature2(self):
		print("feature 2 method")

# this is a child class that inherits class A
# creating an instance of this class means that it will also have the methods of class A and class B
class B(A):
	def feature3(self):
		print("feature 3 method")

	def feature4(self):
		print("feature 4 method")

# this class is its own class with its own unique methods
class C:
	def feature8(self):
		print("feature 8 method")

	def feature9(self):
		print("feature 9 method")


# now lets create a class called D that inherits certain features such as feature 1,2,8,9
# this class inherits class A and class C and if more then do a comma after the current class inside the bracket
class D (A,C):
	pass


# object of class A
instA = A()
# this object can only access the methods of class A and not other classes, an object of class C will only be able to access feature 8 and 9
instA.feature1()
instA.feature2()

# this obj is of class B so it inherits the methods of class A and Class B
instB = B()
instB.feature1()
instB.feature2()
instB.feature3()
instB.feature4()

# this obj of class D can only access feature 1,2,8,9 and not the features of class B
instD = D()
instD.feature1()
instD.feature2()
instD.feature8()
instD.feature9()