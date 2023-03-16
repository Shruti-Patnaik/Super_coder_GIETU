'''#--------------------problem1--------------------------------
#nearest palindrome on a number
import sys
def nearest_palindrome(num):
    for i in range(num+1,sys.maxsize):
        if(str(i)==str(i)[::-1]):
            return i
        
num=int(input())
print(nearest_palindrome(num))
        
#----------------------problem2-------------------------------
d1={"P":"pediatrics","O":"orthopedics","E":"ENT"}
l1=list(map(str,input().split(" ")))
spe=""
c=0
for i in d1.keys():
    if(l1.count(i)>c):
        c=l1.count(i)
        spe=i
print(d1[spe])


#-----------------------problem3-------------------------------
str1=input()
str2=input()
str3=""
for i in range(0,len(str1)):
    if(str1[i] != " "):
        for j in range(0,len(str2)):
            if(str1[i] == str2[j]):
                str3+=str1[i]
                break
print(str3)


#---------------------OOPS concept----------------------------------
#1
class employee:
    def __init__(self):
        self.id=None
    def check_eligibility(self):
        if(self.id >=9000 and self.id<=10000):
            print("Eligible")
        else:
            print("not eligible")

obj1=employee()
obj1.id=10000
#print(obj1)---> prints the address where the obj is created
obj1.check_eligibility()
obj2=employee()
obj2.id=4000
obj2.check_eligibility()

#2
class example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
o1=example(10)
print(o1.get_num())
o1.set_num(15)
print(o1.get_num())

#####OUTPUT#####
10
15

class example:
    def __init__(self,num):
        num=100
o=example()
print(o.num)
########OUTPUT##########
#error

class example:
    def __init__(self,num):
        self.num=num
o=example(200)
print(o.num)
####OUTPUT#######
#200

#3
class shoes:
    def __init__(self,price,material):
        self.price=price
        self.material=material

sl=shoes(1000,"canvas")
print("the value is",id(sl))

#######OUTPUT#########
#the value is 3080979274992

class shoes:
    def __init__(self,price,material):
        self.price=price
        self.material=material

    def __str__(self):
        return "shoe with price "+str(self.price)+"and material is "+str(self.material)
    

sl=shoes(1000,"canvas")
print(sl)

#####OUTPUT###
#shoe with price 1000and material is canvas
#the default behaviour of print is changes by converting the
#hexadecimal address into a string format


class mobile:
    def display(self):
        print("display purchase")
    def purchase(self):
        self.display()
        print("calculating price")

mobile().purchase()

###OUTPUT####
#display purchase
#calculating price
#object is created but not initialized to any variable

class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.total_price=None
        self.ret_mon=None
    def return_money(self):
        self.ret_mon=self.price-self.total_price
        print(self.ret_mon)
    def purchase(self):
        if(self.brand=="Apple"):
            discount=10
        else:
            discount=5
        self.total_price=self.price-self.price*(discount/100)
        print(self.total_price)
        self.return_money()
    

m1=mobile("Apple",20000)
m1.purchase()

####OUTPUT###
#18000.0
#2000.0


class customer:
    def __init__(self,cid,name,age,bal):
        self.cid=cid
        self.name=name
        self.age=age
        self.__bal=bal#private
    def update(self,amt):
        if(amt<1000):
            self.__bal+=amt
    def display(self):
         return(self.__bal)
c1=customer(100,"Gopal",24,1000)
c1.update(500)
#print(c1.__bal) -->gives error as the private cannot be
                    #accessed from outside the class

print(c1.display())# --->accessing the private attibute

##correcting the error
class dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def len_disp(self):
        return self.__length
d1=dam("ABC dam",3.5)
print("the name:",d1.name)
print("the name:",d1.len_disp())



'''
class table:
    def __init__(self):
        print(id(self))
        self.legs=4
        self.glass=None
        self.wooden=None
din_tab=table()
back_tab=table()
front_tab=back_tab
print(din_tab,id(back_tab),id(front_tab))






























































































