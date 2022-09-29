def add(dict):
    
    item = input("What would you like to add to your shopping cart? ").lower()
    if item in dict:
        update = input(f'You already have {item} in your cart! Would you like to update the quanity? ').lower()
        if update == "yes":
            amount = input("New quanitity: ")
            dict[item] = amount
            print("Updated!")
        elif update == "no":
            print("Okay!")
        elif update != "yes" or update != "no":
            print("Sorry, try again.")
    else:
        quantity = input("How many would you like to add? ")
        dict[item] = quantity

def startMessage(dict):
    
    if len(dict.items()) == 0:
        command = input("**Empty Shopping Cart** add items with 'add' ")
    else:
        command = input("**Shopping Cart** You can 'show', 'add', 'delete', 'clear', or 'quit': ").lower()

    return command

def quit():
    
    response = input("Are you sure? You'll lose your entire cart. Type 'yes' or 'no': ").lower()
    if response == "yes":
        print("Sorry to see you go!")
    elif response == "no":
        print("Yes! Nice choice!")
    else:
        print("Sorry! try again")

    return response

def show(dict):
    
    for key, value in dict.items():
                print(f'{key}: {value}')

def delete(dict):
    
    for i in dict.items():
        print(i)
    grocery_to_delete = input("What would you like to delete from your cart? ")
    if grocery_to_delete not in dict.keys():
        print("Sorry, try again.")
    else:
        dict.pop(grocery_to_delete)
        print(f'{grocery_to_delete} deleted!')

def clear(dict):
    
    confirmation = input("Are you sure? Type 'yes' or 'no'. ").lower()
    if confirmation == "yes":
        dict.clear()
        print("Cart Cleared!")
    elif confirmation == "no":
        print("Good call.")
    else:
        print("Sorry, try again.")

# ---------- Main Body ----------

def shoppingCart():
    
    cart = {}

    commands = ["show", "add", "delete", "clear", "quit"]

    while True:

        command = startMessage(cart)
        
        if command not in commands:
            print(f'{command.title()} isn\'t a valid response! Try again.')
        elif command == "quit":
            if quit() == "yes":
                break
        elif command in commands and command != "add" and command != "quit" and len(cart.items()) == 0:
            print("You haven't added any items yet! Try adding first.")
        elif command == "add":
            add(cart)
        elif command == "show":
            show(cart)
        elif command == "delete":
            delete(cart)
        elif command == "clear":
            clear(cart)

shoppingCart()