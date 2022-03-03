# here we will be learning about function decorators
# a decorator is a function that takes a another function as a arguement and it extends the behavior of this function without modifying it explicitly
# it adds functionality to an existing function
# a decorator has a leading @ symbol

# this decorator function takes a function as a arguement 
def start_end_decorator(the_func_that_we_pass):
	# a function in side a function is known as a wrapper function
	# here when running the add function we get an error where the wrapper function was given 2 arguements which was num1 and num2, to avoid this you put a '*args', '**kwargs', where you can put as many number of arguements and key word arguements
	def wrapper(*args,**kwargs):
		print("start")
		# here we execute the function which we passed 
		# here also you put the args and kwargs as we still have to pass the arguemts num1 and num2
		# here we have to store the result or print it out 
		# we dont put a return here because using the return keyword will stop the function executing
		result = the_func_that_we_pass(*args,**kwargs)
		print("end")
		return result
	# then we return the wrapper function
	return wrapper

# here we have put the functions name as the decorator, this will extend the functionality of the 'print_name()' function with the 'start_end_decorator()' function
@start_end_decorator
#def print_name():
	#print("Hi my name, my name is, my name is Lana Rhoades")
# instead lets put a function which has a arguement
def add_function(num1, num2):
	return num1 + num2



print(add_function(10,5))