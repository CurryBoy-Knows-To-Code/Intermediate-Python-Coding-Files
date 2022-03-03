# we can have inner classes as well

class Student:
	def __init__(self, name, year):
		self.name = name
		self.year = year
		self.laptop = self.StudentLaptop()

	# method to show student details
	def info(self):
		print(f"Name = {self.name}, year = {self.year}")

	# lets just say every student has a laptop and each student laptop had its own methods and attributes
	# create a innerclass
	class StudentLaptop:

		company_name = "DELL"

		def __init__(self):
			self.cpu = "i5"
			self.ram_cap = "16GB"
			self.storage_cap = "1TB"
		
		# lets create another method to show info of the laptops, this also has the same method name as the outer class
		def info(self):
			print(f"company_name = {self.company_name}, CPU = {self.cpu}, ram_capacity = {self.ram_cap}, storage_capacity = {self.storage_cap}")


# lets create 2 objects
s1 = Student("sanj",69)
s2 = Student("Shin",25)
# to access the inner class attributes
print(s1.laptop.cpu)
# outer class info method
s1.info()
# inner class info method
s1.laptop.info()