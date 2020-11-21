class ParkingLot:
    """
    Class representation of a Parking Lot.

    Attributes
    ----------
    max_size : int
        size of the parking lot 
    available_slots : list
        list of available slots to park in
    reg_no_slot_dict : dict
        helper dict with registration number as key and slot parked in as value
    driver_age_slots_dict : dict
        helper dict with driver age as key and slots(list) parked in as value
    slot_car_dict : dict
        helper dict with slot as key and Car object as value

    Methods
    -------
    park(reg_no, driver_age)
        Simulates parking of the car in the lot. Uses available slot, fills in helper dicts with appropriate values
    leave(slot)
        Simulates leaving of the car from the lot. Adds slot to available slots, removes values from helper dicts
    slot_nos_from_age(driver_age):
        Prints slot numbers of all cars with drivers age as specified
    slot_no_from_reg_no(reg_no):
        Prints slot number of the car with specified registration number
    reg_nos_from_age(driver_age):
        Prints registration number of the cars with drivers age as specified
    """

    class Car:
        """
        Class representation of a Car.
        """

        def __init__(self, reg_no, driver_age):
            """
            Parameters
            ----------
            reg_no : str
            driver_age : int
            """
            self.reg_no = reg_no
            self.driver_age = driver_age

    max_size = 0

    available_slots = []
    reg_no_slot_dict = {}
    driver_age_slots_dict = {}
    slot_car_dict = {}

    def __init__(self, max_size):
        """
            Parameters
            ----------
            max_size : int
        """
        if max_size <= 0 or max_size > 1000:
            print("Invalid Slots, Parking Lot has a size of 1-1000 only. Please try again with a valid number of slots.")
            return
        self.max_size = max_size
        for i in range(1, max_size+1):
            self.available_slots.append(i)
        print("Created parking of", max_size, "slots")

    def park(self, reg_no, driver_age):
        """
        Simulates parking of the car in the lot. Uses available slot, fills in helper dicts with appropriate values

        Parameters
        ----------
        reg_no : str
        driver_age : int
        """
        if len(self.slot_car_dict) > self.max_size:
            print("Parking Lot is Full.")
            return
        if self.max_size == 0:
            print("Parking Lot not Created.")
            return
        if reg_no in self.reg_no_slot_dict:
            print("Vehicle with identical registration number already parked in. Please check the number again.")
            return
        self.available_slots.sort()
        slot = self.available_slots[0]
        car = self.Car(reg_no, driver_age)
        self.slot_car_dict[slot] = car
        self.reg_no_slot_dict[reg_no] = slot
        reg_no_list = self.driver_age_slots_dict.get(driver_age, 0)
        if reg_no_list:
            self.driver_age_slots_dict.pop(driver_age)
            reg_no_list.append(reg_no)
            self.driver_age_slots_dict[driver_age] = reg_no_list
        else:
            reg_no_list = []
            reg_no_list.append(reg_no)
            self.driver_age_slots_dict[driver_age] = reg_no_list
        print("Car with vehicle registration number \""+reg_no+"\" has been parked at slot number", slot)
        self.available_slots.pop(0)

    def leave(self, slot):
        """
        Simulates leaving of the car from the lot. Adds slot to available slots, removes values from helper dicts

        Parameters
        ----------
        slot : int
        """
        if self.max_size == 0:
            print("Parking Lot not Created.")
            return
        car_leaving = self.slot_car_dict.get(slot, 0)
        if car_leaving:
            self.slot_car_dict.pop(slot)
            self.reg_no_slot_dict.pop(car_leaving.reg_no)
            reg_no_list = self.driver_age_slots_dict.get(car_leaving.driver_age, 0)
            self.driver_age_slots_dict.pop(car_leaving.driver_age)
            reg_no_list.remove(car_leaving.reg_no)
            self.driver_age_slots_dict[car_leaving.driver_age] = reg_no_list
            self.available_slots.append(slot)
            self.available_slots.sort()
            print("Slot number", slot, "vacated, the car with vehicle registration number \"" + car_leaving.reg_no +
                  "\" left the space, the driver of the car was of age", car_leaving.driver_age)
        else:
            print("Slot:", slot, "is already empty.")

    def slot_nos_from_age(self, driver_age):
        """ 
        Prints slot numbers of all cars with drivers age as specified

        Parameters
        ----------
        driver_age : int
        """
        if self.max_size == 0:
            print("Parking Lot not Created.")
            return
        reg_no_list = self.driver_age_slots_dict.get(driver_age, 0)
        if reg_no_list:
            slot_list = []
            for i in range(len(reg_no_list)):
                slot_list.append(self.reg_no_slot_dict[reg_no_list[i]])
            slot_list.sort()
            print(slot_list, sep=", ")
        else:
            print("Not Found.")
        return

    def slot_no_from_reg_no(self, reg_no):
        """
        Prints slot number of the car with specified registration number

        Parameters
        ----------
        reg_no : str
        """
        if self.max_size == 0:
            print("Parking Lot not Created.")
            return
        slot_no = self.reg_no_slot_dict.get(reg_no, 0)
        if slot_no:
            print(slot_no)
        else:
            print("Not Found.")

    def reg_nos_from_age(self, driver_age):
        """
        Prints registration number of the cars with drivers age as specified

        Parameters
        ----------
        driver_age : int
        """
        if self.max_size == 0:
            print("Parking Lot not Created.")
            return
        reg_no_list = self.driver_age_slots_dict.get(driver_age, 0)
        if reg_no_list:
            print(reg_no_list, sep=", ")
        else:
            print("Not Found.")
