#------------------problem1---------------------------------
'''class OverDraw(Exception):
    pass

class LimitReached(Exception):
    pass
    
class Customer:
    def __init__(self,cust_id,cust_name,cust_age,cust_ac):
        self.__cid=cust_id
        self.__name=cust_name
        self.__age=cust_age
        self.__ac=cust_ac
    def withdraw(self,amount):
        try:
            if(amount>obj2.get_balance()):
                raise OverDraw
        except OverDraw:
            print("OverDraw")
            self.take_card()
            exit()
        obj2.set_balance(obj2.get_balance()-amount)
    def take_card(self):
        print("Take Card Out From The ATM")
    def get_customer_id(self):
        return self.__cid
    def get_customer_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_account(self):
        return self.__ac
    
class Account:
    def __init__(self,acc_type,balance,min_bal):
        self.__atype=acc_type
        self.__balance=balance
        self.__min_balance=min_bal
    def get_account_type(self):
        return self.__atype
    def get_balance(self):
        return self.__balance
    def get_min_balance(self):
        return self.__min_balance
    def set_balance(self,x):
        self.__balance=x
        
class PrivilegedCustomer(Customer):
    def __init__(self,cid,name,age,bonus):
        self.__cid=cid
        self.__name=name
        self.__age=age
        self.__bonus_points=bonus
    def increase_bonus(self):
        if(obj2.get_balance() >1000):
            obj2.__bonus_points+=10
        else:
            self.__bonus_points+=2
    def withdraw(self,amount):
        super().withdraw(amount)
        self.increase_bonus()
    def get_bonus_points(self):
        return self.__bonus_points
    
obj1=PrivilegedCustomer(100,"Gopal",43,100)
obj2=Account("Savings",1000,500)
amt=int(input("Enter the amount to be withdrawn"))
obj1.withdraw(amt)
print("Customer Balance",obj2.get_balance())
print("Customer bonus",obj1.get_bonus_points())
try:
    if(obj2.get_balance()<obj2.get_min_balance()):
        raise LimitReached
except LimitReached:
    print("LimitReached")
    obj1.take_card()
    exit()
        
obj1.take_card()

'''

        









































        
