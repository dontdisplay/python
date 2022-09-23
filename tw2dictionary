def addcourse(courses):
    course=input("Enter the course id").upper()
    if course not in courses:
        c_name=input("Enter the course name")
        c_faculty=input("Enter the name of faculty")
        c_reg=int(input("Enter the number of registrations"))
        courses[course]={'course_name':c_name,'faculty':c_faculty,'no_of_reg':c_reg}
    else:
        print("Duplicate course entry!! Entry denied")


def display(courses):
    for course in courses:
        print("--------------------------------------------------------------------------------\n\n")
        print("Details of the course -",course)
        print("Name->",courses[course]['course_name'])
        print("Faculty->",courses[course]['faculty'])
        print("NO_OF_registrations->",courses[course]['no_of_reg'])

def highestreg(courses):
    cr=0
    cname=""
    for course in courses:
        if courses[course]['no_of_reg']>cr:
            cr=courses[course]['no_of_reg']
            cname=courses[course]['course_name']
    print("-----------------------------------------------------------------------------------\n\n")
    print("The Highest Registered course is",cname," with ",cr," registrations")


def main():
    courses={}

    while True:
        print("---------------------------------------------------------------------------------------------\n")
        print("Enter 1 for adding a course")
        print("Enter 2 for displaying present courses")
        print("Enter 3 for finding highest registerd course")
        print("Enter 4 to exit")
        ch=int(input("Enter you choice"))

        if ch==1:
            addcourse(courses)
        if ch==2:
            display(courses)
        if ch==3:
            highestreg(courses)
        if ch==4:
            exit()


if __name__=="__main__":
    main()
