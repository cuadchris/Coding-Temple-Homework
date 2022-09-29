shopping_cart = {}

commands = ["show", "add", "delete", "clear", "quit"]
# command = input("What would you like to do? You can type 'show', 'add', 'delete', 'clear', or 'Quit': ").lower()
# size = len(shopping_cart.items())


while True:
    
    size = len(shopping_cart.items())
    command = input("*Shopping Cart* You can type 'show', 'add', 'delete', 'clear', or 'Quit': ").lower()

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
    elif command in commands and command != "add" and command != "quit" and size == 0:
        print("You haven't added any items yet! Try adding first.")
    elif command == "add":
        item = input("What would you like to add to your shopping cart? ")
        if item in shopping_cart:
            update = (f'You already have {item} in your cart! Would you like to update the quanity?').lower()
            if update == "yes":
                amount = input("New quanitity: ")
                shopping_cart[item] = amount
                print("Updated!")
            elif update == "no":
                print("Okay!")
            else:
                print("Sorry, try again")
        quantity = input("How many would you like to add? ")
        shopping_cart[item] = quantity
    elif command == "show":
        for i in shopping_cart.items():
            print(i)
    elif command == "delete":
        for i in shopping_cart.items():
            print(i)
        grocery_to_delete = input("What would you like to delete from your cart? ")
        if grocery_to_delete not in shopping_cart.keys():
            print("Sorry, try again.")
        else:
            shopping_cart.pop(grocery_to_delete)
            print(f'{grocery_to_delete} deleted!')
    elif command == "clear":
        confirmation = input("Are you sure? Type 'yes' or 'no'. ").lower()
        if confirmation == "yes":
            shopping_cart.clear()
            print("Cart Cleared!")
        elif confirmation == "no":
            print("Good call.")
        else:
            print("Sorry, try again.")