import random

while True:
    students = []
    intro = print("Add names to shuffle!")
    num_students = 10

    for i in range(num_students):
        name = input("Enter a name: ")
        students.append(name)
    
    names = random.choice(students)  # Shuffling the list of students
    print(names)
    
    choice = input("Press 'S' to shuffle again or any other key to exit: ")
    if choice.lower() != 's':
        break
 