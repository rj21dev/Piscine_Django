import sys

def search_by_value(val: str, dictio: dict):
    for key, value in dictio.items():
        if value.lower() == val.lower():
            return key
    return None

def search_by_key(find_key: str, dictio: dict):
    for key, value in dictio.items():
        if key.lower() == find_key.lower():
            return value
    return None

def print_res(to_find: str):
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
    key = search_by_value(to_find, capital_cities)
    value = search_by_key(to_find, states)
    if key:
        print(f"{to_find} is the capital of {search_by_value(key, states)}")
    elif value:
        print(f"{search_by_key(value, capital_cities)} is capital of {to_find}")
    else:
        print(f"{to_find} is neither a capital city nor a state")

def parser():
    if len(sys.argv) != 2:
        return
    lst = sys.argv[1].split(',')
    for elem in lst:
        elem = elem.strip()
        if len(elem) == 0:
            continue
        print_res(elem)

if __name__ == '__main__':
    parser()