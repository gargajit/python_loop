'''
students = ["Hermoine", "Harry", "Ron"]

print(students[0])

for student in students:
    print(student)
'''

'''
students = ["Hermoine", "Harry", "Ron"]

for i in range(len(students)):
    print(i+1, students[i])
'''

#Python Dictionary

'''
students = {
    'Hermione': 'Gryffindor', 
    'Draco': 'Slytherin',
    'Harry': 'Gryffindor',
    'Katie': 'Ravenclaw'
}

#print(students["Draco"])
#print(students["Hermione"])


for student in students:
#    print(student)          #this will print the "keys"
    print(student, students[student], sep = ", ")
'''


#List of Dictionaries

students = [
    {'name': 'Hermione', 'house': 'Gryffindor', 'patronus': 'otter'},
    {'name': 'Harry', 'house': 'Gryffindor', 'patronus': 'stag'},
    {'name': 'Ron', 'house': 'Gryffindor', 'patronus': 'Jack Russell terrier'},
    {'name': 'Draco', 'house': 'Slytherin', 'patronus': None}
]

for student in students:
    print(student['name'], student['patronus'], sep=" -> ")
