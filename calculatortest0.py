import os
import math
import pandas as pd
import numpy as np
import tkinter as tk
import sys #to export output as a file

import tkinter as tk

root = tk.Tk()
root.title("Frame Demo")
root.config(bg="skyblue")

# Create Frame widget
frame = tk.Frame(root, width=200, height=200)
frame.pack(padx=10, pady=10)

root.mainloop()

log_file = open('calculator_output.txt', 'w')  # 'w' will overwrite each time

def log_print(*args, **kwargs):
    """Print to both console and file"""
    message = ' '.join(str(arg) for arg in args)
    print(message)  # Print to console
    print(message, file=log_file)  # Print to file
    log_file.flush()  # Force write to disk

def VerifyLogin(input_user, input_password, filepath='UserPass.csv'):
    try:
        with open(filepath, 'r') as file:
            for line in file:
                fields = line.strip().split(",")
                if len(fields) >= 2:
                    file_username = fields[0].strip()
                    file_password = fields[1].strip()
                    if file_username == input_user and file_password == input_password:
                        return True
    except FileNotFoundError:
        log_print(f"Error: File {filepath} not found")
    except Exception as e:
        log_print(f"Unexpected error: {e}")
    return False

# User prompts
username = input("Input username: ")
password = input("Input password: ")

# Call the function
if VerifyLogin(username, password):
    log_print("Login successful!")
else:
    log_print("Login failed!")
    log_file.close()
    quit()

while True:
    MathMode = input("type reg for regular operations, type complex for more functions")
    if MathMode == ("reg"):
        try:
            FirstZ= input("what do you want to do with these two numbers?input from -, +, /, *(for multiply), %(for modulus) , **(for power of)") 
            x = float(input("enter your first number:"))
            y = float(input("enter your second number:"))
            z= FirstZ.strip()
            if z == ("-"):
                log_print(x - y)
            elif z == ("+") :
                log_print(x + y)
            elif z == ("*") :
                log_print(x * y)
            elif z == ("/") :
                log_print(x / y)
            elif z == ("%") :
                log_print(x % y)
            elif z == ("**") :
                log_print(x ** y)
        except ZeroDivisionError:
            log_print("you can't do that!")
        except SyntaxError:
            log_print("your input doesn't make sense to my code :(")
        break
    
    elif MathMode == ("complex"):  # Changed to elif and fixed indentation
        try:
            x = float(input("enter your number:"))
            FirstZ = input("input a trig function: sin, cos, or tan, or you could type arc before each function for arc functions, log, or sqrt.")
            z = FirstZ.strip()
            if z == ("sin"):
                log_print(math.sin(x))
            elif z == ("arcsin"):
                log_print(math.asin(x))
            elif z == ("cos"):
                log_print(math.cos(x))
            elif z == ("arccos"):
                log_print(math.acos(x))
            elif z == ("arctan"):
                log_print(math.atan(x))
            elif z == ("tan"):
                log_print(math.tan(x))
            elif z == ("log"):
                log_print(math.log(x))
            elif z == ("sqrt"):
                if x >= 0:
                    log_print(math.sqrt(x))
                else:
                    log_print("Error: Cannot take square root of a negative number!")
        except SyntaxError:
            log_print("your input doesn't make sense to my code :(")
        break


log_file.close()
print(f"\nAll output has been saved to: {os.path.abspath('calculator_output.txt')}")