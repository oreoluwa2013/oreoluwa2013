# Solve a simple series circuit

def series_circuit(voltage, resistances):
    total_resistance = sum(resistances)
    current = voltage / total_resistance
    voltage_drops = [current * r for r in resistances]
    
    return current, voltage_drops

# Example usage
V = 12  # volts
resistors = [2, 4, 6]  # ohms

I, drops = series_circuit(V, resistors)

print("Total Current:", I, "A")
print("Voltage Drops:", drops)