#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
username = ""
password = ""

username = input("What is your username?")
password = input("What is your password?" )
if username == "admin":
 print("What is your passsword")

 if password == "12345"
 print("Access granted")
