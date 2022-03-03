# polymorphism is where an variable, method or an object can take multiple forms

class Human:
	pass


class Husband(Human):
	pass

class Employee(Human):
	pass



# this means an object of Employee is also an human but it can also be a Husband, it can take multiple forms

# you can implement Polymorphism with 4 ways: Duck Typing, Operator Overloading, Method Overloading, Method Overriding