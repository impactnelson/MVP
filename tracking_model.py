import time
import random

class EnergyConsumptionTracker:
    def __init__(self):
        self.energy_data = []

    def track_energy(self, device_id):
        while True:
            energy_usage = random.uniform(0.5, 5.0)  # Simulate energy usage in kWh
            timestamp = time.time()
            self.energy_data.append({'device_id': device_id, 'energy_usage': energy_usage, 'timestamp': timestamp})
            time.sleep(60)  # Track energy usage every minute

    def get_energy_data(self):
        return self.energy_data

# Example usage
tracker = EnergyConsumptionTracker()
tracker.track_energy('device_1')

