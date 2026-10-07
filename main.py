import random
import time

# --- Configuration for Gardenly's Smart System ---
MOISTURE_THRESHOLD = 30  # % - If soil moisture drops below this, consider watering
TEMP_THRESHOLD = 25      # °C - If air temperature is above this, consider high evaporation risk
SIMULATION_INTERVAL = 2  # seconds between sensor readings in the simulation

# --- Gardenly Smart Irrigation System Simulation ---

def get_simulated_sensor_data():
    """Simulates reading data from soil moisture and temperature sensors."""
    soil_moisture = random.randint(10, 90)  # Simulate soil moisture percentage
    air_temperature = random.randint(15, 35) # Simulate air temperature in Celsius
    print(f"SENSOR READINGS: Soil Moisture: {soil_moisture}% | Air Temperature: {air_temperature}°C")
    return soil_moisture, air_temperature

def decide_irrigation(soil_moisture, air_temperature):
    """
    Gardenly's core automation logic: Decides whether to irrigate based on sensor data.
    This logic aims to optimize water usage and plant health by considering both dryness
    and environmental factors like temperature (evaporation).
    """
    needs_watering_due_to_dryness = soil_moisture < MOISTURE_THRESHOLD
    high_evaporation_risk = air_temperature > TEMP_THRESHOLD

    # Gardenly's smart decision: Water if soil is dry AND there's a high evaporation risk.
    # This prevents unnecessary watering on cool days (even if slightly dry) and ensures
    # plants get water when they truly need it due to heat and dryness.
    if needs_watering_due_to_dryness and high_evaporation_risk:
        print("DECISION: Soil is dry AND temperature is high. Initiating irrigation to prevent plant stress.")
        return True
    elif needs_watering_due_to_dryness:
        print("DECISION: Soil is dry, but temperature is moderate. Holding off to prevent overwatering.")
        return False
    else:
        print("DECISION: Soil moisture is adequate. No irrigation needed.")
        return False

def perform_irrigation():
    """Simulates activating the irrigation system (e.g., opening a valve)."""
    print("ACTION: Irrigation system activated for a short period.")
    time.sleep(1) # Simulate the duration of watering
    print("ACTION: Irrigation system deactivated.")

def main():
    print("--- Gardenly Smart Garden Management System Simulation ---")
    print("Monitoring garden conditions and automating irrigation for efficiency.")
    print(f"Configuration: Watering triggered if Moisture < {MOISTURE_THRESHOLD}% AND Temp > {TEMP_THRESHOLD}°C.")
    print("-" * 60)

    irrigation_count = 0
    simulation_cycles = 5 # Number of times the system checks conditions

    for i in range(simulation_cycles):
        print(f"\n--- Cycle {i+1}/{simulation_cycles} ---")
        soil_moisture, air_temperature = get_simulated_sensor_data()

        # The core automation step: using sensor data to make a decision
        if decide_irrigation(soil_moisture, air_temperature):
            perform_irrigation()
            irrigation_count += 1
        else:
            print("ACTION: No irrigation performed.")

        if i < simulation_cycles - 1:
            print(f"Waiting {SIMULATION_INTERVAL} seconds for next reading...")
            time.sleep(SIMULATION_INTERVAL)

    print("\n" + "-" * 60)
    print(f"SIMULATION COMPLETE. Total irrigations performed: {irrigation_count}")
    print("--- End of Gardenly Simulation ---")

if __name__ == "__main__":
    main()
