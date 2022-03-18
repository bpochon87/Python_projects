# Use a private attribute or function.
# Use a protected attribute or function.
# Create object that makes use of protected and private.

# Creating class Secret
class Secret():
    # Initializing attributes and methods of class Secret.
    def __init__(self):
        self.foo = 10
        self._protectedVar = 20
        self.__privateVar = 30

    # Changing original _protectedVar value from 20 to 21.
    def changeProtected(self):
        self._protectedVar = 21
        return self._protectedVar

    # Changing original __pritvateVar value from 20 to 21.
    def changePrivate(self):
        self.__privateVar = 31
        return self.__privateVar

# Instantiating an instance (object) of class Secret.
instance = Secret()




# Controlling flow of script.
if __name__ == "__main__":
    print(instance.foo)
    print(instance.changeProtected())
    print(instance.changePrivate())

    # __privateVar will not print directly as illustrated here.
    print(instance.__privateVar)
