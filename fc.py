# # Sample user data
# users = {
#     "user1": "Roshan",
#     "user2": "Roshan",
#     "user3": "Roshan"
# }

# def login():
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")

#     if username in users and users[username] == password:
#         print("Login successful!")
#     else:
#         print("Invalid username or password. Please try again.")

# if __name__ == "__main__":
#     login()


# username='Roshan',
# confirmname='Roshan'

username=input('enter the username: ')
confirmname=input('enter the name again: ')



if username == confirmname:
       print('this is right name',confirmname)
else:
       print('wrong name')
