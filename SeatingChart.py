"""
This program Prompts the user for the number of students and student's name and gives them
a random seat number for a seating chart

Creator: Hope Zobinou

Date: 4/7/21
"""

import random
if __name__ == '__main__':
    Students = [] #The list that holds the students names
    NewStudentOrder = [] #The list that holds the students names in a random order
    SeatNum = 1 #Seat number
    NumOfStudents = int(input("How many students do you have: "))
    for i in range(NumOfStudents): #For loop that gets the student's names and appends them to the "Students" list
        StudentName = input("Enter student's name: ")
        Students.append(StudentName) 
    print()
    NewStudentOrder = random.sample(Students, NumOfStudents) #Random sample makes a list from the "Students" list in random order w/o replacement
    for i in range(NumOfStudents): #For loop that prints the new seating chart
        print("Student Seat #:", SeatNum, "Student Name:", NewStudentOrder[i])
        SeatNum += 1
