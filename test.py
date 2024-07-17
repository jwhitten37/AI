import random

res = random.sample(range(1, 50), 7)

ran_list = []
for x in res:
    
    ran_list.append(x)

print(ran_list)
print(ran_list[0])
print(ran_list[-1])