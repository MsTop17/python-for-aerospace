import math


def calculate_range(fuel_capacity, fuel_consumption_rate, true_airspeed):
    range_in_hours = fuel_capacity / fuel_consumption_rate
    range_in_miles = range_in_hours * true_airspeed
    return range_in_miles

def calculate_endurance(fuel_capacity, fuel_consumption_rate):
    endurance_in_hours = fuel_capacity / fuel_consumption_rate
    return endurance_in_hours

def calculate_total_weight(payload_weight, fuel_weight):
    return payload_weight + fuel_weight

def calculate_cg_position(moment_list, total_weight):
    total_moment = sum(moment_list)
    cg_position = total_moment / total_weight
    return cg_position

def calculate_moment(weight, arm):
    return weight * arm

def calculate_lift(cl, rho, velocity, s):
    return 0.5 * cl * rho * (velocity ** 2) * s

def calculate_drag(cd, rho, velocity, s):
    return 0.5 * cd * rho * (velocity ** 2) * s

def calculate_weight(mass, g=9.81):
    return mass * g

def calculate_acceleration(thrust, drag, weight, total_mass):
    return (thrust - drag - weight) / total_mass

def calculate_velocity(initial_velocity, acceleration, time):
    return initial_velocity + (acceleration * time)

def calculate_distance(velocity, time):
    return velocity * time

def pretty_print(range_val, endurance_val, total_weight_val, cg_pos_val, 
                 lift_val, drag_val, weight_val, accel_val, vel_val, dist_val):
    print("---------------------------------------")
    print("      AIRCRAFT PERFORMANCE REPORT      ")
    print("---------------------------------------")
    print(f"Range: {range_val:.2f} miles")
    print(f"Endurance: {endurance_val:.2f} hours")
    print(f"Total Weight: {total_weight_val:.2f} lbs")
    print(f"Center of Gravity Position: {cg_pos_val:.2f} ft")
    print(f"Lift: {lift_val:.2f} N")
    print(f"Drag: {drag_val:.2f} N")
    print(f"Weight: {weight_val:.2f} N")
    print(f"Acceleration: {accel_val:.2f} m/s^2")
    print(f"Velocity: {vel_val:.2f} m/s")
    print(f"Distance: {dist_val:.2f} m")
    print("---------------------------------------")

def save_info_to_file(range_val, endurance_val, total_weight_val, cg_pos_val, 
                       lift_val, drag_val, weight_val, accel_val, vel_val, dist_val, file):
    file.write("Performance Calculations:\n")
    file.write(f"Range: {range_val:.2f} miles\n")
    file.write(f"Endurance: {endurance_val:.2f} hours\n")
    file.write(f"Total Weight: {total_weight_val:.2f} pounds\n")
    file.write(f"Center of Gravity Position: {cg_pos_val:.2f} feet\n")
    file.write(f"Lift: {lift_val:.2f} Newtons\n")
    file.write(f"Drag: {drag_val:.2f} Newtons\n")
    file.write(f"Weight: {weight_val:.2f} Newtons\n")
    file.write(f"Acceleration: {accel_val:.2f} m/s^2\n")
    file.write(f"Velocity: {vel_val:.2f} m/s\n")
    file.write(f"Distance: {dist_val:.2f} meters\n")



# Define Parameters
fuel_capacity = 150.0 
fuel_consumption_rate = 12.0  
true_air_speed = 180.0  
payload = 500.0  
fuel_weight = fuel_capacity * 6.0  
cl = 0.5  
cd = 0.04  
rho = 1.225  
v = 50.0  
s = 25.0  
mass = 1200.0  
g = 9.81  
thrust = 5000.0  
time = 10.0  
initial_velocity = 0.0

# Calculate moments for CG position
moments = [
    calculate_moment(payload, 4.0),
    calculate_moment(fuel_weight, 6.0)
]

# Run Calculations
range_val = calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed)
endurance_val = calculate_endurance(fuel_capacity, fuel_consumption_rate)
total_weight_val = calculate_total_weight(payload, fuel_weight)
cg_pos_val = calculate_cg_position(moments, total_weight_val)
lift_val = calculate_lift(cl, rho, v, s)
drag_val = calculate_drag(cd, rho, v, s)
weight_val = calculate_weight(mass, g)
accel_val = calculate_acceleration(thrust, drag_val, weight_val, mass)
vel_val = calculate_velocity(initial_velocity, accel_val, time)
dist_val = calculate_distance(vel_val, time)

# Print Summary
pretty_print(
    range_val, endurance_val, total_weight_val, cg_pos_val,
    lift_val, drag_val, weight_val, accel_val, vel_val, dist_val
)




with open("aircraft_performance_analysis.txt", "w") as F:
    save_info_to_file(
        range_val, endurance_val, total_weight_val, cg_pos_val,
        lift_val, drag_val, weight_val, accel_val, vel_val, dist_val,
        file=F
    )

print("\nResults successfully saved to 'aircraft_performance_analysis.txt'.")