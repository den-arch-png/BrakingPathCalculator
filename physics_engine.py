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

    return max(0.0, aircraft_ground_speed - wind_speed_along_runway)


"""Vertical forces"""

def lift_force(airspeed, aircraft_data, environment_data) -> float:

    """Calculates the lift force"""

    air_density = environment_data["air_density"]
    wing_area = aircraft_data["wing"]["area"]
    lift_coefficient = aircraft_data["wing"]["lift_coefficient"]

    return 0.5 * air_density * airspeed**2 * wing_area * lift_coefficient

def normal_force(aircraft_data, environment_data) -> float:

    """Calculates the normal force"""

    slope_angle = airport_data["runways"]["vertical_profile"]["slope_angle"]
    slope_angle_rad = math.radians(slope_angle)
    mass = aircraft_data["mass"]
    gravity = environment_data["gravity"]
    lift = lift_force(aircraft_data, environment_data)

    return max(0.0, mass * gravity * math.cos(slope_angle_rad) - lift)


"""Longitudinal forces"""

def braking_force_wheels(aircraft_data) -> float:
    """Calculates the braking force from the wheels"""
    pass

def reverse_thrust(aircraft_data) -> float:

    """Calculates the reverse thrust force"""

    engine = aircraft_data["engines"]

    thrust_per_engine = engine["take_off_thrust"]
    number_of_engines = engine["number"]
    reverse_thrust_factor = engine["reverse_thrust_factor"]

    return thrust_per_engine * number_of_engines * reverse_thrust_factor

def rolling_resistance(normal_force, aircraft_data) -> float:

    """Calculates the rolling resistance force"""

    C_rr = aircraft_data["landing_gear"]["rolling_resistance_coefficient"]

    return C_rr * normal_force


"""Lateral forces"""



"""Aerodynamic forces"""
def drag_coefficient_calculation(aircraft_data) -> float:
    """Calculates the simplified drag coefficient."""

    wing = aircraft_data["wing"]

    cd0 = wing["zero_lift_drag_coefficient"]
    cd_gear = aircraft_data["landing_gear"]["drag_coefficient"]
    cd_flaps = aircraft_data["flaps"]["drag_coefficient"]

    cl = wing["lift_coefficient"]
    aspect_ratio = wing["aspect_ratio"]
    efficiency = wing["efficiency_factor"]

    induced_drag = cl**2 / (math.pi * aspect_ratio * efficiency)

    return cd0 + cd_gear + cd_flaps + induced_drag

def aerodynamic_drag(airspeed, aircraft_data, environment_data) -> float:
    """Calculates aerodynamic drag."""

    rho = environment_data["air_density"]
    area = aircraft_data["wing"]["area"]
    cd = drag_coefficient_calculation(aircraft_data)

    return 0.5 * rho * airspeed**2 * area * cd



"""Here begins the main function to calculate the braking distance"""

