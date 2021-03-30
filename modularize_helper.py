calculate_to_unit = 24 # This is python naming convention
name_of_unit = "hours"
def days_to_units(name_of_days): #def is used to define a function(method).
    return (f"{name_of_days} days is = {name_of_days * calculate_to_unit} {name_of_unit}") 

def input_validation(num_of_days):
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