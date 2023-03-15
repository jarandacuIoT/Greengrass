import struct


class UPS_Monitoring:
    def __init__(self, bus, address):
        self.bus = bus
        self.address = address

    def ReadVoltage(self):
        "This function returns as float Hat via the voltage " \
        "from the Raspi UPS the provided SMBus object"
        read = self.bus.read_word_data(self.address, 2)
        swapped = struct . unpack("<H", struct.pack("> H", read))[0]
        voltage = swapped * 1.25 / 1000 / 16
        return voltage

    def ReadCapacity(self):
        "This function returns as a float the remaining capacity of the battery connected to the Raspi UPS Hat via the provided SMBus object "
        read = self.bus.read_word_data(self.address, 4)
        swapped = struct.unpack("<H", struct.pack("> H", read))[0]
        capacity = swapped / 256
        return capacity
