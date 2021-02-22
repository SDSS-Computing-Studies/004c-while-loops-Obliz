##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""
username = ""
password = ""

username = input("What is your username?")
password = input("What is your password?" )
if username == "admin":
 print("What is your password")
 if password == "12345" :
  print("Access granted")
if password != "12345" :
    print ("Access Denied")

if password != ("12345"):
    print ("you are locked out, Good Bye.")