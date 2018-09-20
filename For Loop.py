print("this is normal for loop")
for i in range(1,11):
    print(i)
print("\nin this for loop print 1 to 10 numbers passing 3 by 3")
for i in range(1,11 ,3):
    print(i)

print("\nthis is how to print values of 2 list as nexted loop")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj[1:]:
  for y in fruits[:2]:
    print(x, y)