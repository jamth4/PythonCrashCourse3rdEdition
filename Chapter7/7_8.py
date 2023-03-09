sandwich_orders = ['italian', 'turkey', 'ham', 'club']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    
    print(f"I mande a {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)
    
