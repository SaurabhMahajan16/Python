import pandas
import random
listOfNumbers=[1,2,3,4,5]
newListOfNumbers=[number+1 for number in listOfNumbers]
print(newListOfNumbers)
name="Saurabh"
newList=[letter for letter in name]
print(newList)
rangeNumbers=[i+i for i in range(1,5)]
print(rangeNumbers)
students=["Sam", "Saurabh", "Sonu", "Sonali"]
student_scores={student:random.randint(45,100) for student in students}
print(student_scores)
excelled_students={student:score  for (student,score) in student_scores.items() if score>60}
print(excelled_students)
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split() }
print(result)
student_scores_dict={
    "students":['Sam', 'Saurabh', 'Sonu', 'Sonali'],
    "score":[88,55,71,59]
                   }
student_df=pandas.DataFrame.from_dict(student_scores_dict)
print(student_df) 
students=[]
marks=[]
for (index, row) in student_df.iterrows():
    #print(row)
    marks.append(row.score)
    
print(marks)
    