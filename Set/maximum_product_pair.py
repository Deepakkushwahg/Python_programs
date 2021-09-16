# Write a program to find maximum product of two integers in a given set.
st=eval(input("Enter the set\n"))
max_product=[]
max_product.append(max(st))
st.discard(max(st))
max_product.append(max(st))
print(set(max_product))