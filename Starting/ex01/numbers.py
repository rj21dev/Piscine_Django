if __name__ == '__main__':
	with open("numbers.txt", 'r') as file:
		for line in file:
			line = line[:-1]
			elems = line.split(',')
		for elem in elems:
			print(elem)