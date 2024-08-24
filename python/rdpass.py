import random
from string import ascii_letters, digits
all_chs = ascii_letters + digits
def rdpass(n=8):
    result = ''
    for i in range(n):
        ch = random.choice(all_chs)
        result += ch
    return result
print(rdpass())