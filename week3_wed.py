
d = {
    "Annie": [67,90,87],
    "Bryan": [75,72,81],
    "Charlie": [82,100,91]
}

def averageStudents(filename, gradesDict):
    try:
        open(filename)
    except FileNotFoundError:
        open(filename, "w")
    
    with open(filename,'a') as file:
        for g in gradesDict:
            average = round(sum(num for num in d[g]) / len(d[g]))
            file.write("NAME: " + g + " GRADES: " + str(d[g][0]) + " " + str(d[g][1]) + " " + str(d[g][2]) + " AVERAGE: " + str(average) + "\n")
        print(file)
            
    
averageStudents("students.txt",d)