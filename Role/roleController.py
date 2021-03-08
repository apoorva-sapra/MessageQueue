import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Role.role import Role

class RoleController :
    roleObject = ""

    def initializeRole(self):
        self.roleObject = Role()

    def takeInputFromUser(self):
        print("Please choose the role \n")
        while True:
            try:
                userInput = int(input("\nPlease press 1 for Publisher \nPlease press 2 for Subscriber"))
            except:
                print("Please enter valid input!")
                continue
            else:
                if(userInput != 1 or 2):
                    print("Please enter 1 or 2")
                    continue
                return userInput
