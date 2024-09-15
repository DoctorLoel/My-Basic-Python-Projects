def validate_password(password):
    """
    Validate the password.
    :param password: str, the password to validate
    :return: bool, True if valid, otherwise False
    """
    # Your code here
    while True:
        print("Insert password/Press 0 to exit")
        print("_"*150)
        password1 = input()
        if password1 == "0":
            print(":)")
            break
        elif len(password1) < 8:
            print("Password too short")
        elif password1.islower():
            print("Must Contain atleast one upper case letter")
        elif password1.isalpha():
            print("Must contain atleast one digit")
        else:
            print("Password Correct")
            break
        
validate_password("password")