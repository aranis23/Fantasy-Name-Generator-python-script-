import random as rd

gender = ""
names = []
last = []
name = ""

def name_getter(letra):
    cont = 0
    name_file = ""
    path = ""
    read = ""
    length = 0

    if letra == "m": 
        lenght = 6301
        path = "first_name_male.txt"

    elif letra == "f": 
        lenght = 4384
        path = "first_name_female.txt"

    name_file=open(path,"r")

    for cont in range(0,length+1,1):
        read = name_file.readline()+read
        names = read.split()

    print(lenght, names)
    rand = rd.randint(0,lenght)
    name = names[rand]

    return _name

def last_name_getter():
    last_name_file = open("last_name.txt")
    final_name = ""
    read_last=""

    for cont in range(10446):
        read_last = last_name_file.readline()+read_last
        last = read_last.split()
    
    rand2 = rd.randint(0,10445)
    final_name = last[rand2]


def main():
    gender = input("inserte el genero")
    if gender == "m":
        name = name_getter("m")

main()