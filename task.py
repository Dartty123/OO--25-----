class Car:
    type = "Car"

    def __init__(self,electricity: float):
        print("Call __init__ method")
        self.electricity = electricity

    def drive(self):
        print(f"{self.type}: Машина їде ->")
        self.electricity -= 5.0

class Tesla(Car):
    type = "Tesla"

    def headlights(self):
        print(f"{self.type} turn on the light")

    def drive(self):
        print(f"{self.type}: Машина їде з включеним світлом->")
        self.electricity -= 9.8

class BmwElectric(Car):
    type = "BmwElectric"

    def headlights(self):
        print(f"{self.type} turn on the light")

    def drive(self):
        print(f"{self.type}: Машина їде з включеним світлом->")
        self.electricity -= 8.4

tesla = Tesla(100)
bmw = BmwElectric(100)

print (f" {Tesla.type}: Заряд: '{tesla.electricity}' % " )
tesla.drive
print (f" {Tesla.type}: Заряд: '{tesla.electricity}' % " )