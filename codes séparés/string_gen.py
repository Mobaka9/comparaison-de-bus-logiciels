import random
import string
import time

length_of_string = 10000

a = time.time()
stri = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))+"="
b= time.time()
print(stri)
c = b-a
print("temps de creation : "+ str(c))