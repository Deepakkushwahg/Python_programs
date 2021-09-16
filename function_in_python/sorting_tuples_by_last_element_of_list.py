# Q12 program to sort tuple by last element of list by function
n=int(input("Enter the length of a list: "))
print("Enter elements for list")
lst=[tuple(int(input()) for i in range(2)) for j in range(n)]
lst.sort(key=lambda x: x[-1])
print(lst)
