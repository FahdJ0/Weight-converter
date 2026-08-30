password = input("Enter a password: ")
while len(password) < 8:
    print("The password contains less than 8 caracters, rewrite one.")
    password = input("Enter a longer password: ")

cpassword = input("The password you wrote is valid, confirm it: ")
while cpassword != password:
    cpassword = input("The second password is the same as the first one, retry: ")
print("You comfirmed your password right")  