current_users = ["peter", "hans", "dirk", "miles", "alex", "admin"]
new_users = ["peter", "Mike", "maggie", "John", "alex", "admin"]


# check for list content
if current_users and new_users:
    # run through the new users list
    for user in new_users:
        # check for availability of user name
        if user.lower() not in current_users: 
            # allow access
            print("Hello " + user.title() + ", welcome!");
            current_users.append(user.lower())
        else: 
            # deny access
            print("Hello " + user.title() + ", user name already take. Please choose a different one.")
else: 
    # empty lists
    print("No users wait for logging in.")

print("The following users are currently logged in: " + 
      str(current_users))        
print("eof")