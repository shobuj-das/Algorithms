class ParkingLot:
    def __init__(self,capacity):
        self.capacity = capacity

    parked = 0
    
    def park_vehcile(self,reg_no, owner, vehicle_type):
        if self.parked <= self.capacity:
            self.registration_number = reg_no
            self.owner_name = owner
            self.park_vehcile = vehicle_type

    def remove_vechicle(self, reg_no):
        pass

    def search_vehicle(self, reg_no):
        pass

    def available_slot():
        pass

    def display_all_vehicle():
        pass


    if __name__=="__main__":

