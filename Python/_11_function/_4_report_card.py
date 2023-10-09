# def info():
#     ro_no=input("enter your roll :")
#     name=input("enter your name:")
#     eng_m=int(input("enter your eng sub marks:"))
#     math_m=int(input("enter your math sub marks:"))
#     sci_m=int(input("enter your sci sub marks"))
#     return eng_m,math_m,sci_m

# def total(eng,math,sci):
#     return eng+math+sci

# def percentage(total):
#     perc=(total/300)*100
#     return perc

# def grade(perc):
#     if perc>=50 and perc<60:
#         return "E"
#     elif perc>=60 and perc<70:
#         return "D"
#     elif perc>=70 and perc<80:
#         return "C"
#     elif perc>=80 and perc<90:
#         return "B"
#     elif perc>=90 and perc<=100:
#         return "A"
#     else:
#         return "failed"

# def display(total,perce,grade):
#     print("Total Marks:",total)
#     print("percentage:",perce)
#     print("Grade:",grade)

# Eng,Math,Sci=info()
# Total1=total(Eng,Math,Sci)
# percen=percentage(Total1)
# Grade=grade(percen)
# display(Total1,percen,Grade)












# def get_student_info():
#     rno = input("Enter Roll Number: ")
#     name = input("Enter Name: ")
#     eng = float(input("Enter English Marks: "))
#     maths = float(input("Enter Math Marks: "))
#     science = float(input("Enter Science Marks: "))
#     student_info = {
#         'rno': rno,
#         'name': name,
#         'eng': eng,
#         'maths': maths,
#         'Science': science
#     }
#     return student_info

# def calculate_total(student_info):
#     return student_info['eng'] + student_info['maths'] + student_info['Science']

# def calculate_percentage(student_info):
#     total_marks = 300  
#     return (calculate_total(student_info) / total_marks) * 100

# def calculate_grade(student_info):
#     percentage = calculate_percentage(student_info)
#     if percentage >= 90:
#         return 'A+'
#     elif 80 <= percentage < 90:
#         return 'A'
#     elif 70 <= percentage < 80:
#         return 'B'
#     elif 60 <= percentage < 70:
#         return 'C'
#     else:
#         return 'F'
# def display_student_info(student_info):
#     print(f"Roll Number: {student_info['rno']}")
#     print(f"Name: {student_info['name']}")
#     print(f"English Marks: {student_info['eng']}")
#     print(f"Math Marks: {student_info['maths']}")
#     print(f"Science Marks: {student_info['Science']}")
#     print(f"Total Marks: {calculate_total(student_info)}")
#     print(f"Percentage: {calculate_percentage(student_info)}%")
#     print(f"Grade: {calculate_grade(student_info)}")

# num_students = int(input("Enter the number of students: "))

# for i in range(num_students):
#     print(f"Enter data for student {i + 1}:")
#     student_info = get_student_info()
#     display_student_info(student_info)
#     print()













def info():
    rno=int(input("enter rno"))
    name=(input("enter name"))
    eng=int(input("enter english marks"))
    mat=int(input("enter maths marks"))
    sci=int(input("enter scince marks "))
    return rno,name,eng,mat,sci
def total(eng,mat ,sci):
    print ("Total")
    sum=eng+mat+sci
    print(sum)
    return sum
def percentage(sum):
    print("Precentage")
    avg=(sum/300)*100
    print( avg)
def grade(sum):
    print("Grade")
    if sum>=285:
        print("A+")
    elif sum >210:
        print("A")
    else:
        print("B")

def display():
    information=info()
    print(f'name {str(information[1])}')
    print(f'roll no {str(information[0])}')
    print(f'english marks  {str(information[2])}')
    print(f'math marks {str(information[3])}')
    print(f'scince marks {str(information[4])}')
    total_sum=total (information[2],information[3],information[4])
    percentage(total_sum)
    grade(total_sum)

display()