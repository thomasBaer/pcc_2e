users = ["peter", "hans", "dirk", "miles", "alex", "admin"]
#users = []
users.sort()

if users:
    for user in users:
        if user == "admin":
            print("Hello " + user.title() + ", would you like to see the status report?")
        else:
            print("Hello " + user.title() + ", thank you for logging in again.")
else: 
    print("No users wait for logging in.")
        
print("eof")