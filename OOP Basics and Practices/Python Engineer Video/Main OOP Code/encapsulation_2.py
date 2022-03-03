# here we are going to look at encapsulation for methods, a private function




class Software_Engineer:

	def __init__(self, name, age):
		self.name = name
		self.age = age
		self._salary = None
		self._num_of_bugs_solved = 0

	def code(self):
		# this shows there is no need to show the variable from the outside, we dont care how many bugs they have solved only other methods might depend on it
		self._num_of_bugs_solved += 1

	def get_salary(self):
		return self._salary


	def set_salary(self, base_salary):
		# here we can see that the base salary depends on a another function and the encapsulation part is where we cannot  see the number of bugs that instance solved
			self._salary = self._calculate_salary(base_salary)
	# lets create a method so that the salary depends on the number of bugs solved
	# again to show it is a private method we put a leading underscore
	# this method has no need to be called from the outside


	def _calculate_salary(self, base_salary):
		if self._num_of_bugs_solved < 10:
			return base_salary
		if self._num_of_bugs_solved <100:
			return base_salary * 2
		
		return base_salary * 3

 




se1 = Software_Engineer("Sanjeev Giritharan", 15)
# here we loop it so that the number of bugs solved becomes 70 times
for i in range(70):
	se1.code()
print(se1._num_of_bugs_solved)
# here we pass the salary, then it goes to a private method where the salary depends on the number of bugs solved 
se1.set_salary(6000)
# becuase it is 70 times in the method we see that our base salary will double as it is not less than 10 and not greater than 100
print(se1.get_salary())



