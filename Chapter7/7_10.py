vacations = {}
poll = True

while poll:
    user = input("What is your name? ")
    vacation = input("Where would you like to go on a dream vacation? ")
    
    vacations[user] = vacation
    
    repeat = input("Would someone else like to respond? (yes/no)")
    if repeat == "no":
        poll = False
        
for user, vacation in vacations.items():
    print(f"{user} would like to go to {vacation} on a dream vacation.")
    
