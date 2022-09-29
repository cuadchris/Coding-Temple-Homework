def shoppingCart():
    
    cart = {}

    commands = ["show", "add", "delete", "clear", "quit"]

    while True:
        
        if len(cart.items()) == 0:
            command = input("**Empty Shopping Cart** add items with 'add' ")
        else:
            command = input("**Shopping Cart** You can 'show', 'add', 'delete', 'clear', or 'quit': ").lower()

        if command not in commands:
            print(f'{command.title()} isn\'t a valid response! Try again.')
        if command == "quit":
            response = input("Are you sure? You'll lose your entire cart. Type 'yes' or 'no': ").lower()
            if response == "yes":
                print("Sorry to see you go!")
                break
            elif response == "no":
                print("Yes! Nice choice!")
            else:
                print("Sorry! try again")
        elif command in commands and command != "add" and command != "quit" and len(cart.items()) == 0:
            print("You haven't added any items yet! Try adding first.")
        elif command == "add":
            item = input("What would you like to add to your shopping cart? ").lower()
            if item in cart:
                update = input(f'You already have {item} in your cart! Would you like to update the quanity? ').lower()
                if update == "yes":
                    amount = input("New quanitity: ")
                    cart[item] = amount
                    print("Updated!")
                elif update == "no":
                    print("Okay!")
                elif update != "yes" or update != "no":
                    print("Sorry, try again.")
            else:
                quantity = input("How many would you like to add? ")
                cart[item] = quantity
        elif command == "show":
            for key, value in cart.items():
                print(f'{key}: {value}')
        elif command == "delete":
            for i in cart.items():
                print(i)
            grocery_to_delete = input("What would you like to delete from your cart? ")
            if grocery_to_delete not in cart.keys():
                print("Sorry, try again.")
            else:
                cart.pop(grocery_to_delete)
                print(f'{grocery_to_delete} deleted!')
        elif command == "clear":
            confirmation = input("Are you sure? Type 'yes' or 'no'. ").lower()
            if confirmation == "yes":
                cart.clear()
                print("Cart Cleared!")
            elif confirmation == "no":
                print("Good call.")
            else:
                print("Sorry, try again.")

shoppingCart()