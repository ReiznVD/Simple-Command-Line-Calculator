# Project : 1 | A Simple command-line calculator built in Python.

<p align="justify">

A simple command-line calculator written in Python that capable of performing basic arithmetic operations such as addition, subtraction, multiplication, and division. Its includes input validation, error handling, and a looping menu interface.


The aim of this project is to help me improve my coding skill and my english proficiency. It is also a way for me to practice on creating a documentation. To understand this project, you need to know about three things : "variable", "function" and "loop". 


## Features 
- Supports Addition, Subtraction, Multiplication, and Division
- Supports Handling Simple Invalid Input 
- Allows repeating operation without restarting
- Simple text-based menu interface
  
## Requirements
- Python 3.11
- No external libraries

---

## How It Works

### Step 1 - Built a function to encapsulate each mathematical operation
The purpose of having a function is to encapsulate a part of a code into one logical unit, thereby facilitating reusability and maintainability. It is more preferable to avoid reiterating the same lines of code with the same logic in multiple instance throughout the code. Using a function allow your program to have a "shorter" code that is clean and can be employed in any desired location within a program.
```python

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

```
To create a function you need to define them by using the word 
```python 
def
``` 
and followed by the name of the function "add / sub / multi / div" and its parameters "(x,y)". Both the name of the parameter and the function can be wrote with any words or letter as you like.
```python
def add (x,y)
```
After you build the function header or function definition line you can then continue to built its body. The body of a function consist exclusively of the logic that you need the function to work as you intended. Using one of the function above as an example, the body of the function can be summarized as an operation to the parameter saved in a variable. The value of the variable then being called by another function to put a print statement in then return the variable.


---

### Step 2 - Built a Loop
The purpose of having a loop is to facilitate the handling of the multiple choice menu. In the process of constructing the function, we have already created 4 function to handle the mathematical operations. Using a loop would allow a user to choose which operation they would want to use, to change the operation and to exit from the program. 

In the context of this Project, there are two loop needed. The outer loop would be responsible for the selection of the mathematical operation whilst the inner loop would be responsible for the repetition of the chosen operation.
```python
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
```
To clear the confusion, first we will focus on the loop itself. The loop is begin by the word
```python
while True :
```
These words tell the computer to run the code below it until the user explicitly tell it to stop. As you can see in the code, there are many print statement that act as a menu that can be chosen by the user. For the user to choose certain menu, the user needed to input a menu number for the operation that the user need.
```python
    try:
        choose = int(input("Menu Number only : "))
    except ValueError:
        print("Invalid input, please enter numbers only")
        input("Press Enter to continue ....")
        continue
```
The code above simply work as error and input handling. You can choose from any number you like and if you choose something that is not a number, it would print a warning statement of an invalid input. An error handling was necessary because the variable "choose" only accept an integer as defined by the word "int".
```python
choose = int(input("Menu Number only : "))
```
In an instance where the input given is not a number, it would break the program. by giving it an error handling, the program would still able to continue.
```python
    except ValueError:
        print("Invalid input, please enter numbers only")
        input("Press Enter to continue ....")
        continue
```
Subsequent to handling the input, the program incorporates if - elif logic in the event where number 5 is selected it would exit the program and if the number 1 to 4 is selected it would choose from the menu associated to that number and if else, it would tell you that there's no such number.
```python
if choose == 5:
        print("Goodbye")
        sys.exit(0)

    elif choose in [1, 2, 3, 4]:
        ...

    else :
        print("No such option available.")
        input("Press Enter to continue ....")
        continue
```
If the chosen number is 1 to 4, it would initiated the inner loop. The logic on the inner loop is initiated by requesting a user to input two values in which are then saved in two separate variable. Subsequently the program then retrieves the number of the chosen menu and applies appropriate mathematical operation to the two number that have been inputted in the two separate variable before.
```python
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

...

            a = sure_number("First Number : ")
            b = sure_number("Second Number : ")

...
```
These variable work by calling the function "sure_number" where the logic to get input number work. Within the function, the input is saved in a variable "userinput". The space at the front and back is removed and the input then transformed into float and saved in a new variable "value". The program then would check if the value within the variable "value" is integer or non-integer. If the value is non-integer, it would show a print statement that the input is not a number.

Subsequent to the codes above, the if - elif logic begins to put the value that has been saved in variable "a" and "b" to be used by simply calling the related mathematical operation function. Because the unique rule for division, error handling pertaining zero division was needed. Then, the core logic for the inner loop begin.
```python
# Function to get input to do repetition of mathematical operation
def ask_repeat():
    while True:
        repeat = input("Again? (Y/N) : ").strip().lower()
        if repeat in ["y", 'n']:
            return repeat
        else :
            print("Your input is invalid, Please enter either the letter y or n. ")
            
...

            repeat = ask_repeat()
            if repeat == "y":
                time.sleep(1)
                continue
            elif repeat == "n":
                break

...

```
The logic for this section is almost identical to that of the "sure_number" function. Its purpose was to ensure that only letters "y" and "n" whether its lowercase or uppercase to be recognized as an intended letter. If you as a user choose letter "y", the chosen mathematical operation would kept repeating until a user choose letter "n" to exit from the loop.

---
### (Optional) Step 3 - Cleaning the command
By using built-in library to clean the command line, you can kept the command line to look clean and neat. Incorporating the os, sys, and time library from python.

```python
import os, sys, time

...

#Function to clear the screen
def clear_screen():
    os.system ('cls' if os.name == 'nt' else 'clear')

...

clear_screen()

...

sys.exit(0)

...

time.sleep(1)


```
Os library facilitate the cleaning of the command prompt by simply using the words "cls" for windows or "clear" for macintosh or linux. Its work by facilitating python to interact directly with the operating system. While the sys library facilitate the interaction with the python interpreter itself like exiting from a program as in the code above. On the other hand, time library function to give access to system time which allow a pause in the loop before it starts again. all of this optional option was simply to enhanced the user-friendliness of the program.


## License
This project is licensed under the MIT License - see the [View the License](https://github.com/ReiznVD/Simple-Command-Line-Calculator/blob/5deefec74f6270c1a10e69518a0f38e68c1d5fed/LICENSE) file for details

## Author
Created by [ReizVD](https://github.com/ReiznVD)

</p>
