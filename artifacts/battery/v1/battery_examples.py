# ! / Usr / bin / env python
import smbus
import time
from battery_utils import UPS_Monitoring

bus = smbus.SMBus(1)  # 0 = / dev / i2c-0 (port I2C0), 1 = / dev / i2c-1 (port I2C1)
UPS_data = UPS_Monitoring(bus, 0x36)
print("++++++++++++++++++++")
print("Voltage:% 5.2fV" % UPS_data.ReadVoltage())
print("Battery:% 5i %%" % UPS_data.ReadCapacity())
if UPS_data.ReadCapacity() == 100:
    print("Battery FULL")
if UPS_data.ReadCapacity() < 20:
    print("Battery LOW")
print("++++++++++++++++++++")
time.sleep(2)
