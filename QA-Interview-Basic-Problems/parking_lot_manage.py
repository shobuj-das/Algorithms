class ParkingLot:
    def __init__(self,capacity):
        self.capacity = capacity
        self.parked = []
        self.count = 0
        self.open_slots: list = [0] * capacity
        

    def remove_vechicle(self, reg_no):
        flag = False
        for vehicle in self.parked:
            if vehicle["reg_no"] == reg_no:
                self.open_slots[vehicle["slot"]-1] = 0
                self.parked.remove(vehicle)
                self.count -= 1
                print("Vehicle removed")
                break
        if not flag:
            print("Vehicle not found")

    def search_vehicle(self, reg_no):
        flag = False
        for vehicle in self.parked:
            if vehicle["reg_no"] == reg_no:
                flag = True
                break
        return flag

    def available_slots(self):
        slot = 0
        self.current_slots = []
        for i in self.open_slots:
            if i == 0:
                self.current_slots.append((slot+1))
            slot += 1

        return self.current_slots
        
    def get_a_slot(self):
        slot = 0
        for i in self.open_slots:
            if i == 0:
                return (slot + 1)
            slot += 1

    def display_all_vehicle(self):
        if len(self.parked)>0:
            for vehicle in self.parked:
                print(vehicle)
        else:
            print("No vehicle found")

    def park_vehicle(self,reg_no, owner, vehicle_type):
        if self.count < self.capacity:
            if not self.search_vehicle(reg_no=reg_no):
                slot_no = self.get_a_slot()
                self.parked.append(
                    {   
                        "slot" : slot_no,
                        "reg_no" : reg_no,
                        "owner" : owner,
                        "vehicle_type" : vehicle_type
                    }
                )
                print(f"Added vehicle to slot {slot_no}")
                self.open_slots[slot_no - 1] = 1
                self.count += 1
            else:
                print("Vehicle already exist")
        else:
            print("No capacity")


if __name__=="__main__":
    park = ParkingLot(3)

    park.park_vehicle("DHK-101", "Shobuj", "Car")
    park.park_vehicle("DHK-102", "Shobuj", "Bike")
    park.park_vehicle("DHK-103", "Shobuj", "Bus")

    print(park.available_slots())

    print(park.search_vehicle("DHK-102"))
    park.display_all_vehicle()
    park.park_vehicle("DHK-104", "Shobuj", "Bus")
    park.display_all_vehicle()
    print(park.available_slots())

    park.remove_vechicle("DHK-101")
    print(park.available_slots())

    park.park_vehicle("DHK-1040", "Shobuj", "Bus")
    park.park_vehicle("DHK-1004", "Shobuj", "Bus")