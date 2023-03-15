'''#list comprehension
result=[i for i in range(1,10)]
print(result)

#using condition in list comprehension
result=[i for i in range(0,10) if(i%2!=0)]
print(result)

result=[i if(i%2!=0) else i**2 for i in range(0,9)]
print(result)

#list comprehension for two loops
mat=[[1,2,3],[4,5,6],[7,8,9]]
result=[mat[i][j]**2 if(mat[i][j]%2!=0) else mat[i][j]**3
        for i in range(0,len(mat))
        for j in range(0,len(mat[0]))]
print(result)

mat=[[1,2,3],[4,5,6],[7,8,9]]
l2=[]
for i in range(0,len(mat)):
    l3=[]
    for j in range(0,len(mat[0])):
        if(mat[i][j]%2!=0):
            l3.append(mat[i][j]**2)
        else:
            l3.append(mat[i][j]**3)
    l2.append(l3)
print(l2)

#in list comprehension method
print([[mat[i][j]**2 if(mat[i][j]%2!=0) else mat[i][j]**3
        for i in range(0,len(mat))
        for j in range(0,len(mat[0]))]for i in range(0,len(mat))])


#--------------------------problem1----------------------------
 #mylist[9,3,6,1,5,0,8,2,4,7]
#list_b[6,4,6,1,2,2]
#o/p: result=[(6,2),(4,8)]

mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result=[(i,mylist.index(i)) for i in list_b]
print(result)


#-----------------------problem2-------------------------------
#tokenizing by removing stop words
sent=["a new world record was set","in the holy city of ayodhya",
      "on the eve of diwali on tuesday",
      "with over three lakh diya or earthen lamps",
      "lit up simultaneously on the banks of the sarayu river"]
stopwords=["for","a","of","the","and","to","in","on","with","was"]


result=[]
for i in sent:
    l1=i.split(" ")
    l2=[]
    for j in l1:
        if(j not in stopwords):
            l2.append(j)
    result.append(" ".join(l2))

print(result)

OR

print([" ".join([j for j in i.split(" ") if(j not in stopwords)])
          for i in sent])

#-----------------------problem3--------------------------------
#3,2,6,5,1,4,8,9
#num1=3+2+6+9=20
#num2=5148
#o/p=5148+20=5168

str1=list(map(int,input().split(",")))
sum1=0
str2=""
for i in range(0,str1.index(5)):
    sum1+=str1[i]
for i in range(str1.index(8)+1,len(str1)):
    sum1+=str1[i]
for i in range(str1.index(5),str1.index(8)+1):
    str2+=str(str1[i])
print(sum1+int(str2))


#OR

str1=list(map(int,input().split(",")))
sum1=0
str2=""
for i in range(len(str1)):
    if(i<str1.index(5)or i >str1.index(8)):
        sum1+=str1[i]
    else:
        str2+=str(str1[i])
print(sum1+int(str2))


#-------------------------problem4----------------------------
#246:rhdt, 1246:rhftd
#2*2+4*4+6*6=even so trhd
str1=list(input().split(":"))
str2=str1[0]
num=str1[1]
sum1=0
str3=""
for i in num:
    sum1+=int(i)*int(i)
if(sum1%2==0):
    str3+=(str2[-1]+str2[:len(str2)-1])
else:
    str3+=(str2[-3:-1]+str2[-1]+str2[0:len(str2)-3])
print(str3)

'''
#--------------------problem5---------------------------
#sum of largest prime factor of cosecutive n numbers from n

def check_prime(m):
    c=0
    for i in range(m,0,-1):
        if(m%i==0):
            c+=1
    if(c==2):
        return True
    else:
        return False
        

def prime(num):
    large=0
    for i in range(2,num+1):
        if(check_prime(i) and num%i==0 and i>=large):
            large=i
    return large      



n=int(input())
sum1=0
for i in range(n,n+9):
    sum1+=prime(i)
print(sum1)













































