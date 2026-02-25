# read entire file
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# read line by line
file = open("data.txt", "r")
for line in file:
    print(line)
file.close()

#read oneline
file = open("data.txt", "r")
print(file.readline())
file.close()

#write to a file
file = open("data.txt", "w")
file.write("Hello World")
file.close()
