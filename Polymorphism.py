class Vehicle:
    def move(self):
        pass

class Toyota(Vehicle):
    def move(self):
        print("The Toyota drives smoothly with excellent fuel efficiency. 🚗")

class BMW(Vehicle):
    def move(self):
        print("The BMW offers a luxurious driving experience with powerful performance. 🚘")

class Nissan(Vehicle):
    def move(self):
        print("The Nissan is known for its innovative technology and reliability. 🚙")


vehicles = [Toyota(), BMW(), Nissan()]
for vehicle in vehicles:
    vehicle.move()