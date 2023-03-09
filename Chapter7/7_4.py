prompt = "\nPlease enter pizza toppings you'd like on your pizza."
prompt += "\nType quit when you are finished.\n"

while True:
    topping = input(prompt)
    
    if topping == "quit":
        break
    else:
        print(f"Adding {topping} to your order.")