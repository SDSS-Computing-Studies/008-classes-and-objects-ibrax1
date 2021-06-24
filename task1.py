#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grades - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:

    # properties should be listed first

    def __init__(self, name, studentNumber, grade): # You will need to create your own input parameters for all methods
        self.name = name
        self.studentNumber = studentNumber
        self.grade = grade
        # self.courses = courses
        # self.grades = grades
        print("I am a student named " + self.name + ".")
    def methods(self):
        print("Do you want to see:")
        print("1. Average Grades")
        print("2. Honor Roll")
        print("3. My Courses")
        print("4. My Grade in Any Course")
        print("5. My Courses in a list")
        print("6. My Grades in a list")
        command = input("Enter a number (1-6): ")
        return int(command)
        
    def func(self, command):
        if command == 1:
            self.average()
        elif command == 2:
            self.getHonorRoll()
        elif command == 3:
            self.courselist()
        elif command == 4:
            self.grade1course()
        elif command == 5:
            self.getCourses()
        elif command == 6:
            self.getGrades()
        
    def average(self):
        for x in courses:
            def getHonorRoll(self):
                print(2)
    def courselist(self):
        print(3)
    def grade1course(self):
        print(4)
    def getCourses(self, list):
        print(list)
    courses = ["Math, Pop, pepsi, gogy, doog"]
    def getGrades(self, list1):
            print(list1)
    self = ()
    grades = [99, 46, 70, 37, 67]
    def average(self, courses):
        for x in courses:
            y = (x+x)
            y = (y+x)
        return(y)
    print (average(self, courses))

def __del__(self):
        print("goodbye. "+ str(self.name) + " has left the room.")

def average(self):
    pass

def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])




main()