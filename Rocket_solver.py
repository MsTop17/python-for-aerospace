# Rocket Engine Performance Calculator

# specific_impulse = thrust / (mass_flow * 9.81)
# exhaust_velocity = specific_impulse * 9.81


thrust = float(input("Thrust of the engine: "))
mass_flow = float(input("mass flow rate : "))
specific_impulse = thrust / (mass_flow * 9.81)
exhaust_velocity = specific_impulse * 9.81
print(str(specific_impulse))
print(str(exhaust_velocity)) 
