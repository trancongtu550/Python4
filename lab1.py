#Chương 3 bài 1 
print(min(2,3,4))
print(max(2,(-3),7,4,5))
print(max(2,(-3),min(4,7),-5))
#Chương 3 bài 2 
print(min(max(3, 4), abs(-5)))
print(abs(min(4, 6, max(2, 8))))
print(round(max(5.572, 3.258), abs(-2)))
#Chương 3 bài 3
def triple(num):
  return num * 3
triple(3)
#Chương 3 bài 4
def absolute_difference(number1, number2):
  return abs(number1 - number2)
absolute_difference(3, 7)
#Chương 3 bài 5
def km_to_miles(km):
  return km / 1.6
km_to_miles(5)
#Chương 3 bài 6 
def average_grade(grade1, grade2, grade3):
  return (grade1 + grade2 + grade3) / 3
average_grade(80, 95, 90)
#Chương 3 bài 7
def top_three_avg(grade1, grade2, grade3, grade4):
   total = grade1 + grade2 + grade3 + grade4
   top_three = total - min(grade1, grade2, grade3, grade4)
   return top_three / 3
   return max(average_grade(grade1, grade2, grade3),
    average_grade(grade1, grade2, grade4),
    average_grade(grade1, grade3, grade4),
    average_grade(grade2, grade3, grade4))
   return (grade1 + grade2 + grade3) / 3
top_three_avg(50, 60, 70, 80)
#Chương 3 bài 8 
def weeks_elapsed(day1, day2):
    return (day1+day2)%7
weeks_elapsed(3,20)
#Chương 3 bài 9 
def square(num):
  return num*3
square(3) 