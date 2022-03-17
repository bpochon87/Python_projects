""" Practice with parent and child classes """

# Parent class Member
class Member:
    def __init__(self, name, phoneNumber, email):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email

    def welcomeMsg(self):
        msg = "{} is a new member! You may contact them at {} or {}.".format(self.name, self.phoneNumber, self.email)
        return msg


# Child class aaMember and its attributes
class AAmember(Member):
    # Initializing attributes for AAmember class.
    def __init__(self, name, phoneNumber, email, sponsor, yearsSober):
        # super().__init__ brings in all attributes and methods from parent (Member) class.
        super().__init__(name, phoneNumber, email)
        # Adding the two new attributes for AAmember class.
        self.sponsor = sponsor
        self.yearsSober = yearsSober

        # Polymorphising the parent (Member) class welcomeMsg.
    def welcomeMsg(self):
        msg = ("Let's welcome {}! Congratulations on {} year(s) sober. You may "
        "contact them at {} or {}. They have {} sponsor.\n").format(self.name, self.yearsSober,
                                                                self.phoneNumber, self.email, self.sponsor)
        return msg

# Setting new member of class AAmember to variable.
newAAmember = AAmember("Brady", "308-280-0070", "bpochon@gmail.com", "no", "6.5")

        
# Child class naMember
class NAmember(Member):
    # Initializing attributes for NAmember class.
    def __init__(self, name, phoneNumber, email, sponsor, yearsClean, freeFrom):
        # super().__init__ brings in all attributes and methods from parent (Member) class.
        super().__init__(name, phoneNumber, email)
        # Adding the three new attributes for NAmember class.
        self.sponsor = sponsor
        self.yearsClean = yearsClean
        self.freeFrom = freeFrom

    # Polymorphising the parent (Member) class welcomeMsg.
    def welcomeMsg(self):
        msg = ("Way to go on {} year(s) clean from {}, {}! Contact them at {} or {}. "
               "They have {} sponsor.\n").format(self.yearsClean, self.freeFrom, self.name, self.phoneNumber,
                                               self.email, self.sponsor)
        return msg

# Setting new member of class NAmember to variable.
newNAmember = NAmember("Sara", "402-490-0819", "sara.meidlinger@gmail.com", "a", "1", "marijuana")

# If this script is the main module, execute the following.
if __name__ == "__main__":
    print(newAAmember.welcomeMsg())
    print(newNAmember.welcomeMsg())
