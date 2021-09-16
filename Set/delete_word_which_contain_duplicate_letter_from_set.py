# Program to count the words consist duplicate letters in a given set. Also remove or discard those elements from a given set which consist duplicate letter.
set1 = eval(input("Enter the set\n"))
lst=[]
for i in set1:
    c=0
    for j in i:
        if i.count(j)==1:
            c+=1
    if c==len(i):
        lst.append(i)
print("No. of words which contain duplicate letter is",len(set1)-len(lst))
print(f"\nAfter remove duplicate letter words, words is left in a set is -- {len(lst)} -- and strings in the form of set is\n {set(lst)}")
