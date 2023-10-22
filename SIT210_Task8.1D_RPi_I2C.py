# Import necessary libraries
import smbus
import time

# Define constants
BH1750 = 0x23 
CONTINUOUS_HIGH_RES_MODE_1 = 0x10

# Initialize the I2C bus
bus = smbus.SMBus(1)

# Function to read data from the BH1750 sensor
def ReadBH1750(device_address):
    # Read data from I2C interface
    data = bus.read_i2c_block_data(device_address, CONTINUOUS_HIGH_RES_MODE_1)
    # Calculate the light level from the sensor data
    result = (data[1] + (256 * data[0])) / 1.2
    return result

## Main program ##
try:
    while True:
        # Read the light level from the BH1750 sensor
        LightLevel = ReadBH1750(BH1750)
        
        # Categorize the light level and print the corresponding message
        if LightLevel < 5:
            print("Too Dark")
        elif LightLevel < 10:
            print("Dark")
        elif LightLevel < 20:
            print("Medium")
        elif LightLevel < 25:
            print("Bright")
        else:
            print("Too Bright")
        
        # Pause for 1 second
        time.sleep(1)
                
except KeyboardInterrupt:
    # Handle a keyboard interrupt (Ctrl+C) by cleaning up
    GPIO.cleanup()  