
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats() == 0: 
            return False
        self.passengers.append(name)
        return True


    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)


people = ["Sai", "Ganesh", "Veeravalli", "Daniel"]

for a in people:
    success = flight.add_passenger(a)

    if success:
        print("Added", a, "to flight successfully")

    else:
        print("No available seats for", a)
