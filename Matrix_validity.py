# program to check matrix is valid or not
m=eval(input())
ln=len(m[0])
for i in m:
    if len(i)!=ln:
        print('Not valid matrix')
        break
else:
    print('valid matrix')
    print("Element at [1*1]", m[0][0])
    
