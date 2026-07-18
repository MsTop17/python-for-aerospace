import pandas as pd

planet_distances = {
    'Mercury' : 57.2,
    'Venus' : 100.2,
    'Earth' : 149.6,
    'Mars' : 227.9,
    'Jupiter' : 778.6,
    'Saturn' : 1433.5,
    'Uranus' : 2872.5,
    'Neptune' : 4495.1,
    'Pluto' : 5986.4
}

moon_data = {
    'Planet' : [ 'Jupiter','Jupiter', 'Saturn', 'Saturn','Uranus','Neptune'],
    'Moon': ['Io','Ganymede','Titan','Rhea','Titania', 'Triton'],
    'Diameter (km)' : [ 3642,5262,5150, 1528, 1578, 2707],
    'Orbital Period (days)' :[1.77, 7.15, 15.95, 4.52, 8.71, 5.88] 
}


planet_distances = pd.Series(planet_distances)
moon_characteristics = pd.DataFrame(moon_data)
print("Average distance")
print(planet_distances.mean())


print("\nNumber of moons")
outer_planets = ['Jupiter','Saturn','Uranus','Neptune']

for planet in outer_planets:
    num_moons = moon_characteristics[moon_characteristics['Planet'] == planet].shape[0]
    print(f"{planet}: {num_moons}")
print("\n")
for planet in outer_planets:
    largest_moon = moon_characteristics[moon_characteristics['Planet'] == planet].sort_values(by='Diameter (km)', ascending= False).iloc[0]
    print(f"{planet} : {largest_moon['Moon']} ({largest_moon['Diameter (km)']} km)")

