import matplotlib.pyplot as plt
import pandas as pd

planetary_metrics = {
    'Planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
    'Distance_AU': [0.39, 0.72, 1.00, 1.52, 5.20, 9.58, 19.22, 30.05],
    'Orbital_Period_Years': [0.24, 0.62, 1.00, 1.88, 11.86, 29.46, 84.01, 164.8]
}

df = pd.DataFrame(planetary_metrics)

plt.figure(figsize=(10, 6))
plt.scatter(df['Distance_AU'], df['Orbital_Period_Years'], color='blue', marker='o', s=60, zorder=3)

plt.xscale('log')
plt.xticks([0.3, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 30.0], ['0.3', '0.5', '1.0', '2.0', '5.0', '10.0', '20.0', '30.0'])

plt.title('Solar System: Orbital Period vs. Distance from Sun (Log Scale)')
plt.xlabel('Semi-Major Axis Distance (AU) - Logarithmic Scale')
plt.ylabel('Orbital Period (Earth Years)')
plt.grid(True, linestyle='--', alpha=0.5, which="both")

for idx, row in df.iterrows():
    plt.annotate(
        row['Planet'], 
        (row['Distance_AU'], row['Orbital_Period_Years']), 
        textcoords="offset points", 
        xytext=(0, 8), 
        ha='center',
        weight='bold'
    )

plt.tight_layout()
plt.savefig('orbital_trajectory_plot.png', dpi=300, bbox_inches='tight')
plt.show()