lines = open("first_name_male.txt","r")
cont = 0
read = ""
final = ""

for cont in range(0,6301,1):
    read = lines.readline()+read
    final = read.split()
print(cont)
print(final)