number_of_students=int(input("Enter number of students: "))
start=1
total_student_marks=[]
while start<=number_of_students:
    print(f"=============Rol No: {start}=============")
    for i in range(1):
        nep = int(input("Enter nep mark: "))
        eng = int(input("Enter eng mark: "))
        math = int(input("Enter math mark: "))
        sic =int(input("Enter sic mark: "))
        com = int(input("Enter com mark: "))
        total = nep+eng+math+sic+com
        total_student_marks.append(total)
       
    start+=1


i=1

for total in total_student_marks:
    per=total/5
    grade=""
    if per>35 and per<45:
        grade="C"
    elif per>45 and per<60:
        grade="B"
    elif per>60 and per<100:
        grade="A"
    else:
        grade="D"
    
    print(f"Roll No: {i} Total: {total} Percentage: {per} Grade: {grade}")
    i+=1
    
  