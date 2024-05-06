students_name = ["Rudolf", "Darien", "Richie", "Athar", "Cristian"]
students_score = [100, 90, 80, 70, 70]
students_grade = {}

for i in range(len(students_score)):
  if(students_score[i] >= 90):
    students_grade.update({"A"})
  elif(students_score[i] >=70):
    students_grade.update({"B"})
  else:
    students_grade.update({"C"})

print(str(students_grade))