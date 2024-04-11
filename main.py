import matplotlib.pyplot as plt
import numpy as np
import os
from load_data import load_data
from sort import bubble_sort


if __name__ == "__main__":
    data = load_data('activity.csv')
    power_W = data['PowerOriginal']
    print(power_W)
    sorted_power_W = bubble_sort(power_W)
    print(sorted_power_W[::-1])
    reversed_power_W = sorted_power_W[::-1]

def plot_line_chart(sorted_power_W):
    # Indizes der Liste erstellen, die als x-Achse dienen
    x = np.linspace(0, 30, len(sorted_power_W))
    # Erstellen des Liniendiagramms
    plt.figure(figsize=(10, 5))  # Größe des Diagramms festlegen
    plt.plot(x, reversed_power_W)  # Liniendiagramm erstellen
    
    # Hinzufügen von Titel und Beschriftungen
    plt.title('Leistungskurve')
    plt.xlabel('t/min')
    plt.ylabel('Watt')
    
    # Optional: Gitterlinien hinzufügen
    plt.grid(True)
    
    # Speichern des Diagramms im Ordner 'figures'
    plt.savefig('figures/Leistungskurve') 
    
    # Diagramm anzeigen
    plt.show()

# Funktionsaufruf, um das Diagramm zu zeichnen
plot_line_chart(sorted_power_W)
