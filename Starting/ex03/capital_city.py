import sys

def find_capital(key):
	states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
	capital_cities = {
		"OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
	key = states.get(key)
	if not key:
		print('Unknown state')
		return
	print(capital_cities.get(key))

def process():
	if len(sys.argv) == 2:
		find_capital(sys.argv[1])

if __name__ == '__main__':
	process()