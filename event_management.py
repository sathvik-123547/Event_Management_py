class Locker:
    def __init__(self, code):
        self.__code = code
    
    def change_code(self, current_code, new_code):
        # Check if the provided current code matches the locker code
        if current_code == self.__code:
            # Update the code if the match is successful
            self.__code = new_code
            print("Code successfully changed.")
        else:
            print("Current code is incorrect.")
    
    def unlock(self, code):
        # Check if the provided code matches the locker code
        if code == self.__code:
            print("Locker unlocked!")
        else:
            print("Incorrect code. Locker remains locked.")
            

# Creating a Locker object with an initial code
my_locker = Locker("2134")

# Changing the locker code from "2134" to "1933"
my_locker.change_code("2134", "1933")

# Unlocking the locker with the new code "1933"
my_locker.unlock("1933")
