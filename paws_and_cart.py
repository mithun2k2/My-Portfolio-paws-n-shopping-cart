carts = []
prices = []
# Display the user menu and cart until chekout
done = False
while (not done):
    print("\n")
    print("-"* 80)
    print("This is your shopping cart: ")
    print("-" * 80)
    print("Would you like to: ")
    print("1. Add an item to your cart: ")
    print("2. View cart: ")
    print("3. Remove an item from your cart: ")
    print("4. View the total cost of your cart")
    print("5. Checkout")
    choice = input("Enter the number of options you would like to choose:\n")
    if choice == "1":
        # Find out item and price and add it to the cart
        item = input("What item would you like to add in your cart: ")
        price = float(input("How much does the item cost: £"))
        carts.append(item)
        prices.append(price)
        print("{} has been added to your cart sucessfully.".format(item))
    elif choice == "2":
        print("This is what is in your shopping cart:")
        for i in range(len(carts)):
            print(f"{carts[i]} - £{prices[i]}")
        user = input("Press Enter to continue")
    elif choice == "3":
        # Find item that must be removed and check that it is in the cart
        remove = input("Which item would you like to remove: ")
        if remove in carts:
            # Remove items from cart and pricelist
            index = carts.index(remove)
            carts.pop(index)
            prices.pop(index)
            print("{} has been removed from cart successfully".format(remove))

        else:
            print(f"{remove} is not in your cart")
    elif choice == "4":
        if len(carts) == 0:
            print("Your cart is empty.")
        else:
            total_price = sum(prices)
            print(f"Total price: £{total_price:.2f}")
            useer = input("Press Enter to continue")
    elif choice == "5":
        # Exit from the program
        print("Thank you for shopping with paws and cart!")
    else:
        print("This is not a valid option.")