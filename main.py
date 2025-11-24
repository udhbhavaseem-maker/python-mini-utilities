from random import *

def factorial():
    i=int(input("Enter number : "))
    s=1
    for i in range (1,i+1):
        s=s*i
    print("The Factorial of",i,"is",s)

def prime():
    i=int(input("Enter number to be checked : "))
    for j in range(2,i):
        if i%j==0:
            print("The number is not prime ")
            break
    else:
        print("The number is prime")
def calculator():
    i=int(input("Enter first number : " ))
    j=int(input("Enter second number : "))
    print("The available operators are +,-,*,/")
    k=input("Enter operator : ")
    if k=="+":
        print(i+j)
    elif k=="-":
        print(i-j)
    elif k=="*":
        print(i*j)
    elif k=="/":
        print(i/j)
    else:
        print("Invalid operator")
def armstrong():
    i=int(input("Enter number : "))
    m=i
    q=i
    s=0
    t=0
    while i>0:
        i=i//10
        s=s+1
    while m>0:
        n=m%10
        t=t+n**s
        m=m//10
    if t==q:
        print("The number is armstrong.")
    else:
        print("The number is not armstrong.")
def perfectsquare():
    i=int(input("Enter number : "))
    r=int(i**0.5)
    if r*r==i:
        print("The number is perfect square.")
    else:
        print("The number is not perfect square.")
def palindrome():
    i=int(input("Enter number : "))
    b=str(i)
    c=b[::-1]
    if c==b:
        print("The number is palindrome.")
    else:
        print("The number is not palindrome.")
def baseconversion():
    i=int(input("Enter number "))
    print("Type 1 for binary conversion,2 for octal conversion,3 for hexa-decimal conversion.")
    b=int(input("Enter your choice : "))
    if b==1:
        print(bin(i))
    elif b==2:
        print(oct(i))
    elif b==3:
        print(hex(i))
    else:
        print("Invalid choice")
def lcm():
    i=int(input("Enter first number : "))
    j=int(input("Enter second number : "))
    if i>j:
        grt=i
    else:
        grt=j
    while True:
        if grt%i==0 and grt%j==0:
            lcm=grt
            break
        grt=grt+1
    print("The lcm of two numbers : ",lcm)
def hcf():
    i=int(input("Enter first number : "))
    j=int(input("Enter second number : "))
    if i<j:
        sml=i
    else:
        sml=j
    hcf=1
    for k in range(1,sml+1):
        if i%k==0 and j%k==0:
            hcf=k
    print("The hcf of two numbers : ",hcf)
def fibonacci():
    i=int(input("Enter number : "))
    a,b=0,1
    while a<=i:
        print(a,end=" ")
        a,b=b,a+b
def perfectnumber():
    n=int(input("Enter number : "))
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if s==n:
        print("The number is a perfect number.")
    else:
        print("The number is not a perfect number.")

def findmax():
    n=int(input("Enter how many numbers you want to compare : "))
    a=[]
    for i in range(n):
        j=int(input("Enter number : "))
        a.append(j)
    max_a=a[0]
    for i in a:
        if i>max_a:
            max_a=i
    print("The largest number among the given numbers : ",max_a)
    
def primefinder():
    n=int(input("Enter number : "))
    a=[]
    for i in range(2,n):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            a.append(i)       
    for i in a:
        print(i,end=" ")
        
def otpgenerator():
    otp=""
    for i in range(4):
        j=randint(48,57)
        d=chr(j)
        otp+=d
    print("The otp is : ",otp)

def vowelcounter():
    n=input("Enter word : ")
    b="aeiouAEIOU"
    c=0
    for i in n:
        if i in b:
            c=c+1
    print("The total number of vowels in",n,"is : ",c)

dic={1:"finding factorial of the number",2:"checking prime",3:"for a simple calculator",4:"checking if the number is armstrong or not",5:"checking if the number is perfect square or not",6:"checking if the number is palindrome or not",7:"base conversion of the number",8:"finding LCM of two numbers",9:"finding HCF of two numbers",10:"finding fibonacci series till the number",11:"checking if the number is a perfect number or not",12:"finding max number among many numbers",13:"finding prime numbers till the input number",14:"generating OTP",15:"counting vowels in a word"}
for k,v in dic.items():
    print("type",k,"for",v)
print()
z=int(input("Enter your choice : "))
if z==1:
    factorial()
elif z==2:
    prime()
elif z==3:
    calculator()
elif z==4:
    armstrong()
elif z==5:
    perfectsquare()
elif z==6:
    palindrome()
elif z==7:
    baseconversion()
elif z==8:
    lcm()
elif z==9:
    hcf()
elif z==10:
    fibonacci()
elif z==11:
    perfectnumber()
elif z==12:
    findmax()
elif z==13:
    primefinder()
elif z==14:
    otpgenerator()
elif z==15:
    vowelcounter()
else:
    print("Invalid choice")
