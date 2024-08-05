# Car Model Configuration Checker

This project is designed to verify if the configurations of different car models are correct based on predefined allowable configurations. It consists of two main components: a class definition file (`classModel.py`) and a script to interact with the user (`checkmodels.py`).

## Project Structure

- `classModel.py`: Contains the `CarModel` class, which defines different car models and their allowable configurations.
- `checkmodels.py`: Script to interact with the user, taking inputs for car model name and configurations, and checking if the configurations are correct using the `CarModel` class.

## `CarModel` Class

The `CarModel` class is responsible for defining different car models and their functionalities. It includes a private methods to return a detailed functionality for each model.

### Methods

- `functionality`: Private method to print the functionalities of a given car model.
- `model_elite`: Checks if the configuration for the "Elite" model is correct.
- `model_classic`: Checks if the configuration for the "Classic" model is correct.
- `model_paragon`: Checks if the configuration for the "Paragon" model is correct.
- `model_gentry`: Checks if the configuration for the "Gentry" model is correct.

### Functionalities of Each Model

- **Elite**: Lane Changing, Overtaking, Intersections navigation
- **Classic**: Overtaking
- **Gentry**: Lane Changing, Overtaking
- **Paragon**: Lane Changing

## `checkmodels.py` Script

The `checkmodels.py` script is the user interface for the project. It prompts the user to enter a car model name and its configurations, then checks if the provided configurations are correct.

### Usage

1. Run the `checkmodels.py` script.
2. Enter the car model name when prompted.
3. Enter the car configurations separated by spaces (e.g., `CAMERA RADAR LiDAR`).
4. The script will output whether the configurations are correct and list the functionalities of a correct car model.

### Example

```sh
$ python checkmodels.py
Enter your car name: Elite
Enter your car configurations, separated by spaces as shown in the format (CAMERA RADAR LiDAR):
CAMERA RADAR LiDAR
ALLOWABLE VEHICLE CONFIG FOR ELITE IS CORRECT.

FUNCTIONALITIES INCLUDE:
 Lane Changing
 Overtaking
 Intersections navigation
```

## Requirements

- Python 3.x

## Installation

Clone the repository and navigate to the project directory:

```sh
git clone git@github.com:os-olaniyi/PythonCarModel.git
cd PythonCarModel
```

Run the script:

```sh
python checkmodels.py
```

## Contributing

Contributions are welcome! Please submit a pull request.
