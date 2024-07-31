import numpy as np


def averageStudents(filename, gradesDict):
    try:
        open(filename)
    except FileNotFoundError:
        open(filename, "w")
    
    with open(filename,'r') as file:
        w = open(filename,'a')
        w.write(context)
        for line in file.readlines():
            print(line)
    
func("this.txt","hello\n")