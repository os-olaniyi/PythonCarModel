def functionality(model_name):
    """ This function return the functionality of each car model. """

    if model_name == "Elite":
        functionality = (f"ALLOWABLE VEHICLE CONFIG FOR {model_name.upper()} IS CORRECT.\n\nFUNCTIONALITIES INCLUDE:\n Lane Changing\n Overtaking\n Intersections navigation ")
        print(functionality)
    elif model_name == "Classic":
        functionality = (f"ALLOWABLE VEHICLE CONFIG FOR {model_name.upper()} IS CORRECT.\n\nFUNCTIONALITIES INCLUDE:\n Overtaking\n ")
        print(functionality)
    elif model_name == "Gentry":
        functionality = (f"ALLOWABLE VEHICLE CONFIG FOR {model_name.upper()} IS CORRECT.\n\nFUNCTIONALITIES INCLUDE:\n Lane Changing\n Overtaking\n")
        print(functionality)
    elif model_name == "Paragon":
        functionality = (f"ALLOWABLE VEHICLE CONFIG FOR {model_name.upper()} IS CORRECT.\n\nFUNCTIONALITIES INCLUDE:\n Lane Changing\n")
        print(functionality)


# Define the configuration for the Elite model
def elite(name, configs):
    car_name = "Elite"
    car_config = ["CAMERA", "RADAR", "LiDAR"]
    
    if name == car_name and configs == car_config:
        functionality(car_name)
        #return True
    else:
        print (f"Wrong Configuration for {car_name.capitalize()}")
        #return False


# Define the configuration for the Elite model
def classic(name, configs):
    car_name = "Classic"
    car_config = ["RADAR"]
    
    if name == car_name and configs == car_config:
        functionality(car_name)
    else:
        print (f"Wrong Configuration for {car_name.capitalize()}")


def gentry(name, configs):
    car_name = "Gentry"
    car_config = ["CAMERA", "RADAR"]
    
    if name == car_name and configs == car_config:
        functionality(car_name)
    else:
        print (f"Wrong Configuration for {car_name.capitalize()}")



def paragon(name, configs):
    car_name = "Paragon"
    car_config = ["CAMERA"]
    
    if name == car_name and configs == car_config:
        functionality(car_name)
    else:
        print (f"Wrong Configuration for {car_name.capitalize()}")



# Read in the user inputs
car_name = input("Enter your car name: ")
car_config = input("Enter your car configs below, separated by spaces as shown in the format (CAMERA RADAR LiDAR):\n ")
#Split the User input for car configuration to a list.
configuration = car_config.split()
car_name = car_name.capitalize()
print (car_name)
print(configuration)


#Define function that Check for the configuration using the model name.
def check_config (car_name, configuration):
    
    """ This function takes 2 input parameters."""
    if car_name == "Elite":
        elite(name = car_name, configs = configuration)
    elif car_name == "Classic":
        classic(name = car_name, configs = configuration)
    elif car_name == "Gentry":
        gentry(name = car_name, configs = configuration)
    elif car_name == "Paragon":
        paragon(name = car_name, configs = configuration)
    else:
        print(f"No such vehicle Model here. {car_name}!")

check_config = check_config(car_name, configuration)