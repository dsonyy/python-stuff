import random

def game():
    lower = 1
    higher = 1000
    count = 1
    key = random.randrange(1,1000)
    print("\nI thought about the number that:")
    print(" - is higher than " + str(lower))
    print(" - is lower than  " + str(higher))
    c = input("What's that number? ") 
    while int(c) != key:
        if (c.isdigit()):
            if (int(c) > key):
                if (int(c) < higher):
                    higher = int(c)
            elif (int(c) < key):
                if (int(c) > lower):
                    lower = int(c)
        count = count + 1
        c = input(str(lower) + " < ??? < " + str(higher) + ": ") 
    print("YES! That was " + str(c) + ". It took you " + str(count) + " attemps!")


def main():
    while True:        
        print("           ___________________________________________         ")
        print("  ________|        _       _  _       _         _  _  |_______ ")
        print("  \       | |_| | |   |_| |_ |_|  |  | | | | | |_ |_| |      / ")
        print("   \      | | | | |_| | | |_ | \  |_ |_| |_|_| |_ | \ |     /  ")
        print("   /      |___________________________________________|     \  ")
        print("  /__________)                                     (_________\ ")

        print("                 _______________________________         ")
        print("        ________|                               |_______ ")
        print("        \       |        -- Main Menu --        |      / ")
        print("         \      |                               |     /  ")
        print("          \     |  1. Play                      |    /   ")
        print("          /     |  2. Exit                      |    \   ")
        print("         /      |_______________________________|     \  ")
        print("        /__________)                         (_________\ ")
        c = ""
        c = input("\nType the number of option to select: ")
        while c != '1' and c != '2':
            c = input("What? ")
        if c == '2':
            return
        if c == '1':
            game()
        
main()