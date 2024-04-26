"""
This file contains a Loger class, with some methods for registring and login into the app

Author: Tomás Cárdenas Benitez
"""

class Loger:
    def __init__(self):
        self.users = {}
    
    def register(self, username, password,utype):
        if username in self.users:
            print(f"{username} is already registered!")
        else:
            self.users[username] = {'password': password, 'type': utype}
            print(f"{username} succesfully registered!")

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Log in succesfully made")
        else:
            print("Username or password are typed incorrectly")