
# Product selection
a = "game controller"
b = "gaming headset"
c = "gaming mouse"
print("Welcome to Arcade Game Shop!")
print("We have:")

cart = []
total = 0

while True:
    print("a - game controller: 250DH")
    print("b - gaming headset: 180DH")
    print("c - gaming mouse: 120DH")
    print("0 - nothing")

    # Chosse product
    d = input("Chosse your product: ")

    if d == "0":
        break

    while d != "a" and d != "b" and d != "c" and d != "0":
        print("Product not found")
        d = input("Chosse your product: ")

    if d == "a":
        unit_price = 250
        name = "game controller"
        print(f"You selected: {name}")

    elif d == "b":
        unit_price = 180
        name = "gaming headset"
        print(f"You selected: {name}")

    elif d == "c":
        unit_price = 120
        name = "gaming mouse"
        print(f"You selected: {name}")

    
    # Quantity of product
    quantity = int(input("Enter quantity: "))
    
    while quantity <= 0:
        print("Invalid quantity! Try again.")
        quantity = int(input("Enter quantity: "))
    

    product = quantity * unit_price

    print(f"You want {quantity} products?")
    e = input("(yes/no) : ")

    # Check the answer
    while e != "yes" and e != "no":
        print("What did you say? can you repeat?")
        e = input("(yes/no) : ")

    
    # yes to quantity
    if e == "yes":
        price = unit_price * quantity
        print(f"Your price is {product} DH ")


    # no to quantity
    elif e == "no":
        while e == "no":
            
                quantity = int(input("Enter quantity: "))
                while quantity <= 0:
                    print("Invalid quantity! Try again.")
                    quantity = int(input("Enter quantity: "))
                
                product = quantity * unit_price


                print(f"You want {quantity} products?")
                e = input("(yes/no) : ")
                

    
                while e != "yes" and e != "no":
                    print("What did you say? can you repeat? ")
                    e = input("(yes/no) : ")
            

            



    if d == "0":
        break

    cart.append(name)
    print(f"cart :{cart}")
    total += product
    print(f"Total is {total}DH")


if total > 0:

    print(f"Total is {total}DH")



    # membership card
    print("Do you have a membership card? ")
    f = input("(yes/no) : ")
    # Owning a membership card
    if f == "yes":
        print("A discount of 20 DH has been applied!")
        total = total - 20
        print(f"Your price after discount is {total} DH")

    # Not having a membership card
    else:
        print(f"So, your price is still {total} DH")
                
        



    # Calculating the tax value on the product (in French language)
    # TVA = Value Added Tax    
    print("TVA est 20%")
    TVA = total * 0.20
    print(f"TVA est {TVA} DH")


    # TTC = All Taxes Included 
    TTC = total + TVA
    print(f"Total price: {TTC} DH")


    # card or cash
    print("You want to pay with Credit card or Cash?")
    pay = input("card/cash : ")

    # Credit card
    if pay == "card":
        password = int(input("Enter your password: "))
        while password != 1234:
            print("Your password is incorrect. Try again")
            password = int(input("Enter your password: "))
        print("Thank you for shopping with us!")



    # Cash
    else:
        print(f"Your total price is {TTC} DH")
        money = int(input("Enter your money: "))

        # Cash > TTC
        if money > TTC:
            change = money - TTC
            print(f"This is your Change: {change}DH")
            print("Thank you for shopping with us!")


        elif money == TTC:
            print("Thank you for shopping with us!")


        # Cash < TTC
        else:
            print("sorry but your payment is not enough")
            remaining = TTC - money

            while remaining > 0:
                print(f"You still need to pay {remaining} DH")
                cash = int(input("Enter your money: "))
                money += cash
                remaining = TTC - money
                
            change = money - TTC
            print(f"This is your Change: {change}DH")
            print("Thank you for shopping with us!")

            


else:
    print("Goodbye")

        
