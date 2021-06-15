# costructor
from typing import get_args


class User:
    total = 0
    def __init__(self,name,email,role) -> None:
        self.name = name
        self.email = email
        self.__role = role
        User.total += 1

    def info(self):
        return(f"{self.name} - {self.email} - {self.__role}")


    @property
    def getRole(self) :
        return self.__role

    @getRole.setter
    def getRole(self,newrole):
        if self.__role != "admin" :
            self.__role = newrole


    @classmethod
    def setTotal(cls,total) :
        cls.total = total

    @classmethod
    def setClass(cls,params) :
        name,email,role = params.split("-")
        return cls(name,email,role)
    

    @staticmethod
    def inistatic(word) :
        return word

print(User.inistatic("hallo ini statix"))










syukur = User("syukur beriman jaya lawolo","syukur@gmail.com","user")
params = ("briman - briman@gmail.com - user")
print(User.total)
User.setTotal(10)
print(User.total)


print("====set class method===\n")
stringPrint = User.setClass(params)
print(stringPrint)
# print(syukur.info())
# syukur.update_role("user")
# print(syukur.info())
# print(syukur.__dict__)
# print(syukur.getRole())

syukur.role = "moderator"
print(syukur.info())