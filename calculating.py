# Calculating with Functions
lst = []


def zero(*args):
	global lst
	lst.insert(0, 0)
	return result()


def one(*args): 
	global lst
	lst.insert(0, 1)
	return result()


def two(*args):
	global lst 
	lst.insert(0, 2)
	return result()


def three(*args): 
	global lst
	lst.insert(0, 3)
	return result()


def four(*args): 
	global lst
	lst.insert(0, 4)
	return result()


def five(*args): 
	global lst
	lst.insert(0, 5)
	return result()


def six(*args): 
	global lst
	lst.insert(0, 6)
	return result()


def seven(*args):
	global lst 
	lst.insert(0, 7)
	return result()


def eight(*args): 
	global lst
	lst.insert(0, 8)
	return result()


def nine(*args): 
	global lst
	lst.insert(0, 9)
	return result()


def plus(*args): 
	global lst
	lst.insert(0, "+")
	return result()


def minus(*args): 
	global lst
	lst.insert(0, "-")
	return result()


def times(*args):
	global lst 
	lst.insert(0, "*")
	return result()


def divided_by(*args):
	global lst 
	lst.insert(0, "//")
	return result()


def result():
	global lst
	if len(lst) == 3:
		if lst[1] == "+":
			res = lst[0] + lst[2]
			lst = []
			return res
		elif lst[1] == "-":
			res = lst[0] - lst[2]
			lst = []
			return res
		elif lst[1] == "*":
			res = lst[0] * lst[2]
			lst = []
			return res
		else:
			res = lst[0] // lst[2]
			lst = []
			return res