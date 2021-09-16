# program to check string is anagram or not
a=input("Enter first string\n")
b=input("Enter second string\n")
if(len(a)==len(b)):
    if(sorted(a)==sorted(b)):
        print("String is anagram")
    else:
        print("String is not anagram")
else:
    print("String are not anagram")
    