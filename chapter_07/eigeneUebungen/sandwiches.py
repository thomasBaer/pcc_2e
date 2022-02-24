sandwich_orders = ['tuna', 'tuna', 'ham', 'pastrami', 'egg', 'salmon', 'pastrami', 'ham', 'ham', 'pastrami', 'egg']
finished_sandwiches = []

flag = True

print(sandwich_orders)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
if 'pastrami' not in sandwich_orders:
    print ("Unfortunatly pastrami sandwiches are out.")

while flag:
    sandwich_order = input("Please give me your sandwich order (or enter done): ")
    if sandwich_order == 'done':
        break
    
    sandwich_orders.append(sandwich_order)

while sandwich_orders:
    sandwich_in_progress = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_in_progress)
    print("I made you a " + sandwich_in_progress + " sandwich.")
    
print(finished_sandwiches)



