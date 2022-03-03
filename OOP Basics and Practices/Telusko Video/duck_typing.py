class Pycharm:
	def execute(self):
		print("Compiling...")
		print("Running...")


# lets have another IDE class Jupiter
class Jupiter:
	def execute(self):
		print("Debuging...")
		print("Compiling...")
		print("Running...")
		
	pass


class Laptop:
	# no matter  what IDE we pass we always call the execute method, this means calling the execute method either calls the Pycharm or Jupiter method
	def code(self, IDE):
		IDE.execute()




# lets create an laptop object 
lap1 = Laptop()
# here we have to pass an IDE which will then run and call the method in class Pycharm
# to do this we need to create a object of class Pycharm 
ide  = Pycharm()
# this method will call the method of Pycharm as that is the IDE  we pass
lap1.code(ide)
print()
# here we changed the IDE to Jupiter
ide = Jupiter()
# so now this method will call the method of Jupiter as that is the new IDE we pass
lap1.code(ide)
