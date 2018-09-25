import random
print(random.randint(0,10))

print("_________________________________________________________")

colors = ['red' , ' blue' , 'yellow' , 'purple' , 'green']
print(colors[random.randint(0,2)])
print(random.choice(colors))

print("_________________________________________________________")

winnigNumbers = set()

while len(winnigNumbers) < 5:
    winnigNumbers.add(random.randint(1 , 99))
print(winnigNumbers)

