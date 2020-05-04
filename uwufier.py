import sys

def uwufy(string):
	return f"OwO {string.replace('r','w')} >w<"

if not len(sys.argv) == 1:
	print(uwufy(sys.argv[1]))
else:
	print("UwU ewwow: you didn't entew a stwing")
