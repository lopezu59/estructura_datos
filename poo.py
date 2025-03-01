class Vehicle:
    
    brand = str
    model = str
    color = str  
    engine_displacement: int
    fuel = int
    wheels: int
    type = str
    
    
    
    def __init__(self, brand:str, fuel:int, type:str )-> None:
        self.brand = brand
        self.fuel = fuel
        self.type = type
    
    def __str__(self)->str:
        return f"The brand is: {self.brand}, and the level of Fuel is: {self.fuel}, also the type is: {self.type}"
    
    def turn_on(self):
        if self.fuel <= 10:
            return("The vehicle has low fule please refuel,")
        else:  
            return("The vehicle is ready to go,")
        
    def speed_up(self):
      while self.fuel > 0:
            self.fuel -= 1
            if self.fuel == 0:
                print("The vehicle has low fuel, please refuel. The vehicle has stopped.")
                break
            elif self.fuel <= 10:
                print(f"The vehicle is speeding up. Warning: Low fuel level ({self.fuel} units left).")
            else:
                print(f"The vehicle is speeding up. Fuel level: {self.fuel} units.")
            if self.fuel == 0:
                self.stop()
    
    def stop(self):
        print("The vehicle has stopped.")
    
    def turn_off(self):
        pass
    
class Motorcicle(Vehicle):
   pass
        
class Car(Vehicle):
   pass



Vehicle1 = Vehicle("Mazda", 20, "Unknown")
print(Vehicle1)
print(Vehicle1.turn_on(),Vehicle1.speed_up())   


moto1 = Motorcicle("Yamaha", 9, "Motorcicle")
print(moto1)
print(moto1.turn_on(),moto1.speed_up()) 

car1 = Car("Toyota", 29, "Car")
print(car1)
print(car1.turn_on(), car1.speed_up()) 
