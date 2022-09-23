def addinfo(courses):
    c_code=input("Enter the course code").upper()
    if c_code not in courses:
        c_name=input("Enter the name of the course")
        c_faculty=input("Enter the name of faculty")
        c_reg=int(input("Enter the number of registrations"))
        courses[c_code]={'course_name':c_name,'faculty':c_faculty,'no_of_reg':c_reg}
    else:
        print("duplicate course entry")

def display(courses):
    for course in courses:
        print("----------------------------------------------------------------------")
        print("THE DETAILS OF COURSE-",course)
        print("coursename-",courses[course]['course_name'])
        print("faculty-",courses[course]['faculty'])
        print("no of reg-",courses[course]['no_of_reg'])


def highestreg(courses):
    cr=0
    c_name=""
    for course in courses:
        if courses[course]['no_of_reg']>cr:
            cr=courses[course]['no_of_reg']
            c_name=courses[course]['course_name']
    print("the courese with highest registrations is")
    print("course-",c_name,"no of reg-",cr)



def main():
    courses={}
    while True:
        print("Enter 1 to add information of courses")
        print("Enter 2 to display infromation of courses")
        print("Enter 3 to find the course with highest registrations")
        ch=int(input("Enter your choice"))
        if ch==1:
            addinfo(courses)

        if ch==2:
            display(courses)
        if ch==3:
            highestreg(courses)
        if ch==4:
            exit()


if __name__=="__main__":
    main()
