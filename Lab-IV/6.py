student_detail=[{"Name":"Jack", "Assignment_marks":[10,20,30], "Quiz_marks":
[40,50,60], "Exam_marks":[70,80,90]},{"Name":"Tony", "Assignment_marks":
[31,32,33], "Quiz_marks":[24,25,26], "Exam_marks":[15,16,17]},{"Name":"Ryan",
"Assignment_marks":[22,19,33], "Quiz_marks":[44,55,66], "Exam_marks":
[77,88,99]}]
print("Displaying marks in list\n")
for i in student_detail:
    for j in i:
        print(f"{j}: {i[j]}")
    print()
print("\nDisplaying average marks\n")
for i in student_detail:
    for j in i:
        if (j in ["Assignment_marks", "Quiz_marks"]):
            print(f"avg.{j}: {sum(i[j])/len(i[j])}")
        elif(j=="Exam_marks"):
            print(f"avg.{j}: {sum(i[j])/len(i[j])}")
            m=sum(i[j])
            print(f"total {j}: {m}")
            if m>90:
                print("Grade: A")
            elif 90>m>80:
                print("Grade: B")
            elif 80>m>65:
                print("Grade: C")
            elif 65>m>50:
                print("Grade: D")
            else:
                print("Grade: F")
        else:
            print(f"{j}: {i[j]}")
        print()