class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def car_details(self):
        print(f"This is a {self.make} {self.model}, made in {self.year}.")
            
Car = Cars("Kia", "Carnival", "2022")
Car.car_details()
