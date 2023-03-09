active = True
while active == True:
    
    age = input("How old are you? Type done when finished\n")
    if age == 'done':
        active = False
    else:
        age = int(age)

        if age < 3:
            ticket = 0
        elif age < 12:
            ticket = 10
        else:
            ticket = 15
        print(f'Your ticket will cost ${ticket}.')