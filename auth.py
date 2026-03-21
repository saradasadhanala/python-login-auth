import hashlib

class AuthSystem:

    def __init__(self,filename):
        self.filename = filename
#TODO: upgrade password hashing to bcrypt
    def hash_password(self,password):
        hashed = hashlib.md5(password.encode()).hexdigest()
        return hashed

    def register(self,username,password):
        try:

            with open(self.filename,"r") as file:
                for line in file:
                    if ',' not in line:
                        continue
                    stored_username,_ = line.strip().split(",")
                    if stored_username == username:
                        print("User already exist")
                        return
        except FileNotFoundError:
            pass
        hashed_password = self.hash_password(password)
        with open(self.filename,"a") as file:
            file.write(username + "," + hashed_password + "\n")
        print("User registered successfully")

    def login(self,username,password):

        hashed_password = self.hash_password(password)
        
        try:
            with open(self.filename,"r") as file:
                for line in file:
                    if ',' not in line:
                        continue
                    stored_user,stored_password = line.strip().split(",")
                    if stored_user == username and stored_password == hashed_password:
                        print("Login successfull")
                        return True
        except FileNotFoundError:
            print("No users registered yet")
            return False
        print("Invalid username or password")
        return False

