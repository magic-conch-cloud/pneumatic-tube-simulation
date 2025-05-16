def validate_input(value, min_value, max_value):
    if not (min_value <= value <= max_value):
        raise ValueError(f"Value {value} is out of bounds ({min_value}, {max_value})")
    return True

def calculate_gravitational_force(mass1, mass2, distance):
    G = 6.67430e-11  # Gravitational constant
    if distance <= 0:
        raise ValueError("Distance must be greater than zero.")
    force = G * (mass1 * mass2) / (distance ** 2)
    return force

def degrees_to_radians(degrees):
    import math
    return degrees * (math.pi / 180)

def radians_to_degrees(radians):
    import math
    return radians * (180 / math.pi)