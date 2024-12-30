file = open("Nature.txt" , "r")
print(" Reading First 4 letters ")
print(file.read(5))
file.close()

file = open("Nature.txt" , "r")
print(" Reading First Line ")
print(file.readline())
file.close()

file = open("Nature.txt" , "r")
print(" Reading Multiple Line ")
print(file.readline( ) )
print(file.readline( ) )
print(file.readline( ) )
file.close()

file = open("Nature.txt" , "r")
print("Looping Through lines ")
for line in file:
    print(line)
file.close()