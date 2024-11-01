class Course:
  def __init__(self,code,name,credits,type):
    self.code = code
    self.name = name
    self.credits = credits
    self.type = type
    self.enrolled_Students = []

  def __str__(self):
    return f"{self.name} {self.code}, credits:{self.credits}, is {self.type}"
  
  def enrollStudent(self,Student):
    if Student not in self.enrolled_Students:
      self.enrolled_Students.append(Student)
      Student.courses[self.code] = self.name
      print(f"{Student.name} enrolled in {self.name}")
  
class Student:
  def __init__(self,ID,name):
    self.ID = ID
    self.name = name
    self.courses = {}

  def dropCourse(self,Course):
    if Course.code in self.courses:
      self.courses.pop(Course.code)
      print(f"{self.name} dropped from {Course.name}")
    else:
      print(f"{self.name} not enrolled in {Course.name}")

  def listStudentCourses(self):
    print(f"List of courses for {self.name}:")
    for course_name in self.courses.values():
      print(course_name)

class System:
  def __init__(self):
    self.catalog = {}
    self.students = {}
  
  def addCourse(self,Course):
    self.catalog[Course.name] = Course    #course name as key
    print(f"Course {Course.code} added to catalog")

  def addStudent(self,Student):
    self.students[Student.name] = Student

  def getCourse(self,name):
    return self.catalog.get(name)
  
  def getStudent(self, name):
    return self.students.get(name)
    
  def displayCatalog(self):
    print("catalog: ")    
    for Course in self.catalog:
      print(Course)

  def saveCatalogFile(self,filename = "courses_catalog.txt"):
    with open(filename,'w') as file:
      for Course in self.catalog:
        file.write(f"{Course}\n")
    print("catalog saved successfully")

  def loadCatalogFile(self,filename = "courses_catalog.txt"):
    with open(filename,'r') as file:
      for line in file:
        line = line.strip().split(",")
        self.catalog.append(line)
    print("catalog loaded successfully")

    
def menu():

  system = System()

  #examples
  system.addCourse(Course(203,"Math",5,"core"))
  system.addCourse(Course(144,"English",2,"elective"))
  system.addCourse(Course(135,"Physics",4,"core"))
  system.addCourse(Course(334,"Programming",4,"core"))
  
  system.addStudent(Student(4420, "Ali"))
  system.addStudent(Student(3480, "Abbas"))
  system.addStudent(Student(1230, "Zahraa"))


  while True:

    print("""
1. Add Course: Add a new Course to the catalog.
2. Enroll Student in Course: Enroll a Student in a specified Course.
3. Drop Course for Student: Drop a specified Course for a Student.
4. List Student courses: Display all courses a Student is enrolled in.
5. Save Course Catalog: Save the current Course catalog to a file.
6. Load Course Catalog: Load the Course catalog from a file.
7. Exit: Exit the program.
- - - - - - - - - - - - - - - - - - - - - - - - - - -
""")
    choice = input("choose your character: ")

    if choice == "1":
      name = input("Enter course name: ")
      code = int(input("Enter course code: "))
      credits = int(input("Enter credits"))
      type_ = input("core or elective? ")
      system.addCourse(Course(code,name,credits,type_))
    
    elif choice == "2":
      student_name = input("enter Student name:")
      course_name = input("Enter Course name:")

      student = system.getStudent(student_name)
      course = system.getCourse(course_name)

      course.enrollStudent(student)
    
    elif choice == "3":
      student_name = input("enter Student name:")
      course_name = input("Enter Course name:")

      student = system.getStudent(student_name)
      course = system.getCourse(course_name)

      student.dropCourse(course)

    elif choice == "4":
      student_name = input("enter Student name:")
      student = system.getStudent(student_name)

      student.listStudentCourses()

    elif choice == "5":
      system.saveCatalogFile()

    elif choice == "6":
      system.loadCatalogFile()

    elif choice == "7":
      print("Exiting program")
      break

    else:
      print("Try again")
      
menu()






# System.addCourse(Math)
# System.addCourse(English) 
# System.addCourse(Physics)
# System.addCourse(Programming)

# System.displayCatalog()

# Math.enrollStudent(Ali)
# Math.enrollStudent(Abbas)

# Ali.dropCourse(Math)

# Abbas.listStudentCourses()
# System.saveCatalogFile()

# System.loadCatalogFile()


