'''---------------------List---------------------------------
list1=[]
print(list1,type(list1))
list1.extend([1,2,4,75,6.7])
print(list1)
del list1[0]
print(list1)


#-----------------------problem1-----------------------------

def count_sen(s):
    l,d=0,0
    for i in s:
        if(i.isalpha()):
            l+=1
        elif(i.isdigit()):
            d+=1
        else:
            pass
    list1=[]
    list1.extend([l,d])
    return list1

str1=input("enter the sentence")
print("The number of letters and digits are ",count_sen(str1))


#------------------------problem2----------------------------

def find_pair_of_numbers(l1,sum1):
    c=0
    for i in range(0,len(l1)):
        for j in range(i+1,len(l1)):
            if(l1[i]+l1[j] == sum1):
                c+=1
                break
            else:
                continue
    if(c==0):
        return 0
    else:
        return c

l1=[int(i) for i in input().split()]
sum1=int(input())
print(find_pair_of_numbers(l1,sum1))


#--------------------------problem3-----------------------------

def str_con(s1):
    if(len(s1)<2):
        return -1
    else:
        s2=""
        s2=s2+s1[0:2]
        s2=s2+s1[len(s1)-2:]
        return s2
        
str1=input("enter the string")
print(str_con(str1))   


#-----------------------problem4---------------------------------

def str_change(s1):
    s2="ing"
    if(len(s1)<3):
        return s1
    elif(s1[-3:] == s2):
        return s1+"ly"
    else:
        return s1+"ing"

s1=input()
print(str_change(s1))


#---------------------problem5----------------------------------
def check_double(n1):
    dou=n1*2
    n1=str(n1)
    dou=str(dou)
    if(len(n1) == len(dou)):
        for i in n1:
            if(i in dou and n1.index(i) != dou.index(i)):
                return True
            else:
                return False
    else:
        return False

n1=int(input())
print(check_double(n1))


#---------------------problem6-----------------------------------


def find_more_than_average(t1):
    sum1,c=0,0
    for i in t1:
        sum1=sum1+i
        avg=sum1/10
    for i in t1:
        if(i>=avg):
            c+=1
    per=(c/10)*100
    return per

def freq(t1):
    l1=[]
    for i in range(0,26):
        l1.append(t1.count(i))
    return l1

def sort_tuple(t1):
    t2=list(t1)
    t2.sort()
    return t2
    
t1=tuple(map(int,input().split()))
print(find_more_than_average(t1))
print(freq(t1))
print(sort_tuple(t1))

#-----------------------problem7-------------------------------

def translate(d1,str1):
    l1=[]
    for i in str1:
        l1.append(d1[i])
    return l1

d1={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
str1=[i for i in input().split()]
print(translate(d1,str1))


-----------------------problem8(list slicing)--------------------------------

start=int(input())
end=int(input())
l1=list()
for i in range(start,end+1):
    l1.append(i)
l2=[]
for i in range(len(l1)):
    for j in range(i,len(l1)):
        l2.append(l1[i:j+1])
print(l2)
            
'''
def chunk(l1,n1):
    l2=[]
    for i in range(0,len(l1),n1):
        for j in range(n1):
            l2=[l1[i:i+n1]]
            print(l2)
            break
n1=int(input())
l1=list(map(int,input().split()))
n1=int(input())
























