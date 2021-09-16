# Write a Python program to remove an item from a set if it is present in the set. Here Both Item and Set is enter by the User.
st=set(map(int, input("Enter the set element\n").split()))
item=int(input("Enter the item which do you want to remove: "))
if(item in st):
    st.remove(item)
    print("Set after removing item\n{}".format(st))
else:
    print("Item ({}) is not present in the set".format(item))
