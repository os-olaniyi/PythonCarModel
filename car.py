def functionality(model_name):
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



def elite(name, configs):
    car_name = "Elite"
    car_config = ["CAMERA", "RADAR", "LiDAR"]
    
    if name == car_name and configs == car_config:
        functionality(car_name)
        #return True
    else:
        print (f"Wrong Configuration for {car_name.capitalize()}")
        #return False


def classic(name, configs):
    car_name = "Classic"
    car_config = ["RADAR"]
    
    if name == car_name and configs == car_config:
        functionality(car_name)
        #return True
    else:
        print (f"Wrong Configuration for {car_name.capitalize()}")
        #return False


def gentry(name, configs):
    car_name = "Gentry"
    car_config = ["CAMERA", "RADAR"]
    
    if name == car_name and configs == car_config:
        functionality(car_name)
        #return True
    else:
        print (f"Wrong Configuration for {car_name.capitalize()}")
        #return False



def paragon(name, configs):
    car_name = "Paragon"
    car_config = ["CAMERA"]
    
    if name == car_name and configs == car_config:
        functionality(car_name)

    else:
        print (f"Wrong Configuration for {car_name.capitalize()}")


car_name = input("Enter your car name: ")
car_config = input("Enter your car configs below, separated by spaces as shown in the format (CAMERA RADAR LiDAR):\n ")
configuration = car_config.split()
car_name = car_name.capitalize()
print (car_name)
print(configuration)

def check_config (car_name, configuration):
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