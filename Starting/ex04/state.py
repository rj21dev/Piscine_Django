import sys

def search_by_value(value, dictio):
	for key, val in dictio.items():
		if val == value:
			return key
	return None

def find_state(capital):
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
	code = search_by_value(capital, capital_cities)
	if not code:
		print('Unknown capital city')
		return
	print(search_by_value(code, states))

def process():
	if len(sys.argv) == 2:
		find_state(sys.argv[1])

if __name__ == '__main__':
	process()