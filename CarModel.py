class CarModel:
    def __init__(self, model_name, model_config) -> None:
        self.model_name = model_name
        self.model_config = model_config

    def __functionality(self, model_name):
        """ This is a private method, and can only be accessed from within this class."""
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
    
    # Method to check configs for Elite model
    def model_elite(self):
        car_model = "Elite"
        car_config = ["CAMERA", "RADAR", "LiDAR"]
        if self.model_name == car_model and self.model_config == car_config:
            return self.__functionality(self.model_name)
        else:
            print (f"Wrong Configuration for {self.model_name.capitalize()}")

    # Method to check configs for Classic model
    def model_classic(self):
        car_model = "Classic"
        car_config = ["RADAR"]
        if self.model_name == car_model and self.model_config == car_config:
            return self.__functionality(self.model_name)
        else:
            print (f"Wrong Configuration for {self.model_name.capitalize()}")

    # Method to check configs for Paragon model    
    def model_paragon(self):
        car_model = "Paragon"
        car_config = ["CAMERA"]
        if self.model_name == car_model and self.model_config == car_config:
            return self.__functionality(self.model_name)
        else:
            print (f"Wrong Configuration for {self.model_name.capitalize()}")

    # Method to check configs for Elite model    
    def model_gentry(self):
        car_model = "Gentry"
        car_config = ["CAMERA", "RADAR"]
        if self.model_name == car_model and self.model_config == car_config:
            return self.__functionality(self.model_name)
        else:
            print (f"Wrong Configuration for {self.model_name.capitalize()}")