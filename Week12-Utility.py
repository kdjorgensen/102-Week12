#https://github.com/kdjorgensen/102-Week12.git
#Kristian Jorgensen
#CSCI 102A
#Week 12 Utility

# Print Output
import string

def PrintOutput(thing_to_print):
    print('OUTPUT ', thing_to_print)

# LoadFile

def LoadFile(filename):
    with open(filename) as f:
        list = f.readlines()
    return "OUTPUT ", list

#UpdateString

def UpdateString(first_part, second_part, num):
    print("OUTPUT ", first_part[:num] + second_part + first_part[(num + len(second_part)):])

# FindWordCount

def FindWordCount(list, substring):
    return list.count(substring)

# Find Score
def ScoreFinder(list_one, list_two, name):
    if list_one.upper().index(name.upper()) > 0:
        print("OUTPUT ", name, list_two[list_one.index(name)])
    else:
        print("OUTPUT Player Not Found")

# Union

def Union(list_one, list_two):
    return "OUTPUT ", list_one + list_two

# Intersection

def Intersection(list_one, list_two):
    new_list = []
    for i in range(0, len(list_one), 1):
        if list_one in list_two:
            new_list.append(list_one)
    return "OUTPUT ", new_list


# NotIn

def NotIn(list_one, list_two):
    new_list = []
    for i in range(0, len(list_one), 1):
        if list_one not in list_two:
            new_list.append(list_one)
    return "OUTPUT ", new_list