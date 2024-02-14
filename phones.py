from mobiles import Mobile, Apple, Samsung, Nothing,OnePlus,Mi


# Dataset
apple = (Apple("Apple", "iPhone 15", 76990, "512GB", 3348, 48, "Black", True, True),
        Apple("Apple", "iPhone 15 Pro", 184900, "1TB", 3274, 48, "Titanium Gold",True, True))

samsung = (Samsung("Samsung", "Galaxy S23 5G", 79999, "8GB 256GB", 3900, "Rose Gold",50, True, True),
           Samsung("Samsung", "Galaxy S23 Ultra 5G", 154990, "12GB 1TB", 5000, "Lavander",108, True, True))

nothing = (Nothing("Nothing", "Phone (1) 5G", 39999, "8GB 256GB", 4500, 50, "Black",True, True),
           Nothing("Nothing", "Phone (2) 5G", 49999, "12GB 512GB", 4700, 50, "white",True, True))

oneplus = (OnePlus("OnePlus", "11 5G", 61999, "16GB 256GB", 5000, 50, "Aqua",True, True),
           OnePlus("OnePlus", "11R 5G", 45999, "18GB 512GB", 5000, 50, "Pearl Green", True, True))

mi = (Mi("Redmi", "Note 13 Pro+", 30999, "16GB 512GB", 5000, 200, "Black",True, True),
    Mi("Xiaomi", "13 Pro 5G", 59999, "12GB 512GB", 4820, 50, "Orange",True, True),
    Mi("Xiaomi", "13 Ultra 5G", 69999, "16GB 1TB", 5000, 50, "White" ,True, True))

# smartphones in a list
smartphones = [apple, samsung, nothing, oneplus, mi]


# def phone_color(mobile,color):
#     mobile.color = color

# phone_color(apple, "Product(Red)")
# phone_color(samsung, "Pearl White")
# phone_color(nothing, "White")


# print(f"{apple.brand} {apple.model} is released on {apple.year}")
# print(f"It's available in {apple.color} color")


def iphone15():
    print()
    print("Specifications ")
    print()
    print(f"Brand: {apple[0].brand}")
    print(f"Model: {apple[0].model}")
    print(f"Color: {apple[0].color}")
    print(f"Variant: {apple[0].variant}")
    print(f"Battery: {apple[0].battery}mAh")
    print(f"Camera: {apple[0].camera}MP")
    print()
    apple[0].phone_isAvailable()
    print(f"Price: ₹{apple[0].price:,.2f}")
    apple[0].phone_discount()
    print()
def iphone15pro():
    print()
    print("Specifications ")
    print()
    print(f"Brand: {apple[1].brand}")
    print(f"Model: {apple[1].model}")
    print(f"Color: {apple[1].color}")
    print(f"Variant: {apple[1].variant}")
    print(f"Battery: {apple[1].battery}mAh")
    print(f"Camera: {apple[1].camera}MP")
    print()
    apple[1].phone_isAvailable()
    print(f"Price: ₹{apple[1].price:,.2f}")
    apple[1].phone_discount()
    print()

def samsungs23():
    print()
    print("Specifications ")
    print()
    print(f"Brand: {samsung[0].brand}")
    print(f"Model: {samsung[0].model}")
    print(f"Color: {samsung[0].color}")
    print(f"Variant: {samsung[0].variant}")
    print(f"Battery: {samsung[0].battery}mAh")
    print(f"Camera: {samsung[0].camera}MP")
    print()
    samsung[0].phone_isAvailable()
    print(f"Price: ₹{samsung[0].price:,.2f}")
    samsung[0].phone_discount()
    print()

def samsungs23ultra():
    print()
    print("Specifications ")
    print()
    print(f"Brand: {samsung[1].brand}")
    print(f"Model: {samsung[1].model}")
    print(f"Color: {samsung[1].color}")
    print(f"Variant: {samsung[1].variant}")
    print(f"Battery: {samsung[1].battery}mAh")
    print(f"Camera: {samsung[1].camera}MP")
    print()
    samsung[1].phone_isAvailable()
    print(f"Price: ₹{samsung[1].price:,.2f}")
    samsung[1].phone_discount()
    print()

def nothing1():
    print()
    print("Specifications ")
    print()
    print(f"Brand: {nothing[0].brand}")
    print(f"Model: {nothing[0].model}")
    print(f"Color: {nothing[0].color}")
    print(f"Variant: {nothing[0].variant}")
    print(f"Battery: {nothing[0].battery}mAh")
    print(f"Camera: {nothing[0].camera}MP")
    print()
    nothing[0].phone_isAvailable()
    print(f"Price: ₹{nothing[0].price:,.2f}")
    nothing[0].phone_discount()
    print()

def nothing2():
    print()
    print("Specifications ")
    print()
    print(f"Brand: {nothing[1].brand}")
    print(f"Model: {nothing[1].model}")
    print(f"Color: {nothing[1].color}")
    print(f"Variant: {nothing[1].variant}")
    print(f"Battery: {nothing[1].battery}mAh")
    print(f"Camera: {nothing[1].camera}MP")
    print()
    nothing[1].phone_isAvailable()
    print(f"Price: ₹{nothing[1].price:,.2f}")
    nothing[1].phone_discount()
    print()

def oneplus11():
    print()
    print("Specifications ")
    print()
    print(f"Brand: {oneplus[0].brand}")
    print(f"Model: {oneplus[0].model}")
    print(f"Color: {oneplus[0].color}")
    print(f"Variant: {oneplus[0].variant}")
    print(f"Battery: {oneplus[0].battery}mAh")
    print(f"Camera: {oneplus[0].camera}MP")
    print()
    oneplus[0].phone_isAvailable()
    print(f"Price: ₹{oneplus[0].price:,.2f}")
    oneplus[0].phone_discount()
    print()

def oneplus11r():
    print()
    print("Specifications ")
    print()
    print(f"Brand: {oneplus[1].brand}")
    print(f"Model: {oneplus[1].model}")
    print(f"Color: {oneplus[1].color}")
    print(f"Variant: {oneplus[1].variant}")
    print(f"Battery: {oneplus[1].battery}mAh")
    print(f"Camera: {oneplus[1].camera}MP")
    print()
    oneplus[1].phone_isAvailable()
    print(f"Price: ₹{oneplus[1].price:,.2f}")
    oneplus[1].phone_discount()
    print()
    
def redminote13pro():
    print()
    print("Specifications ")
    print()
    print(f"Brand: {mi[0].brand}")
    print(f"Model: {mi[0].model}")
    print(f"Color: {mi[0].color}")
    print(f"Variant: {mi[0].variant}")
    print(f"Battery: {mi[0].battery}mAh")
    print(f"Camera: {mi[0].camera}MP")
    print()
    mi[0].phone_isAvailable()
    print(f"Price: ₹{mi[0].price:,.2f}")
    mi[0].phone_discount()
    print()

def xiaomi13pro():
    print()
    print("Specifications ")
    print()
    print(f"Brand: {mi[1].brand}")
    print(f"Model: {mi[1].model}")
    print(f"Color: {mi[1].color}")
    print(f"Variant: {mi[1].variant}")
    print(f"Battery: {mi[1].battery}mAh")
    print(f"Camera: {mi[1].camera}MP")
    print()
    mi[1].phone_isAvailable()
    print(f"Price: ₹{mi[1].price:,.2f}")
    mi[1].phone_discount()
    print()

def xiaomi13ultra():
    print()
    print("Specifications ")
    print()
    print(f"Brand: {mi[2].brand}")
    print(f"Model: {mi[2].model}")
    print(f"Color: {mi[2].color}")
    print(f"Variant: {mi[2].variant}")
    print(f"Battery: {mi[2].battery}mAh")
    print(f"Camera: {mi[2].camera}MP")
    print()
    mi[2].phone_isAvailable()
    print(f"Price: ₹{mi[2].price:,.2f}")
    mi[2].phone_discount()
    print()




iphone15()
iphone15pro()

samsungs23()
samsungs23ultra()

nothing1()
nothing2()

oneplus11()
oneplus11r()

redminote13pro()
xiaomi13pro()
xiaomi13ultra()


