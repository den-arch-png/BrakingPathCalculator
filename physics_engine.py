import json

"""This module takes raw data
 and calculates physical forces 
 contributing to braking distance"""


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


aircraft_data = load_json("a320-214.json")
environment_data = load_json("environment.json")
airport_data = load_json("vienna-schwechat.json")


"""Vertical forces"""

def normal_force() -> float:
    """Calculates the normal force"""
    pass

def lift_force() -> float:
    """Calculates the lift force"""
    pass



"""Longitudinal forces"""

def braking_force_wheels() -> float:
    """Calculates the braking force from the wheels"""
    pass

def reverse_thrust(data) -> float:
    """Calculates the reverse thrust force"""
    engine = data["engines"]

    thrust_per_engine = engine["take_off_thrust"]
    number_of_engines = engine["number"]
    reverse_thrust_factor = engine["reverse_thrust_factor"]

    return thrust_per_engine * number_of_engines * reverse_thrust_factor

def rolling_resistance() -> float:
    """Calculates the rolling resistance force"""
    pass

def weight_along_slope() -> float:
    """Calculates the weight component along the slope"""
    pass


"""Lateral forces"""



"""Aerodynamic forces"""

def aerodynamic_drag() -> float:
    """Calculates the aerodynamic drag force"""
    pass