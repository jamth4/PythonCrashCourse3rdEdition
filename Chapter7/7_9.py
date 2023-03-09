sandwich_orders = ['italian', 'pastrami', 'turkey', 'pastrami', 'ham', 'chicken', 'pastrami', 'club']
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    
    print(f"I made a {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)