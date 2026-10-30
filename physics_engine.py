import json
import math

"""This module takes raw data
 and calculates physical forces 
 contributing to braking distance"""


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

aircraft_data = load_json("a320-214.json")
environment_data = load_json("environment.json")
airport_data = load_json("vienna-schwechat.json")



def airspeed_calculation(aircraft_data, environment_data) -> float:

    """Calculates the airspeed based on ground speed and wind conditions"""

    aircraft_ground_speed = aircraft_data["ground_speed"]
    wind_speed = environment_data["wind_speed"]
    wind_direction = environment_data["wind_direction"]
    wind_direction_rad = math.radians(wind_direction)
    wind_speed_along_runway = wind_speed * math.cos(wind_direction_rad)

    return aircraft_ground_speed - wind_speed_along_runway


"""Vertical forces"""

def lift_force(aircraft_data, environment_data) -> float:

    """Calculates the lift force"""

    air_density = environment_data["air_density"]
    airspeed = airspeed_calculation()
    wing_area = aircraft_data["wing"]["area"]
    lift_coefficient = aircraft_data["wing"]["lift_coefficient"]

    return 0.5 * air_density * airspeed**2 * wing_area * lift_coefficient

def normal_force(aircraft_data, environment_data) -> float:

    """Calculates the normal force"""

    mass = aircraft_data["mass"]
    gravity = environment_data["gravity"]
    lift = lift_force()

    return mass * gravity - lift


"""Longitudinal forces"""

def braking_force_wheels() -> float:
    """Calculates the braking force from the wheels"""
    pass

def reverse_thrust(aircraft_data) -> float:

    """Calculates the reverse thrust force"""

    engine = aircraft_data["engines"]

    thrust_per_engine = engine["take_off_thrust"]
    number_of_engines = engine["number"]
    reverse_thrust_factor = engine["reverse_thrust_factor"]

    return thrust_per_engine * number_of_engines * reverse_thrust_factor

def rolling_resistance() -> float:

    """Calculates the rolling resistance force"""

    C_rr = aircraft_data["landing_gear"]["rolling_resistance_coefficient"]
    normal_force_value = normal_force()

    return C_rr * normal_force_value

def weight_along_slope() -> float:
    """Calculates the weight component along the slope"""
    pass


"""Lateral forces"""



"""Aerodynamic forces"""

def aerodynamic_drag() -> float:
    """Calculates the aerodynamic drag force"""
    pass