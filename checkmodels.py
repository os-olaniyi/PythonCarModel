from CarModel import *

# Read input from user
car_name = input("Enter your car name: ")
car_config = input("Enter your car configurations, separated by spaces as shown in the format (CAMERA RADAR LiDAR):\n")

# Convert the car_config from user to a list.
configuration = car_config.split()

# Ensure the car name input is Capitalized.
car_name = car_name.capitalize()

# Instantiate an object of Car model
car_model = CarModel(car_name, configuration)

def check_config (car_name, configuration):
    """ This function takes 2 parameters and use the user input name to call the appropriate configuration instance. """
    if car_name == "Elite":
        car_model.model_elite()
    elif car_name == "Classic":
        car_model.model_classic()
    elif car_name == "Gentry":
        car_model.model_gentry()
    elif car_name == "Paragon":
        car_model.model_paragon()
    else:
        print(f"No such car model here. {car_name}!")

check_config = check_config(car_name, configuration)