
# emission_model.py

def calculate_emissions(activity_data):
    """
    Calculates total emissions based on input activity data.
    :param activity_data: dict with activity type and value
    :return: total emissions (float)
    """
    emission_factors = {
        'electricity_kwh': 0.92,  # kg CO2 per kWh
        'fuel_liters': 2.31,      # kg CO2 per liter
    }

    total_emissions = 0
    for activity, value in activity_data.items():
        factor = emission_factors.get(activity, 0)
        total_emissions += factor * value

    return total_emissions

if __name__ == "__main__":
    sample_data = {'electricity_kwh': 1500, 'fuel_liters': 300}
    emissions = calculate_emissions(sample_data)
    print(f"Total Emissions: {emissions} kg CO2")
