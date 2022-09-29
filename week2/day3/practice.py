shopping_cart = {}

commands = ["show", "add", "delete", "clear", "quit"]
# command = input("What would you like to do? You can type 'show', 'add', 'delete', 'clear', or 'Quit': ").lower()
# size = len(shopping_cart.items())


while True:
    
    size = len(shopping_cart.items())
    command = input("What would you like to do? You can type 'show', 'add', 'delete', 'clear', or 'Quit': ").lower()

    if command not in commands:
        print(f'{command.title()} isn\'t a valid response! Try again.')
    elif command != "add" and size == 0:
        print("You haven't added any items yet! Try adding first.")
    elif command == "add":
        item = input("What would you like to add to your shopping cart? ")
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