class Person:

    def init(self, CIN, Fname, Lname, tel=[]):
        self.Fname = Fname
        self.Lname = Lname
        self.CIN = CIN
        self.__tel = tel

    def get_tel(self):
        return self.__tel
    
    def get_CIN(self):
        return self.CIN
    
    def get_Fname(self):
        return self.Fname
    
    def get_Lname(self):
        return self.Lname
    
    def tel(self, value):
        if not value.isdigit():
            raise ValueError("tel have digits")
        if len(value)< 8:
            raise ValueError("tel is very small")
        self.__tel.append(value) 

    def display(self):
        print(f"Person CIN: {self.CIN}, Name: {self.Fname} {self.Lname}, Telephone numbers: {', '.join(self.tel)}")

class account :

    __NBaccounts = 0

    def __init__(self, owner ):
        self.owner = owner
        self.balance = 0
        account.__NBaccounts += 1
        self.code = account.__NBaccounts
    
    def get_balance (self):
        return self.balance
    
    def get_code (self):
        return self.code
    
    def get_owner (self):
        return self.owner
    
    def credit (self , amount):
        if amount <= 0 :
            raise ValueError ("amount must be positive ")
        self.balance += amount

    def credit_from (self , amount , account):
        if amount <= 0 :
            raise ValueError (" amount must be positive")
        if account.balance <amount :
            raise ValueError ("insufficient balance")
        self.balance -= amount
    
    def debit_to (self , amount , account):
        if amount <= 0 :
            raise ValueError ("amount must be positive")
        if self.balance < amount
            raise ValueError ("insufficient balance")
        self.balance -= amount
        account.balance += amount  

    def display (self)
        print (f"account code : {self.code}")
        print (f"pwner {self.owner.Fname} {self.awner.lname}")
        print (f"balance {self.balance}")
    @staticmethod
    def displayNBaccounts() :
        print(f"total number of accounts created is : {account.__NBaccounts}")




p1 = person("1234" , "said" , "krimil" , ["0540303244"])
a1 = account (p1)
a1.credit(6000)
a1.display()
account.displayNBaccounts()
    




    
    
