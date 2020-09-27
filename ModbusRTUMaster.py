# Pymodbus Synchronous Client Example (ModbusRTUMaster):
# --------------------------------------------------------------------------------------------------------
# The following is an example of how to use the ModbusRTUMaster
# to read holding registers to aquire Temperature and Humidity data from Modbus slave (Sensor device).

# Setup:
# ------
# 1. Modbus slave (Real/Simulated Sensor device) to be connected to the Ubuntu Server using serial port

# 2. ModbusRTUMaster is written in Python and is running inside Ubuntu Server 18.04.
#    Pre-requisites are, 'Python' and 'pymodbus' to be installed in Ubuntu 18.04 Server.

# 3. Modbus Slave configuration:

#    Slave ID (Unit number) = 1,
#    Start of Holding registers address (start code) = 0x0000,
#    Number of registers (Amount of Data) = 2,
#    Temperature Data = To get a current temperature value, divide read value (first register) by 100.
#    Humidity Data = To get a current Humidity value, divide read value (second register) by 100.
# -------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------- #
# import the various server implementations
# --------------------------------------------------------------------------- #
import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer
import time
import logging

#logging.basicConfig()
#log = logging.getLogger()
#log.setLevel(logging.DEBUG)

# Symbol to display Celcius
degree_sign = u"\N{DEGREE SIGN}"

# Modbus master serial port device (this should be connected to the slave device serial port)
port = 'COM9'
# Serial baudrate which matches to Modbus slave (sensor device)
baudrate = 115200

client = ModbusClient(
  method = 'rtu'
  ,port='COM9'
  ,baudrate=baudrate
  ,parity = 'O'
  ,timeout=1
  )
# Open connection with serial port with defined port configurations
connection = client.connect()

interation = 0

# This block will continuously poll the slave device (sensor) to read holding registers. To comeout of loop, use Ctl + C.
while True:
    interation = interation + 1
    
    registers  = client.read_input_registers(0x0000,2,unit=1)# start_address, count, slave_id
    
    if not registers.isError():
      # Read temperature from first register and divide the value by 100 for celcius format
      temperature = registers.registers[0]/float(100)
    
      # Read Humidity from second register and divide the value by 100 for RH format
      humidity = registers.registers[1]/float(100)
    
      # Print values onto Terminal
    
      iteration_str = "Interation" + str(interation)
      temperature_str = "Temperatute = " + str(temperature) + degree_sign + 'C'
      humidity_str = "Humidity = " + str(humidity) + " RH"
    
      print(iteration_str + ": " + temperature_str + ", "+ humidity_str)
    
    else:
      # Do stuff to error handling.
      print('Error message: {}'.format(registers))
      # Delay for 3 seconds for next read
    
    print("Error")

    time.sleep(3)