import time
from nielvis import I2C, Bank, I2CSpeedMode

# specify the bank
bank = Bank.A
# specify the mode of operation that this program uses to communicate with the
# I2C slave device
speed = I2CSpeedMode.STANDARD
# configure an I2C session
with I2C(bank, speed) as i2c:
    # specify the 7-bit address
    slave_device_address = 0b1001111
    # specify the number of bytes to read from the I2C slave device
    number_bytes_to_read = 1
    # read data from the I2C slave device
    return_value = i2c.read(slave_device_address, number_bytes_to_read)
    # print the data
    print(return_value)
