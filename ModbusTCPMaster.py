# Pymodbus Synchronous Client Example (ModbusTCPMaster):
# ---------------------------------------------------------------------------


# --------------------------------------------------------------------------- #
# import the various server implementations
# --------------------------------------------------------------------------- #

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import time
import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
#logging.basicConfig(format=FORMAT)
#log = logging.getLogger()
#log.setLevel(logging.DEBUG)


def run_sync_client():
   
  # ------------------------------------------------------------------------#
  client = ModbusClient('localhost', port=502)
  # from pymodbus.transaction import ModbusRtuFramer
  # client = ModbusClient('localhost', port=5020, framer=ModbusRtuFramer)
  # client = ModbusClient(method='binary', port='/dev/ptyp0', timeout=1)
  # client = ModbusClient(method='ascii', port='/dev/ptyp0', timeout=1)
  # client = ModbusClient(method='rtu', port='/dev/ptyp0', timeout=1,
  #                       baudrate=9600)
  client.connect()
    
  interation = 0

  # This block will continuously poll the slave device (sensor) to read holding registers. To comeout of loop, use Ctl + C.
  while True:
      interation = interation + 1

      # ------------------------------------------------------------------------#
      # 1. Read Status of DI (Function code 02)
      #    The following query is to read 4 DI statuses of AXM-IO1 module
      # ----------------------------------------------------------------------- #
      
      registers = client.read_discrete_inputs(0, 28, unit=0x2)
    
      if not registers.isError():
        
        #log.debug(registers)

        # di_hex_value = registers.bits
        # di1_mask, di2_mask, di3_mask, di4_mask = 0x01, 0x02, 0x04, 0x08
        
        if registers.bits[0] == True:
            di1_status = "On"
        else:
            di1_status = "Off"

        if registers.bits[1] == True:
            di2_status = "On"
        else:
            di2_status = "Off"

        if registers.bits[2] == True:
            di3_status = "On"
        else:
            di3_status = "Off"

        if registers.bits[3] == True:
            di4_status = "On"
        else:
            di4_status = "Off"

        print("Reading 4 DI statuses of AXM-IO1 module. Iteration" + str(interation) + ":    " + "DI1=" + di1_status + ", DI2=" + di2_status + ", DI3=" + di3_status + ", DI4=" + di4_status)

      else:
        # Do stuff to error handling.
        print('Error message: {}'.format(registers))
      #-------------------------------------------------------------------------#


      # Read Data (Function Code 03)


      # Delay for 3 seconds for next read
      time.sleep(3)

if __name__ == "__main__":
    run_sync_client()