import random

my_random1 = [random.randrange(1,101) for _ in range (10)]
my_random2 = [random.randrange(1,101) for _ in range (10)]
common_elements = []

print(my_random1)
print(my_random2)

common_elements = [item for item in set(my_random1+my_random2) if item in my_random1,my_random2]

print(common_elements)
