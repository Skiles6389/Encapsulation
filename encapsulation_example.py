class Cars:
    def _init_(self, make, model, year):
    #three attributes given to person class
        self.make = make
        self.model = model
        self.year = year
    #the _init_ method gets called when you create 
    #a new object in a class. It takes 4 parameters:
    #self, make, age, and gender...self refers to
    #the object itself and the other parameters are used
    #to initialize the attributes of the object
        def greet(self):
            print(f"Hello, my name is {self.name} and I am a {self.gender} person.")
            
Cars = Cars("Alice", 30, "female")
Cars.greet()
