def my_var():
	base_string = "%s has a type %s"
	
	var = 42
	print(base_string%(var, type(var)))
	
	var = '42'
	print(base_string%(var, type(var)))

	var = 'quarante-deux'
	print(base_string%(var, type(var)))
	
	var = 42.0
	print(base_string%(var, type(var)))
	
	var = True
	print(base_string%(var, type(var)))
	
	var = [42]
	print(base_string%(var, type(var)))

	var = {42 : 42}
	print(base_string%(var, type(var)))

	var = (42,)
	print(base_string%(var, type(var)))

	var = set()
	print(base_string%(var, type(var)))

if __name__ == '__main__':
	my_var()