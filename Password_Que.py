password = input("enter a number")
if len(password)<=6 or len(password)>=16 and "$" in password and "2" in password or "8" in password and "A" in password or "Z" in password:
    print("Strong password")
else:
    print("weak password")

