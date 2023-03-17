#----------------------problem1-----------------------------
#wecare company, 2 types of vehicles,(id,type,cost,premium),
#2%for two-wheelers, 6% of four-wheelers
#display premium amount and details
'''class WeCare:
    def __init__(self,vid,vtype,vcost):
        self.__vid=vid
        self.__vtype=vtype
        self.__vcost=vcost
        self.__prem=None
    def premium_cal(self,__vcost):
        if(self.__vtype=="twowheelers"):
            self.__prem=self.__vcost*0.02
        elif(self.__vtype=="fourwheelers"):
            self.__prem=self.__vcost*0.06
    def display(self):
        print("car-id",self.__vid)
        print("car-type",self.__vtype)
        print("car-cost",self.__vcost)
        print("car-premium-amount",self.__prem)
    def get_id(self):
        return self.__vid
    def set_id(self,new_id):
        self.__vid=new_id

typev=input("Enter the car type")
if(typev not in ["twowheelers" ,"fourwheelers"]):
    print("Invalid Car Type")
    exit()
costv=int(input("Enter the car cost"))
idv=input("Enter the car id")
obj1=WeCare(idv,typev,costv)
obj1.premium_cal(costv)
obj1.display()
print("Id:",obj1.get_id())
obj1.set_id("OR083491")
print(obj1.get_id())
'''

#-------------------------problem2----------------------------
#student(id(age&mark valid,mark->65 or more),age(>20),mark(0-100))
'''class Student:
    def __init__(self,sid,age,mark):
        self.__id=sid
        self.__age=age
        self.__mark=mark
    def validitate_age(self):
        if(self.__age>20):
            return True
        else:
            return False
    def validitate_mark(self):
        if(self.__mark>=0 and self.__mark<=100):
            return True
        else:
            return False
    def check_qualification(self):
        if(obj1.validitate_age() and obj1.validitate_mark()):
            return True
        else:
            return False
    def get_sid(self):
        return self.__id
    def get_age(self):
        return self.__age
    def get_mark(self):
        return self.__mark
    def set_sid(self,new_id):
        self.__id=new_id
    def set_age(self,new_age):
        self.__age=new_age
    def set_mark(self,new_mark):
        self.__mark=new_mark
    def admission(self):
        cid=int(input("Enter a course"))
        if(cid==1001):
            if(obj1.get_mark()>=85):
                fees=25575-(25575*0.25)
            else:
                fees=25575
            print(fees)
        elif(cid==1002):
            if(obj1.get_mark()>=85):
                fees=15500-(15500*0.25)
            else:
                fees=15500
            print(fees)
        else:
            print("Invalid Course")
        
print("Hello! Welcome")
sid=input("Enter the ID")
age=int(input("Enter the age"))
mark=int(input("Enter the mark in entrance exam"))
obj1=Student(sid,age,mark)
print("Validatiting...")
if(obj1.check_qualification()):
    print("Validation Passed")
    if(obj1.get_mark()>=65):
        obj1.admission()
    else:
        print("Better Luck Next Time")
else:
    print("Error Data. Please check and enter")
    print("Details",obj1.get_sid()," ",obj1.get_mark(),
          " ",obj1.get_age())
    sid=input("Re-enter the ID")
    age=int(input("Re-enter the age"))
    mark=int(input("Re-enter the mark in enterance exam"))
    obj1.set_sid(sid)
    obj1.set_mark(mark)
    obj1.set_age(age)
    if(obj1.check_qualification()):
        print("Validation Passed")
        if(obj1.get_mark()>=65):
            obj1.admission()
        else:
            print("Better Luck Next Time")

'''
#-------------------------problem3-------------------------
#customer can collect or opt for delivery
#pizza delivery system
'''
class Pizzaservice:
    def validate_pizza_type(self):
        if(self.ptype in ["small","medium"]):
            return True
        else:
            print("Invalid choice")
            exit()
    def calculate_pizza_cost(self):
        if(self.validate_pizza_type()):
            if(self.ptype=="small" and self.add_topp==True):
                self.cost=(150*self.qnty)+(35*self.qnty)
            elif(self.ptype=="small" and self.add_topp==False):
                self.cost=150*self.qnty
            elif(self.ptype=="medium" and self.add_topp==True):
                self.cost=(200*self.qnty)+(50*self.qnty)
            else:
                self.cost=200*self.qnty
        return(self.cost)

class Customer(Pizzaservice):
    def __init__(self,ptype,qnty,topp):
        self.ptype=ptype
        self.qnty=qnty
        self.add_topp=topp
        self.cost=None
        
    def validate_quantity(self,qnty):
        if(self.qnty>=1 and self.qnty<=5):
            return True
        else:
            print("Invalid choice")
            exit()

class DoorDelivery(Customer):
    def __init__(self,ptype,qnty,topp,dist):
        self.ptype=ptype
        self.qnty=qnty
        self.add_topp=topp
        self.cost=0
        self.dist=dist
        
    def validate_distance_in_kms(self):
        if(self.dist>=1 and self.dist<=10):
            return True
        else:
            print("Invalid choice")
            exit()
    def calculate_pizza_costd(self,dist):
        if(obj2.validate_distance_in_kms()):
            if(self.dist<=5):
                self.cost=self.cost+5
            else:
                self.cost+=7
        else:
            print("Out Of Service Range")
        return self.cost

print("Hi All! Choose the service in number")
print("1>Order Only")
print("2>Home Delivery")
ch=int(input())
ptype=input("Enter Pizza Type")
quantity=int(input("Enter Pizza Quantity"))
topp=bool(input("Topping? Enter True for yes and False for No"))
if(ch==1):
    obj1=Customer(ptype,quantity,topp)
    print("Validating")
    if(obj1.validate_quantity(obj1.qnty)):
        print(obj1.calculate_pizza_cost())
elif(ch==2):
    dist=int(input("Enter the distance"))
    obj2=DoorDelivery(ptype,quantity,topp,dist)
    if(obj2.validate_quantity(obj2.qnty)):
        print(obj2.calculate_pizza_cost()+obj2.calculate_pizza_costd(obj2.dist))
           
else:
    print("Invalid choice")

'''























