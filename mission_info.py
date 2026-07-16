mission_duration = 10
fuel_level = 1000000
distance_to_destination = 5000056565
mission_time = 0
fuel_consumption_rate = 50
distance_traveled_per_hour = 40000

while mission_time <= mission_duration:
    fuel_level -= fuel_consumption_rate
    distance_to_destination -= distance_traveled_per_hour
    print("Mission Time : ", mission_time)
    print("remaining fuel : ", fuel_level, "gallons")
    print("Distance to destination : " ,distance_to_destination, "kilometers\n" )

    if fuel_level <= 0 or distance_to_destination <= 0:
        break
    mission_time += 1
print("Misson Complete")