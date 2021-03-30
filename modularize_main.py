from modularize_helper import input_validation
"""
Alternatives:
    from modularize_helper import *
    import modularize_helper --> eta use korle function er age module er naam dite hbe.
    Example = modularize_helper.input_validation
    
"""


user_input = ""
while user_input != "exit":
    #Always take input as String exit
    user_input = input("Please enter the number of days.\n") 
    # by comma(,) is used to separate integers   
    #for num_of_days in set(user_input.split(',')):    
    input_validation(user_input)

