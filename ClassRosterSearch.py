# ClassRosterSearch.py
#
# This particular program takes two arguments from the terminal, a command and a csv file, and prints the names
# (FirstName LastName) that fit the requested data.
#
# Created by Jailan Sabet

import re, csv, sys

# Final list to return names
finalList = []

# Read in csv file
csvFile = sys.argv[2]
inFile = open(csvFile)
inReader = csv.reader(inFile)
studentsData= list(inReader)

# Check csv data, such as included header or incorrect formatting, by checking emails have an @ symbol
emailAt = re.compile(r'@')
if emailAt.search(studentsData[0][2]) == None:
    if emailAt.search(studentsData[1][2]) == None:
        # error, incorrect formatting
        raise Exception('CSV file has incorrect formatting.')
    else:
        # csv header deleted in list
        del studentsData[0]

# Save command
inp = sys.argv[1]

# partition the input into the command (name, email, or gpa) and the pattern
com = inp.partition(' ')
command = com[0] # command
pat = com[2] # pattern
patternVar = re.compile(pat,re.I) # Regex object to search for pattern. re.I means this search will not be case sensitive.

# Search through names
if command == '-name':
    for student in studentsData:
        # Search for pattern - if not found, fd == None
        fd = patternVar.search(student[0]+student[1])

        # If pattern was found, student will be added to the "Final List"
        if fd != None:
            finalList.append(student)

        #reinitialize found variable to none
        fd == None

# Search through emails
elif command == '-email':
    for student in studentsData:
        # Search for pattern - if not found, fd == None
        fd = patternVar.search(student[2])

        # If pattern was found, student will be added to the "Final List"
        if fd != None:
            finalList.append(student)

        #reinitialize found variable to none
        fd == None

# Search through gpa
elif command == '-gpa':
    sign = pat[-1] #Plus or minus
    gpaNum = float(pat[0:len(pat)-1]) #gpa number for comparison

    if sign == '+':
        for student in studentsData:
            if gpaNum < float(student[3]):
                finalList.append(student)
    else:
        for student in studentsData:
            if gpaNum > float(student[3]):
                finalList.append(student)

# Faulty command
else:
    raise Exception('Command not found.')

# Print Names
for name in finalList:
    print(name[0] + ' ' + name[1])
