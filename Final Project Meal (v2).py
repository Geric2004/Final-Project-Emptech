#T-STEM-11G Pair #6
#Eser, German III, S.
#Gaerlan, Paolo Miguel

#Initialize Variables Needed
done = False
#Variables below are initialized so that when there are no inputs in any of them, the program can still continue without crashing
main = ""
mainChoice = ""
mainPrice = 0
mainQuantity = 0
mainTotal = 0
side = ""
sidePrice = 0
sideQuantity = 0
sideTotal = 0
sideChoice = ""
drink = ""
drinkPrice = 0
drinkQuantity = 0
drinkTotal = 0
drinkChoice = ""
discount = 0
discounted = 0


#Main program while loop
while (done == False):
    print("Welcome! Please select an option! \n[1] Mains \n[2] Sides \n[3] Drinks \n[4] Check out \n[5] Exit \nNote: One can only order one dish per each kind of food \n and selecting a dish option overrides the selection.")
    choice = input("\nWhich option would you select? ")  
    #while choice is not "1", "2", "3", or "4" then keep asking the user to enter a correct input
    while (choice not in ["1", "2", "3", "4", "5"]):
        print("\nInvalid Input! Please only input: 1, 2, 3, 4, or 5!")
        choice = input("Which option would you select?")
    
    #If statement for main
    if (choice == "1"):
        print("You have selected mains. Here are the following choices) \n[1] Steak ₱ 900 \n[2] Salmon ₱ 850 \n[3] Chicken ₱ 300 \n[4] Cancel")
        mainChoice = input("Which dish would you like? ")
        #If user inputs "1" main is set to "Steak", as well as the price and quantity for that main is also set
        if (mainChoice == "1"):
            main = "Steak"
            mainPrice = 900
            mainQuantity = int(input("How many would you like? "))
        #If user inputs "2" main is set to "Salmon", as well as the price and quantity for that main is also set    
        elif (mainChoice == "2"):
            main = "Salmon"
            mainPrice = 850
            mainQuantity = int(input("How many would you like? "))
        #If user inputs "3" main is set to "Chicken", as well as the price and quantity for that main is also set
        elif (mainChoice == "3"):
            main = "Chicken"
            mainPrice = 300
            mainQuantity = int(input("How many would you like? "))
        #If user inputs "4", choice is canceled
        elif (mainChoice == "4"):
            print("\nChoice Canceled!\n")
        mainTotal = round(mainPrice * mainQuantity, 2)
    #If statement for side
    if (choice == "2"):
        print("\nYou have selected sides. Here are the following choices: \n[1] Baked Potato ₱ 80 \n[2] Mashed Potato ₱ 75 \n[3] Steamed Vegetables ₱ 50 \n[4] Cancel")
        sideChoice = input("Which dish would you like? ")
        #If user inputs "1" side is set to "Baked Potato", as well as the price and quantity for that side is also set
        if (sideChoice == "1"):
            side = "Baked Potato"
            sidePrice = 80
            sideQuantity = int(input("How many would you like? "))
            
        #If user inputs "3" side is set to "Mashed Potato", as well as the price and quantity for that side is also set
        elif (sideChoice == "2"):
            side = "Mashed Potato"
            sidePrice = 75
            sideQuantity = int(input("How many would you like? "))
        #If user inputs "3" side is set to "Steamed Vegetables Potato", as well as the price and quantity for that side is also set
        elif (sideChoice == "3"):
            side = "Steamed Vegetables"
            sidePrice = 50
            sideQuantity = int(input("How many would you like? "))
        #If user inputs "4", choice is canceled
        elif (sideChoice == "4"):
            print("\nChoice Canceled!\n")
        sideTotal = sidePrice * sideQuantity
    #If statement for drink
    if (choice == "3"):
        print("\nYou have selected drinks. Here are the following choices: \n[1] Ice Tea ₱ 55 \n[2] Root Beer ₱ 60 \n[3] Water ₱ 20 \n[4] Cancel")
        drinkChoice = input("Which dish would you like? ")
        #If user inputs "1" side is set to "Ice Tea", as well as the price and quantity for that drink is also set
        if (drinkChoice == "1"):
            drink = "Ice Tea"
            drinkPrice = 55
            drinkQuantity = int(input("How many would you like? "))
        #If user inputs "2" side is set to "Root Beer", as well as the price and quantity for that drink is also set
        elif (drinkChoice == "2"):
            drink = "Root Beer"
            drinkPrice = 60
            drinkQuantity = int(input("How many would you like? "))
        #If user inputs "3" side is set to "Water", as well as the price and quantity for that drink is also set
        elif (drinkChoice == "3"):
            drink = "Water"
            drinkPrice = 20
            drinkQuantity = int(input("How many would you like? "))
        #If user inputs "4", choice is canceled
        elif (drinkChoice == "4"):
            print("\nChoice Canceled!\n")
        drinkTotal = drinkPrice *  drinkQuantity
    #If Statement for Checkout
    if (choice == "4"):
        #Prints price breakdown
        print("\nMain - ", main, "- ₱", mainPrice, "x", mainQuantity, "= ₱", mainTotal)
        print("Side - ", side, "- ₱", sidePrice, "x", sideQuantity, "= ₱", sideTotal)
        print("Drink - ", drink, "- ₱", drinkPrice, "x", drinkQuantity, "= ₱", drinkTotal)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        total = float(mainTotal + sideTotal + drinkTotal)
        print("\nTOTAL: ₱", "{:.2f}".format(total, 2))
        #Takes payment input
        payment = int(input("Enter amount to be paid: ₱ "))
        
        #if the input is insufficient, keep asking the user to enter an amount that is more than the total
        while(payment < total):
            print("Insufficient Funds!")
            payment = int(input("Enter amount to be paid: ₱ "))

        #If combo 1 is selected, 10% discount is given
        if (mainChoice == "3" and sideChoice == "2" and drinkChoice == "1"):
            print("Chicken Mash Tea Combo gives 10% discount.")
            discount = total * 0.10
            discounted = total - discount
            change = payment - discounted
        #if combo 2 is selected, 15% discount is given
        elif (mainChoice == "1" and sideChoice == "3" and drinkChoice == "2"):
            print("Steak Veg Beer gives 15% discount.")
            discount = total * 0.15
            discounted = total - discount
            change = payment - discounted
        #if no combo is chose, no discount is given
        else:
            change = payment - total
        #prinkts discount, discounted price, and change with 2 decimal places
        print("DISCOUNT: ₱", "{:.2f}".format(discount, 2))
        print("DISCOUNTED: ₱","{:.2f}".format(discounted, 2))
        print("CHANGE: ₱", "{:.2f}".format(change, 2))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        #Clears all variables as not to conflict with the next transaction
        main = ""
        mainPrice = 0
        mainQuantity = 0
        mainTotal = 0
        side = ""
        sidePrice = 0
        sideQuantity = 0
        sideTotal = 0
        drink = ""
        drinkPrice = 0
        drinkQuantity = 0
        drinkTotal = 0
        discount = 0
    
    #If user chooses 5, sets done to true to stop while loop
    if (choice == "5"):
        done = True
