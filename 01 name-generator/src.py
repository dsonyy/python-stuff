import sys
import string
fprefix_path = "./prefix.txt"
def name_to_prefix( str ):
	randrange(0,10)
	return


print("\n              *   *   *              \n")
print("Welcome to the amazest name generator\n")

try:
	fprefix = open(fprefix_path, "r")
except:
	print("There are no" + fprefix_path + "file. Exitting.")
	sys.exit()

name = input("Please type your first name: ")
while not name.isalpha():
	name = input("I don't think that's your real first name.\nType the real one: ")
	
city = input("OK, now please write the name of the city where you were born: ")

bonus = input("Good. Now think about any random name and type it here: ")

	
fprefix.close();