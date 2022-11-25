def print_numbers(filename):
	with open(filename, 'r') as file:
		for line in file:
			line = line[:-1]
			elems = line.split(',')
		for elem in elems:
			print(elem)


if __name__ == '__main__':
	print_numbers("numbers.txt")