# here we will be looking about class decorators
# class decorators do the same thing as function decorators but are typically used to maintain and update a state
# here we are going to use classes and decorators to keep count how many times we execute the 'say_hello()' function
class Count_Calls:
	def __init__(self,function_that_we_pass):
		self.function_that_we_pass = function_that_we_pass
		self.number_of_times_function_has_been_called = 0
	# the call method allows you too execute a object of this class just like a function
	def __call__(self,*args,**kwargs):
		# each time the function is called it is incremented by 1 
		self.number_of_times_function_has_been_called += 1
		# here print the amount of times it has beeen called
		print(self.number_of_times_function_has_been_called)
		# here we call the function again
		return self.function_that_we_pass(*args,**kwargs)






cc = Count_Calls(None)
# as we have used the call method we can put brackets for our object to work like a filter
# calling this object will execute the call method which print out hello there!!!
# here we put our class decorator
@Count_Calls
def say_something():
	print("Mario says ching chong")
say_something()

