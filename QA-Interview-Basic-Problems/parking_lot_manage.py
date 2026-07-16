class ParkingLot:
    def __init__(self,capacity):
        self.capacity = capacity

    parked = []
    count = 0

    def park_vehcile(self,reg_no, owner, vehicle_type):
        if self.parked <= self.capacity:
            self.parked.append(
                {
                    "reg_no" : reg_no,
                    "owner" : owner,
                    "vehicle_type" : vehicle_type
                }
            )
        else:
            print("No capacity")
        

    def remove_vechicle(self, reg_no):
        pass

    def search_vehicle(self, reg_no):
        pass

    def available_slot():
        pass

    def display_all_vehicle():
        pass


    if __name__=="__main__":

