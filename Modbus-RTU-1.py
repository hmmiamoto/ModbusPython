from pymodbus.client.sync import ModbusSerialClient
from pymodbus.register_read_message import ReadInputRegistersResponse

import time


proxsys = ModbusSerialClient(
    method='rtu',
    port='/dev/ttyUSB0',
    stopbits=1,
    bytesize=8,
    baudrate=9600,
    parity='N',
    timeout=0.3
    )

connection = proxsys.connect()
print(connection)

# value = proxsys.read_coil(1,8,unit=0x05).bits
value = proxsys.read_discrete_inputs(0,8,unit=0x05).bits
print(value)

value = proxsys.read_holding_registers(14,2,unit=0x05).registers
print(value)

proxsys.write_coil(1, True, unit=0x05)
time.sleep(0.1)
proxsys.write_coil(2, True, unit=0x05)
time.sleep(0.1)
proxsys.write_coil(1, True, unit=0x05)
time.sleep(5)

proxsys.write_coil(1, False, unit=0x05)
time.sleep(0.1)
proxsys.write_coil(2, False, unit=0x05)
time.sleep(0.1)
proxsys.write_coil(1, False, unit=0x05)





