'''everything here is python is an object'''
'''comp=3+9j
print(type(comp))


----------------read a number----------------------
num=int(input("Enter a value"))
if(num%3==0):
    if(num%5==0):
        print("multiple of 3 and 5")
    else:
        print("multiple of 3")
elif(num%5==0):
    print("multiple of 5")
else:
    print("invalid number")


-------------odd,even-------------------
print("The number from 1 to 100")
for i in range(1,101):
    print(i,end=" ")
print("\nThe odd number from 1 to 100")
for i in range(1,101,2):
    print(i,end=" ")
print("\nThe even number from 1 to 100")
for i in range(2,101,2):
    print(i,end=" ")

---------------reverse even and odd--------------
print("The number from 100 to 1")
for i in range(100,1,-1):
    print(i,end=" ")
print("\nThe odd number from 1 to 100")
for i in range(100,1,-2):
    print(i,end=" ")
print("\nThe even number from 1 to 100")
for i in range(99,0,-2):
    print(i,end=" ")


---------------break------------------
for i in range(1,100):
    if(i==50):
        break
    print(i)


-----------------continue-----------------
for i in range(1,100):
    if(i==50):
        continue
    print(i,end=" ")



#pass is used when we want to write the empty statements

-------------------------functions-----------------------------
def fun1(n,m):
    sum1=n+float(m)
    return sum1
print(fun1(2.9,'4'))


 #catagories of function based on the agruments
--------------positional agruments----------------
def fun1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
fun1(10,100.4,"shruti",'97')


#-------------keyword argument--------------------
def fun1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
fun1(num4=10,num1=100.4,num3="shruti",num2='97')


#-------------default arguments--------------------
def fun3(name, roll,branch,col_name="GIET"):
    print(name, roll,branch,col_name)
fun3("sarthak",218,"CSE")

def fun3(name="ABC", roll,branch,col_name):
    print(name, roll,branch,col_name)
fun3(218,"CSE","GIET")  #this gives and error


#-------------Variable no of arguments-------------
def fun2(m,*args):
    for i in args:
        print(i,end=" ")

fun2(10,20)
print()
fun2(10,20,"m",50)



#------------------------problem1-------------------------
a=int(input())
b=int(input())
c=int(input())
if(a==7):
    print(b*c)
elif(b==7):
    print(c)
elif(c==7):
    print("-1")
else:
    print(a*b*c)


#-----------------------problem2----------------------------
inr=int(input("Amount you want"))
name=input("Country name please")
if(name=="Euro"):
    req=0.01417*inr
elif(name=="British Pound"):
    req=0.0100*inr
elif(name=="Australian Dollar"):
    req=0.02140*inr
elif(name=="Canadian Dollar"):
    req=0.02027*inr
else:
    print(-1)
print("required amount in ",req," in ",name)



#--------------------problem3-------------------------------
adult=int(input("enter number of adults"))
child=int(input("enter the number of children"))
cost=(adult*37550)+(37550/3)*child+(0.07*((adult*37550)+(37550/3)*child))-(0.1*((adult*37550)+(37550/3)*child+(0.07*((adult*37550)+(37550/3)*child))))
print(cost)

'''#-----------------problem4----------------------------------
def num_five(num5,req):
    if(req//5 <= num5):
        return (req//5)
    else:
        return 0

def num_one(num1,rest):
    if(rest//1 <= num1):
        return(rest//1)
    else:
        return 0

def num_coin(num5,num1,req):
    num_of_five=num_five(num5,req)
    rest=req-num_of_five*5
    num_of_one=num_one(num1,rest)
    if((num_of_five*5+num_of_one*1)!= req or (num_of_five==0 and num_of_one == 0)):
        print(-1)
    else:
        print(num_of_five)
        print(num_of_one)



num5=int(input())
num1=int(input())
req=int(input())
num_coin(num5,num1,req)



























