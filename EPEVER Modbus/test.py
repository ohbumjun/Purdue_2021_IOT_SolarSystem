import minimalmodbus
import serial
import epever_modbus as epever
import time
import datetime


XTRA3210N = minimalmodbus.Instrument(port='COM1', slaveaddress=1, mode=minimalmodbus.MODE_RTU)

XTRA3210N.serial.baudrate = 115200
XTRA3210N.serial.stopbits = 1
XTRA3210N.serial.bytesize = 8
XTRA3210N.serial.parity = serial.PARITY_NONE
XTRA3210N.serial.timeout = 1

XTRA3210N.clear_buffers_before_each_transaction = True

if XTRA3210N.read_bit(epever.DAY_NIGHT, 2) == 0:
    print("It's day time")
else:
    print("It's night time")


while True: 
    try:
        print(str(datetime.datetime.now()) + '\n')

        pv_voltage = XTRA3210N.read_register(epever.PV_VOLTAGE, 2, 4)
        pv_current = XTRA3210N.read_register(epever.PV_CURRENT, 2, 4)
        pv_power_l = XTRA3210N.read_register(epever.PV_POWER_L, 2, 4)
        pv_power_h = XTRA3210N.read_register(epever.PV_POWER_H, 2, 4) * 65536
        pv_power = pv_power_h + pv_power_l

        print("PV Voltage: " + str(pv_voltage) + "V")
        print("PV Current:" + str(pv_current) + "A")
        print("PV Power: " + str(pv_power) + "W")

        bt_voltage = XTRA3210N.read_register(epever.BT_VOLTAGE, 2, 4)
        bt_current = XTRA3210N.read_register(epever.BT_CURRENT, 2, 4)
        bt_power_l = XTRA3210N.read_register(epever.BT_POWER_L, 2, 4)
        bt_power_h = XTRA3210N.read_register(epever.BT_POWER_H, 2, 4) * 65536
        bt_power = bt_power_h + bt_power_l
        bt_soc = XTRA3210N.read_register(epever.BT_PERCENT, 0, 4)

        print("Battery Voltage: " + str(bt_voltage) + "V")
        print("Battery Current: " + str(bt_current) + "A")
        print("Battery Power: " + str(bt_power) + "W")
        print("Battery Soc: " + str(bt_soc) + "%")

    except minimalmodbus.NoResponseError:
        print(minimalmodbus.NoResponseError)

    print('\n')

    time.sleep(10)

