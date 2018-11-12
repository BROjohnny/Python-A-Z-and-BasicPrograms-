#how to print text file lines in python IDE
file1 = open("1_todolist.txt" , "r")

#type 1
print(file1.read())

print("--------------------------------------------------------------------------")

file2 = open("2_todolist.txt" , "r")

#type2
print(file2.readlines())

print("--------------------------------------------------------------------------")

file3 = open("3_todolist.txt" , "r")

#type3
print(file3.readline())

print("--------------------------------------------------------------------------")

file3.seek(0)

for index,line in enumerate(file3 , start = 1) :
    print( "{}) {}" .format(index,line) , end= '')

print("\n--------------------------------------------------------------------------")

def write_file(task):
    with open('4_todolist.txt' , 'w') as file4:
        file4.write(task)

write_file('master johnny madrid')
print("\nin 4_todolist.txt will be update from this")

print("--------------------------------------------------------------------------")

def append_file(task):
    with open('5_todolist.txt' , 'a') as file5:
        file5.write(task)

append_file('\nmaster johnny madrid')
print("\nin 5_todolist.txt will be update from this")
