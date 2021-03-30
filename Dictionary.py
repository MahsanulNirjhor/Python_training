def execute():
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
while user_input!="exit":
    user_input = input("Enter your value \n")
    print(f'User input is {user_input}')
    days_and_units = user_input.split(":")
    days_and_units_dictionary = {"Days":days_and_units[0],"Unit":days_and_units[1]}
    print(days_and_units_dictionary)