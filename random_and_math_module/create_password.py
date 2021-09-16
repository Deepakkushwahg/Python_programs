# program to create password
import random
import string
char_lower=string.ascii_lowercase
char_upper=string.ascii_uppercase
dig=string.digits
special_char="!@#$%^&*-_"
pas=char_lower + char_upper + dig + special_char
lst=list(pas)
random.shuffle(lst)
print("suitable password")
print("".join(random.sample(lst,8)))