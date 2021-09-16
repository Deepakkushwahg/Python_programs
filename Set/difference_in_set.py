# Program that Display which Letters are in the First String but not in the Second.
st1=set(input("Enter the first sets elements\n").split())
st2=set(input("Enter the second sets elements\n").split())
letters=sorted(st1.difference(st2))
print("Letter {} is present in first set but not in second set".format(letters))
