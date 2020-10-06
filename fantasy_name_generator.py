import random as rd

gender = ""
names = []
last = []
length = 0

final_name = ""
read = ""
read_last=""

def name_getter():
    cont = 0
    name_file = ""
    last_name_file = open("last_name.txt")

    if gender.lower == "m": 
        lenght = 6301
        name_file = open("first_name_male.txt")

    elif gender.lower == "f": 
        lenght = 4384
        name_file = open("first_name_female.txt")

    for cont in range(length):
        read = name_file.readline()+read
        names = read.split()
    
    for cont in range(10445):
        read_last = last_name_file.readline()+read_last
        last = read.split()


    rand = rd.randint(lenght)
    rand2 = rd.randint(10445)
    final_name = names[rand]+last[cont]

    return final_name

def main():
    gender = input("inserte el genero")
    if gender == "m":
        final_name = name_getter()
        print(final_name)
main()

