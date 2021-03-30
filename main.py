""" 
age = "I am 26"
print(f"I am {26} years old.") # 'f' stands for format. 
print(5/2)
 """
#Global Variables
calculate_to_unit = 24 # This is python naming convention
name_of_unit = "hours"
#Global Variables

""" 
print(f"24 days is = {calculate_to_unit} {name_of_unit}")
print(f"30 days is = {calculate_to_unit} {name_of_unit}")
print(f"365 days is = {calculate_to_unit} {name_of_unit}") 
"""


""" 
def days_to_units(name_of_days): #def is used to define a function(method).
    print(f"{name_of_days} days is = {name_of_days*calculate_to_unit} {name_of_unit}") 
""" 
# Sting er modhe variable use korte hole () use korte hbe

def days_to_units(name_of_days): #def is used to define a function(method).
    return (f"{name_of_days} days is = {name_of_days * calculate_to_unit} {name_of_unit}")   
    

""" 
days_to_units(20) # To run a function you have to call by giving () after the variable
days_to_units(30)
days_to_units(50) 
"""
""" 
def input_validation():
    if user_input.isdigit():#to check if the input value is int or text or something else
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_hours = days_to_units(user_input_number)
            print(calculated_hours)
        elif user_input_number == 0:
            print("Given value greater than 0 days") 
        #python can work without else statement 
    else:
        print("value is not an integer") 
"""

#try/except = try/exception = try/catch
def input_validation():
    try:
        user_input_number = int(num_of_days)
        if user_input_number > 0:
            calculated_hours = days_to_units(user_input_number)
            print(calculated_hours)
        elif user_input_number == 0:
            print("Given value greater than 0 days") 
        #python can work without else statement 
    except:
        print("value is not an integer")

user_input = ""
#----------------list-------------------------------

""" 
while user_input != "exit":
    user_input = input("Please enter the number of days.\n") #Always take input as String 
    # For clean code every functio should be modularized.
    #for num_of_days in user_input.split():# by default space is used to separate integers
    for num_of_days in user_input.split(','):# by comma(,) is used to separate integers    
        input_validation() """

#----------------------Set---------------------------
while user_input != "exit":
    user_input = input("Please enter the number of days.\n") #Always take input as String exit
    for num_of_days in set(user_input.split(',')):# by comma(,) is used to separate integers    
        input_validation()




