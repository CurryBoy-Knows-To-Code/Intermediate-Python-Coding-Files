import random

# in OOP you got instance, class and static methods
# instance methods takes in the instance as the first arguements 
# class methods take in the class name as the first arguement 
# static methods dont take in any 'special' arguement it is like a normal function

class Student:
	# class varibale
	# btw these are randomly generated location and contact number
	school = "North Leamington School"
	location = "PH2 9RN"
	contact_number = "+1 202-918-2132"
	
	def __init__(self, mark1, mark2, mark3):
		self.m1 = mark1
		self.m2 = mark2
		self.m3 = mark3

	# lets create a method to find average mark of student, this is also an instance method
	def avg(self):
		return round((self.m1 + self.m2 + self.m3)/3,2)

	# this is a getter method and by convention you have the get in the method name
	def get_m1(self):
		return self.m1

	# this is a setter by convention it has set in the method name
	def set_m1(self, new_mark):
		self.m1 = new_mark

	# this a method that shows class variables, this is a class method and by convention we use 'cls' as the first arguemt
	# to make the method a class method we use the @classmethod decorator
	@classmethod
	def school_info(cls):
		print(f"SCHOOL NAME = {cls.school}, SCHOOL LOCATION = {cls.location}, CONTACT NUMBER = {cls.contact_number}")

	# this method is a staticmethod, where it will generate a random centre number
	# this will not take any class or instance variables
	@staticmethod
	def get_centre_number():
		return str(random.randint(1,9999))




s1 = Student(45, 85, 73)
s2 = Student(76, 34, 67)
# these 2 lines below print the average mark of each object
print(s1.avg())
print(s2.avg())
# we pass the class name when calling the class method
Student.school_info()
print(s1.get_centre_number())