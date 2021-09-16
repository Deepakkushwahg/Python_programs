# Q13 program to find person is able to vote or not by function
def vote(age):
    if(age>=18):
        return "able to vote"
    else:
        return "not able to vote"
    
age=int(input())
v=vote(age)
print(f"He/She is {v}")
