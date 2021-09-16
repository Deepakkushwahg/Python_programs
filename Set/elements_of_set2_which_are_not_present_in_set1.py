# Program to find all elements of a set2 which are not present in set1 using Set Comprehension.
set1=eval(input("Enter the set1\n"))
set2=eval(input("Enter the set2\n"))
print({i for i in set2 if i not in set1})
