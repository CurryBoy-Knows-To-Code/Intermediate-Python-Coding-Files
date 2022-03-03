# in OOP's you actualy have 2 types of variables, class and instance variables/attributes
# a class variable is where the variable is shared and it is the same among all the objects of the same classmethod
# and instance variables are variables unique to that object 
class Vehicle:
	# this is a class attribute which means it is a common instance variable
	# most vehicles have 4 tyres
	num_tyres = 4

	def __init__(self, company, model, engine, vehicle_type, mileage):
		# these are the instance attributes that will be unique to that objects
		self.company = company
		self.engine = engine
		self.vehicle_type = vehicle_type  
		self.mileage = mileage




# lets create 3 objects
# this is car object
vehicle1 = Vehicle("Buggati", "Veyron", "W16", "supercar", 0)
# this is a bike object
vehicle2 = Vehicle("Suzuki", "Hayabusa","1299cc inline-four cylinder", "Bike", 69)
# this is a three-wheeler
vehicle3 = Vehicle("Reliant motor", "Reliant robbin", "848 cc OHV light alloy straight-4", "Three-Wheeler", 154) 