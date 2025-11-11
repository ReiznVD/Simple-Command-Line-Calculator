import os, sys, time


# Function to handle Printing logic
def msg(value):
    print("Result : ", value)

# Function to do Addition
def add(x , y):
    summ = x + y
    msg(summ)
    return summ

# Function to do Subtraction
def sub(x , y):
    subs = x - y
    msg(subs)
    return subs 

# Function to do Multiplication
def multi(x , y):
    mult = x * y
    msg(mult)
    return mult

# Function to do Division
def div(x , y):
    divs = x / y
    msg(divs)
    return divs

# Function to get input to do repeating of mathematical operation
def ask_repeat():
    while True:
        repeat = input("Again? (Y/N) : ").strip().lower()
        if repeat in ["y", 'n']:
            return repeat
        else :
            print("Your input is invalid, Please enter either the letter y or n. ")

#Function to clear the screen
def clear_screen():
    os.system ('cls' if os.name == 'nt' else 'clear')

# Function to ensure only number can be inputted to mathematical operation
def sure_number(prompt):
    while True:
        try:
            userinput = input(prompt).strip()
            value = float(userinput)
            if value.is_integer():
                return int(value)
            return value
        except ValueError:
            print("Invalid input, please enter a number")

# Outer Loop
while True :
    clear_screen()
    print("------------------ Menu ------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print ("============================================")

    try:
        choose = int(input("Menu Number only : "))
    except ValueError:
        print("Invalid input, please enter numbers only")
        input("Press Enter to continue ....")
        continue

    if choose == 5:
        print("Goodbye")
        sys.exit(0)

    elif choose in [1, 2, 3, 4]:
        # Inner Loop
        while True: 
            clear_screen()
            print ("============================================")
            a = sure_number("First Number : ")
            b = sure_number("Second Number : ")
            print()
            print ("============================================")
            if choose == 1 :    
                result = add(a,b)
            elif choose == 2 :
                result = sub(a,b)
            elif choose == 3 :
                result = multi(a,b)
            elif choose == 4 :
                try :
                    result = div(a,b)
                except ZeroDivisionError:
                    print("Division by Zero is not possible")
                    
            
            repeat = ask_repeat()
            if repeat == "y":
                time.sleep(1)
                continue
            elif repeat == "n":
                break

    else :
        print("No such option available.")
        input("Press Enter to continue ....")
        continue

    


