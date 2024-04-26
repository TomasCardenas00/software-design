"""
This file contains a Processor class, with some methods for registering all the actions made by the users

Author: Tomás Cárdenas Benitez
"""

import datetime


class Processor():
    def __init__(self,name):
        self.name = name

    def login(self):
        return f"User: {self.name} - Action: Login - Time: {datetime.now}"
        
    def register(self):
        return f"User: {self.name} - Action: Register - Time: {datetime.now}"

    def vehicle_search(self):
        return f"User: {self.name} - Action: Searched for a Vehicle - Time: {datetime.now}"

    def vehicle_classification(self):
        return f"User: {self.name} - Action: Classified vehichles - Time: {datetime.now}"

    def vehicle_modification(self):
        return f"User: {self.name} - Action: Modified a Vehicle - Time: {datetime.now}"
    
    def vehicle_addition(self):
        return f"User: {self.name} - Action: Added a Vehicle - Time: {datetime.now}"
    
    def vehicle_elimination(self):
        return f"User: {self.name} - Action: Deleted a Vehicle - Time: {datetime.now}"
    
    def exit(self):
        return f"User: {self.name} - Action: Exited - Time: {datetime.now}"

    def add_to_log(self, message):
        file_ = open("actionlog.txt","a")
        file_.write("\n"+message)
        file_.close