import time

def main():
    num = input("How many numbers would you like to get? ")
    while not num.isdigit():
        num = input("What? ")
        
    sleep = input('''Would you like that the program will sleep 
    for a while after drawing each number? [y, n] ''')
    while sleep.lower() != "y" and sleep.lower() != "n":
        sleep = input("What? ")
    
    
    for i in range(1, int(num) + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        if (sleep.lower() == "y"):
            time.sleep(0.5)

main()