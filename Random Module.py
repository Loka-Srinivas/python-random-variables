# random function():- It is used to generate random float number between 0.0 to 1.0

import random
print(random.random())



#uniform function():- It is used to generate random float number between two given numbers
print(random.uniform(1,10))


#randinte function():- It is used to generate random integer between two given numbers
print(random.randint(100,200))

#randrange function():- It is used to generate random integer between two given numbers with a step value
print(random.randrange(100,200,5))


#choice function():- It is used to generate random element from a non-empty sequence
list1=['apple', 'banana', 'cherry', 'grapes']
print(random.choice(list1))


#choices function():- It is used to generate random elements from a non-empty sequence
list1=['Blue', 'Black', 'White', 'Green']
print(random.choices(list1, k=2))



#sample function():- It is used to generate unique random elements from a non-empty sequence
list1=['Blue', 'Black', 'White', 'Green']
print(random.sample(list1, k=3))




import random
print(random.random())


print(random.uniform(1,20))

print(random.randint(100,300))


print(random.randrange(100,200,9))

list1=['Srinu','Dhanesh','Mahesh','Hemanth','Aravind','sateesh','Dharishi']

print(random.choice(list1))

print(random.choices (list1,k=3))


print(random.sample(list1,k=3))



   