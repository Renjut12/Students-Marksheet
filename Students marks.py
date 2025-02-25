'''Creates a text file named "students.txt" if it doesn’t already exist.
Allows the user to add student names and their marks to the file.
Reads the file and displays the student details in a formatted way.
Counts and displays the number of students who scored above 75 marks.?......'''

def add_student():
    with open('Students.txt','a') as file:
        name = input("Enter student Name:") 
        marks = int(input('Mark:'))
        file.write(f"{name},{marks}\n")
    print('Students record added successfully...!\n')

def display_students():
    f = open('Students.txt','r')
    print("\n Student Records")
    print("-" * 30)

    for line in f:
        data = line.strip().split(",")
        if len(data)==2:
            name,marks = data
            print(f"Name:{name},Marks:{marks}")

def count_highscore():
    count=0
    f = open("Students.txt","r")

    for line in f:
        name,marks = line.strip().split(",")
        if int(marks)>75:
            count+=1
            print(f"number of students scoring above 75 is : {count}\n")


while True:

    choice = int(input("Enter Operation\n 1:Add Students\n 2:Display Students\n 3:Count Students with marks above 75 \n 4:QUIT   ------------->"))
    if choice==1: 
        add_student()
    elif choice==2:
        display_students()
    elif choice==3:
        count_highscore()
    elif choice==4:
        print('Exist from the program')  
        break
    else:
        print("Invalid choice")          