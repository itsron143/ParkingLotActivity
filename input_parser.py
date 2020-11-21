import sys
from ParkingLot import ParkingLot

parking_lot = None


def execute(command):
    global parking_lot
    if command[0] == "Create_parking_lot":
        parking_lot = ParkingLot(int(command[1]))
    elif command[0] == "Park":
        parking_lot.park(str(command[1]), int(command[3]))
    elif command[0] == "Slot_numbers_for_driver_of_age":
        parking_lot.slot_nos_from_age(int(command[1]))
    elif command[0] == "Leave":
        parking_lot.leave(int(command[1]))
    elif command[0] == "Slot_number_for_car_with_number":
        parking_lot.slot_no_from_reg_no(str(command[1]))
    elif command[0] == "Vehicle_registration_number_for_driver_of_age":
        parking_lot.reg_nos_from_age(int(command[1]))
    else:
        print("Incorrect Command")


def readFile(fileName):
    try:
        with open(fileName) as file:
            commands = file.readlines()
            for command in commands:
                execute(command.replace('\n', '').split())
    except Exception as e:
        print(e)
