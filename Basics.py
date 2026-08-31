trys = 3
password = input("Create your password: ")
while len(password) < 8:
    password = input("The password must be minimum 8 caracters, retry: ")
cpassword = input("Confirm your password: ")
while password != cpassword:
    cpassword = input("Those passwords are not the same, retry: ")
login = input("Now you have to log-in,you have 3 try, use the password: ")
while login != password and trys > 1:
    trys = trys -1
    login = input(f"To log-in, you have to enter the password you set, you have {trys} try left: ")
    if trys == 0:
        print("Too many errors, you can't try anymore.")