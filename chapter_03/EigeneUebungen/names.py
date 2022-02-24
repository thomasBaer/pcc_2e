myFriends = ['peter', 'klaus', 'hans']
myFriends.insert(0, 'walter')
myFriends.append('markus')

print("Ah, " + myFriends.pop(0).title() + " is this really you?")

for i in myFriends:
    print("Hello " + i.title()+ ", nice to see you.")
    
    