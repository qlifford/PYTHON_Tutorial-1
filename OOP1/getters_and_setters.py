# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password
        
# user1 = User("cliff", "cliff@cliff.com", "123")
# print(user1.email)
# user1.email = "456"
# print(user1.email)


class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
        
    @property   
    def email(self):
        return self._email
    
    @email.setter   
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            raise ValueError ("Invalid Email!")
        
user1 = User("cliff", "cliff@cliff.com", "123")
print(user1.username)
# print(user1.email())
# user1.email = ("commms")
# print(user1._email)
user1._email = "glory@glory.koy"
print(user1._email)