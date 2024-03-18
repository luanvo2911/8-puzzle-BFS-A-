import random

# Generate a list of 9 different random numbers from 0 to 9
for x in range(0, 1000):
  random_list = random.sample(range(9), 9)
  random_string = str()
  for i in random_list:
    random_string += str(i)
    
  f = open(f"test/{x}.txt", "w")
  f.write(random_string)
  f.close()

# print(random_string)
