from abc import ABC, abstractmethod

class Mobile(ABC):
    
    year = 2023

    @abstractmethod
    def __init__ (self, brand , model, price, variant, battery, camera, 
                  color,status, discount):
        self.brand = brand
        self.model = model
        self.price = price
        self.variant = variant
        self.battery = battery
        self.camera = camera
        self.color = color
        self.status = status
        self.discount = discount



class Apple(Mobile):
    
     # superclass constructor
        def __init__(self, brand, model, price, variant, battery, camera, color,status, discount):
            super().__init__(brand, model, price, variant, battery, camera, color,status, discount)
        
        # overriding the phone_isAvailable() method
        def phone_isAvailable(self):
            if self.status == True:
                print(f"It is Available in sale!")
            else:
                print(f"Currently not Available for sale!")
            return self
    
        # overriding the phone_price() method
        def phone_price(self):
            print(f"The {self.brand} {self.model} is priced at ₹{self.price:,.2f}")
            return self
        
        # overriding the phone_discount() method
        def phone_discount(self):
            discounted = self.price - (self.price * 0.25 / 100)
            if self.status == True:
                if self.discount == True:
                    print(f"Discounted price at ₹{discounted:,.2f}")
            elif self.status == False:
                print("But, it has discount of 25% once it is available for sale!")
            return self


class Samsung(Mobile):

     # superclass constructor
        def __init__(self, brand, model, price, variant, battery, camera, color ,status, discount):
            super().__init__(brand, model, price, variant, battery, camera, color,status, discount)
        
        # overriding the phone_isAvailable() method
        def phone_isAvailable(self):
            if self.status == True:
                print(f"It is Available in sale!")
            else:
                print(f"Currently not Available for sale!")
            return self
    
        # overriding the phone_price() method
        def phone_price(self):
            print(f"The {self.brand} {self.model} is priced at ₹{self.price:,.2f}")
            return self
        
        # overriding the phone_discount() method
        def phone_discount(self):
            discounted = self.price - (self.price * 0.25 / 100)
            if self.status == True:
                if self.discount == True:
                    print(f"Discounted price at ₹{discounted:,.2f}")
            elif self.status == False:
                print("But, it has discount of 25% once it is available for sale!")
            return self


class Nothing(Mobile):
    
         # superclass constructor
        def __init__(self, brand, model, price, variant, battery, camera, color ,status, discount):
            super().__init__(brand, model, price, variant, battery, camera, color,status, discount)
        
        # overriding the phone_isAvailable() method
        def phone_isAvailable(self):
            if self.status == True:
                print(f"It is Available in sale!")
            else:
                print(f"Currently not Available for sale!")
            return self
    
        # overriding the phone_price() method
        def phone_price(self):
            print(f"The {self.brand} {self.model} is priced at ₹{self.price:,.2f}")
            return self
        
        # overriding the phone_discount() method
        def phone_discount(self):
            discounted = self.price - (self.price * 0.25 / 100)
            if self.status == True:
                if self.discount == True:
                    print(f"Discounted price at ₹{discounted:,.2f}")
            elif self.status == False:
                print("But, it has discount of 25% once it is available for sale!")
            return self

class OnePlus(Mobile):
    
         # superclass constructor
        def __init__(self, brand, model, price, variant, battery, camera, color ,status, discount):
            super().__init__(brand, model, price, variant, battery, camera, color,status, discount)
        
        # overriding the phone_isAvailable() method
        def phone_isAvailable(self):
            if self.status == True:
                print(f"It is Available in sale!")
            else:
                print(f"Currently not Available for sale!")
            return self
    
        # overriding the phone_price() method
        def phone_price(self):
            print(f"The {self.brand} {self.model} is priced at ₹{self.price:,.2f}")
            return self
        
        # overriding the phone_discount() method
        def phone_discount(self):
            discounted = self.price - (self.price * 0.25 / 100)
            if self.status == True:
                if self.discount == True:
                    print(f"Discounted price at ₹{discounted:,.2f}")
            elif self.status == False:
                print("But, it has discount of 25% once it is available for sale!")
            return self
        
class Mi(Mobile):
    
         # superclass constructor
        def __init__(self, brand, model, price, variant, battery, camera, color ,status, discount):
            super().__init__(brand, model, price, variant, battery, camera, color,status, discount)
        
        # overriding the phone_isAvailable() method
        def phone_isAvailable(self):
            if self.status == True:
                print(f"It is Available in sale!")
            else:
                print(f"Currently not Available for sale!")
            return self
    
        # overriding the phone_price() method
        def phone_price(self):
            print(f"The {self.brand} {self.model} is priced at ₹{self.price:,.2f}")
            return self
        
        # overriding the phone_discount() method
        def phone_discount(self):
            discounted = self.price - (self.price * 0.25 / 100)
            if self.status == True:
                if self.discount == True:
                    print(f"Discounted price at ₹{discounted:,.2f}")
            elif self.status == False:
                print("But, it has discount of 25% once it is available for sale!")
            return self
  





# app = Apple("Apple", "iPhone 15", 76990, "256GB", 3815, 12, False, True)
# app.phone_isAvailable()


         






    

