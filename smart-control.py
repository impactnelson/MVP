class SmartDevice:
    def __init__(self, device_id, device_name):
        self.device_id = device_id
        self.device_name = device_name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f'{self.device_name} is turned on.')

    def turn_off(self):
        self.is_on = False
        print(f'{self.device_name} is turned off.')

    def get_status(self):
        return {'device_id': self.device_id, 'device_name': self.device_name, 'is_on': self.is_on}

# Example usage
device = SmartDevice('device_1', 'Living Room Light')
device.turn_on()
device.turn_off()
print(device.get_status())

