from mobiles import Mobile, Apple, Samsung, Nothing, OnePlus, Mi
# from phones import iphone, galaxy, nothin, plusone, xioami

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



# Main Program starts here
print()
print("\u001b[35m" + "---------------------------------------" + "\u001b[1m")
print("\u001b[31m" + "         Welcome to buykart            " + "\u001b[1m")
print("\u001b[32m" + "We have the following products in stock" + "\u001b[1m")
print("\u001b[35m" + "---------------------------------------" + "\u001b[1m")

print()
print("\u001b[37m")


def main_menu():

    mainmenu = ["Smartphones", "Computer Peripherals", "Gaming Consoles", "Accessories"]
    for i, menus in enumerate(mainmenu, start=1):
        print(f"{i}: {menus}")
    while True:
        try:
            menu = int(input("Select a category(Products) or (q)to quit : "))
            if menu == 1 :
                while True:
                    print()
                    # print("=======================================")
                    print()
                    print("List of smart Smartphone Brands available: ")
                    print("-------------------------------------------")
                    print()
                    for smartphone in smartphones:
                        print(smartphone[0].brand)
                    print()
                    Brand_select = str(input("Enter Smartphone Brand to view the products: ")).lower()
                    print()
                    print("=======================================")

                    for smartphone in smartphones:
                        if Brand_select == smartphone[0].brand.lower():
                            for i,mobile in enumerate(smartphone,start=1):
                                print(f"{i}: {mobile.brand} {mobile.model}")
                    
                    print()
                    print("=======================================")   

                    Prod_select = int(input("Select a product (1 or2): "))
                    print()
                    print("=======================================")
                    if Prod_select == 1:
                        print("Specifications ")
                        print(f"Brand: {apple[0].brand}")
                        print(f"Model: {apple[0].model}")
                        print(f"Variant: {apple[0].variant}")
                        print(f"Battery: {apple[0].battery}mAh")
                        print(f"Camera: {apple[0].camera}MP")
                        print()
                        apple[0].phone_isAvailable()
                        print(f"Price: ₹{apple[0].price:,.2f}")
                        apple[0].phone_discount()
                        print()
                        print("=======================================")
                        print()
                        print("[1: Add to cart] [2: Buy Now] [3: Main Menu]",end="")
                        optn_select = int(input(" "))
                        if optn_select == 1:
                            print("")
                            print("==============")
                            print("Added to cart")
                            print("==============")
                        elif optn_select == 2:
                            print("===========================================")
                            print("You have successfully purchased the product")
                            print("===========================================")
                        elif optn_select == 3:
                            main_menu()

                    elif Prod_select == 2:
                        print("Specifications ")
                        print()
                        print(f"Brand: {apple[1].brand}")
                        print(f"Model: {apple[1].model}")
                        print(f"Variant: {apple[1].variant}")
                        print(f"Battery: {apple[1].battery}mAh")
                        print(f"Camera: {apple[1].camera}MP")
                        print()
                        apple[1].phone_isAvailable()
                        print(f"Price: ₹{apple[1].price:,.2f}")
                        apple[1].phone_discount()
                        print()
                        print("=======================================")
                        print()
                        print("[1: Add to cart] [2: Buy Now] [3: Main Menu]",end="")
                        optn_select = int(input(" "))
                        if optn_select == 1:
                            print("")
                            print("==============")
                            print("Added to cart")
                            print("==============")
                            
                        elif optn_select == 2:
                            print("===========================================")
                            print("You have successfully purchased the product")
                            print("===========================================")
                            break
                        elif optn_select == 3:
                            main_menu()
            elif menu == 2:
                print()
                print("Electronics: coming soon...")
                print()
            elif menu == 3:
                print()
                print("Laptops: coming soon...")
                print()
            elif menu == 4:
                print()
                print("Accessories: coming soon...")
                print()
            elif menu >=5 and menu <= 10:
                print(f"Oops! It's not a valid input. Please try again...")
                print()
           
        except ValueError:
            print(f"Oops! It's not a valid input. Please try again...")
            print()
        # menu = int(input("Select a category(Products) or (q) to Quit : "))
        # if menu == 1:
            # while True:
            #     print()
            #     # print("=======================================")
            #     print()
            #     print("List of smart Smartphone Brands available: ")
            #     print("-------------------------------------------")
            #     print()
            #     for smartphone in smartphones:
            #         print(smartphone[0].brand)
            #     print()
            #     Brand_select = str(input("Enter Smartphone Brand to view the products: ")).lower()
            #     print()
            #     print("=======================================")

            #     for smartphone in smartphones:
            #         if Brand_select == smartphone[0].brand.lower():
            #             for i,mobile in enumerate(smartphone,start=1):
            #                 print(f"{i}: {mobile.brand} {mobile.model}")
                
            #     print()
            #     print("=======================================")   

            #     Prod_select = int(input("Select a product (1 or2): "))
            #     print()
            #     print("=======================================")
            #     if Prod_select == 1:
            #         print("Specifications ")
            #         print(f"Brand: {apple[0].brand}")
            #         print(f"Model: {apple[0].model}")
            #         print(f"Variant: {apple[0].variant}")
            #         print(f"Battery: {apple[0].battery}mAh")
            #         print(f"Camera: {apple[0].camera}MP")
            #         print()
            #         apple[0].phone_isAvailable()
            #         print(f"Price: ₹{apple[0].price:,.2f}")
            #         apple[0].phone_discount()
            #         print()
            #         print("=======================================")
            #         print()
            #         print("[1: Add to cart] [2: Buy Now] [3: Main Menu]",end="")
            #         optn_select = int(input(" "))
            #         if optn_select == 1:
            #             print("")
            #             print("==============")
            #             print("Added to cart")
            #             print("==============")
            #         elif optn_select == 2:
            #             print("===========================================")
            #             print("You have successfully purchased the product")
            #             print("===========================================")
            #         elif optn_select == 3:
            #             main_menu()

            #     elif Prod_select == 2:
            #         print("Specifications ")
            #         print(f"Brand: {apple[1].brand}")
            #         print(f"Model: {apple[1].model}")
            #         print(f"Variant: {apple[1].variant}")
            #         print(f"Battery: {apple[1].battery}mAh")
            #         print(f"Camera: {apple[1].camera}MP")
            #         print()
            #         apple[1].phone_isAvailable()
            #         print(f"Price: ₹{apple[1].price:,.2f}")
            #         apple[1].phone_discount()
            #         print()
            #         print("=======================================")
            #         print()
            #         print("[1: Add to cart] [2: Buy Now] [3: Main Menu]",end="")
            #         optn_select = int(input(" "))
            #         if optn_select == 1:
            #             print("")
            #             print("==============")
            #             print("Added to cart")
            #             print("==============")
                        
            #         elif optn_select == 2:
            #             print("===========================================")
            #             print("You have successfully purchased the product")
            #             print("===========================================")
            #             break
            #         elif optn_select == 3:
            #             main_menu()
            #     elif menu == 2:
            #         print()
            #         print("Electronics: coming soon...")
            #         print()
            #     elif menu == 3:
            #         print()
            #         print("Laptops: coming soon...")
            #         print()
            #     elif menu == 4:
            #         print()
            #         print("Accessories: coming soon...")
            #         print()
            #     elif menu >=5 and menu <= 10:
            #         print(f"Oops! It's not a valid input. Please try again...")
            #         print()
            #     if menu.lower() == "q":
            #         print("Thank you for visiting buykart")
            #         break
        
                    
            


            # optn_select = int(input("[1: Add to cart] [2: Buy Now] [3: Main Menu] "))
            # if optn_select == 3:
                
            # other options...
    # other menus...

if __name__ == "__main__":
    main_menu()




