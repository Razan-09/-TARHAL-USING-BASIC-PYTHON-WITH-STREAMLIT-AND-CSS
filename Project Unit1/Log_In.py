class Authentication :
    def __init__(self):
        self.users={}
    def sign_up(self):
         email=input("Enter Your Email: ")
         username=input("Enter Your UserName: ")
         password=input("Enter Your Password:")
         #check if the email is vaild
         if"@" not in email or not email.endswith(".com"):
             print("Invalid email")
             return False
         #check if the username is already registered
         elif username in self.users:
             print("Warning! This username is already registered")
             return False
          #check if the password at least than 8 characters
         elif len(password) < 8:
             print("Warning! Password must be at least 8 characters long.")
             return False
         #save new user information
         else:
             self.users[username] = password
             print("Registration successful!")
             return True

    def login(self):
          username=input("Enter Your UserName: ")
          password=input("Enter Your Password:")
           #check the username and password
          if self.validate_user(username, password):
             print("Login successful!")
          else:
           print("Login invalid")
    def validate_user(self, username, password):
          if  username in self.users and password == self.users[username]:
                return True
          else:
               return False
               #allow login if Registration successful
auth = Authentication()

if auth.sign_up():
 auth.login()