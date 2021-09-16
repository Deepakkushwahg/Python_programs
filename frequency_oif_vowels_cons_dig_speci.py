# program to find frequency of vowels , consonants , digits and special character
st=input("Enter your string\n")
c1=0
c2=0
c3=0
c4=0
for i in st:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        c1=c1+1
    elif(i>='a' and i<='z' or i>='A' and i<='Z'):
        c2=c2+1
    elif(i>='0' and i<='9'):
        c3=c3+1
    else:
        c4=c4+1
print("No. of vowels = ",c1)
print("No. of consonant = ",c2)
print("No. of digits = ",c3)
print("No. of special character = ",c4)
