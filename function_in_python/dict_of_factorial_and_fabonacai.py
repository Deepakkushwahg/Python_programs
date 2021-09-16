# program to find dictionary of factorial and fabonacai
def fact(n):
    i=1
    while n>0:
        i=i*n
        n=n-1
    return i

def fabo(n):
    lst=[]
    a=0
    b=1
    lst.append(a)
    while n-1 > 0:
        c=a
        a=a+b
        b=c
        lst.append(a)
        n=n-1
    return lst
n=int(input("Enter the number:"))
key=fact(n)
value=fabo(key)
dct={}
dct.update({key:value})
print(dct)