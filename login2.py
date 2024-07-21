def login():
    # Predefined username and password
    valid_username = "admin"
    valid_password = "password"
    
    # Prompt user for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Check credentials
    if username == valid_username and password == valid_password:
        print("Login successful!")
    else:
        print("Invalid username or password")

# Run the login function
login()
