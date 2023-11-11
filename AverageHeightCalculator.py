# Input a Python list of student heights
student_heights = input("Input a Python list of student heights \n").split()
#print(student_heights)
totalStudents=len(student_heights)
sum_total=0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sum_total+=student_heights[n]

average_height=round(sum_total/totalStudents)
print(f"total height = {sum_total}\nnumber of students = {totalStudents} \naverage height = {average_height}")

  

