import random

 # the frequencies of specified vowels and consonants are different
vowels = ("aaeeeiioouy")
consonants = ("bccddfghhjkllmmnnnpqrrsstttvwxz")

def get_vowel():
	return random.choice(vowels)
	
def get_consonant():
	return random.choice(consonants)

def get_word(segments):
	way = random.randrange(2)
	string = ""
	for _ in range(segments):
		if way == 0:
			string += get_vowel() + get_consonant()
		elif way == 1:
			string += get_consonant() + get_vowel()
	return string
	
def main():
	num = input("How many names would you like to generate? ")
	if not num.isdigit():
		num = input("Hey! I'm expecting a positive number. ")
	if not num.isdigit():
		num = input("Do you understand? ")
	if not num.isdigit():
		num = input("Oh god, what are you doing? Just type a positive N-U-M-B-E-R! ")
	if not num.isdigit():
		num = input("You have got one last try!!! ")
	if not num.isdigit():
		print("NOW I TYPE THE NUMBER INSTEAD OF YOU. MUHAHAHA ")
		input();
		num = 1000000
	
	for _ in range(int(num)):
		name = get_word(random.randrange(2,5)).title() + " "
		
		if 	random.randrange(7) == 0:
			name += get_word(1) + " "
	
		name += get_word(random.randrange(1,6)).title()
		
		print(name)
	
main()
