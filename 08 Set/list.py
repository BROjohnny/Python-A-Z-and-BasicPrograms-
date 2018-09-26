
friends = ["ossa" , "jeewa" , "pantha" , "madu rox"]


print(friends)
print(friends[0])
print(friends[2])

print("\n")
print("___________________________________________________________________")
print("\n")

fiveProduct = [5 , 10 , 15 , 20 , 25 , 30]

print(fiveProduct)
print(fiveProduct[0])
print(fiveProduct[5])


print("\n")
print("___________________________________________________________________")
print("\n")

ages = input("Enter special ages in our life")
ourages = ages.split(',')
print(ourages)

print("\n")
print("___________________________________________________________________")
print("\n")

fiveProduct = [5 , 10 , 15 , 20 , 25 , 30]
names = ["janidu" , "jaysanka"]
fiveProduct.extend(names)
print(fiveProduct)
fiveProduct.remove("janidu")
fiveProduct.append("master")
print(fiveProduct)