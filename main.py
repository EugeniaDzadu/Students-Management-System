# console colours
ROSY_PINK="\033[38;2;135;82;62m"
BLUE="\033[0;34m"
BANANA_YELLOW="\033[38;2;240;238;113m"
DARK_RED="\033[38;2;145;40;16m"
GREEN="\033[0;32m"

# accessing the student module
from student import Student
from tabulate import tabulate

# databases
student_database = []

def welcome_screen():
    user_response = int(input(GREEN+'******* Student Management System******* \n'
          '1. Add Student \n'
          '2. View all students \n'
          '3. Update students info \n'
          '4. Delete student info \n'
          '5. Search for student \n'
          '6. Exit app \n\n'
          'Provide valid option: '))
    
    # calling a function to determine user choose option
    user_chosen_option(user_response)
    
def user_chosen_option(user_response):
    if user_response == 1:
        add_student()
        
    elif user_response == 2:
        view_student()
        
    elif user_response == 3:
        user_id = input('Enter studentid: ')
        exist = is_student_id_available(user_id)
        if exist == False:
            print('Student record not found')
        else:
           update_student(user_id)
           
    elif user_response == 4:
        delete_student()
    
    elif user_response == 5:
        search_student()
        
    elif user_response == 6:
        print('Thanks for visiting our website')
        exit(0)
    
    else:
        print('Invalid response, please try again!!')
    welcome_screen()
        
# function to handle adding students
def add_student():
    print('***** Provide New Student Information***** \n')
    student_id = input('Enter Student ID: ')
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    age = int(input('Enter age: '))
    gender = input('Enter gender: ')
    

    # if len(student_id) < 1:
    #     print('wrong input, please try again!!')
    # elif len(first_name)<1:
    #     print('wrong input, please try again!!')
    # elif len(last_name)<1:
    #     print('wrong input, please try again!!')
    # elif len(age)<1:
    #     print('wrong input, please try again!!')
    # elif len(gender)<1:
    #     print('wrong input, please try again!!')
    # # create instance of the class, which will make us get an object
    student = Student(student_id, first_name, last_name, age, gender)
    
    # save the info into the database
    student_database.append(student)
    print(f'{first_name}  {last_name} has been saved successfully \n')
    
def view_student():
     print(f'****Student Information*****')
     if student_database != "":
        student_table=[]
        for student in student_database:
            student_table.append([student.student_id, student.first_name , student.last_name, student.age, student.gender])
        header = ['Student_ID', 'FirstName', 'LastName', 'Age', 'Gender']
        print(BANANA_YELLOW, tabulate( student_table, header, tablefmt='fancy_grid'))
      
     else:
         print('no information available to view')
         
def is_student_id_available(id):
    for student in student_database:
        if student.student_id == id:
            return True
    return False
         
def update_student(user_id):
        choose = input(BLUE+'***Choose data to change*** \n'
                           'FirstName(F) \n'
                           'LastName(L) \n'
                           'Age(A) \n'
                           'Gender(G)\n\n'
                           'Choose data: ').upper()
        prompt = ''
        if choose == 'F': 
            prompt = 'FirstName'
        elif choose == 'L':
            prompt == 'LastName'
        elif choose == 'A':
            prompt = 'Age'
        elif choose == 'G':
            prompt = 'Gender'
        answer = input(f'Enter new {prompt}: ')
        update_student_info(user_id,choose, answer)
        print('Student info updated successfully')


def update_student_info(id, prompt, value):
    for student in student_database:
        if student.student_id == id:
            if prompt == 'F':
                student.first_name = value
            elif prompt == 'L':
                student.last_name = value
            elif prompt == 'A':
                student.age = value
            elif prompt == 'G':
                student.gender = value
                
           
            
def delete_student():
    for student in student_database:
        if student.student_id:
          delete = input('Enter StudentID: ')
          input(ROSY_PINK, 'Are you sure?\n'
                  'YES \n'
                  'NO \n\n'
                  'choose option: ').upper()
        else:
            print('Your search is empty')
            
def search_student():
    if len(student_database)>0:
        student_list = []
        user_search = input('Enter studentID:')
        for student in student_database:
            if student.student_id == user_search:
                student_list.append([student.student_id, student.first_name, student.last_name, student.age, student.gender])
                header = ['Student_ID', 'FirstName', 'LastName', 'Age', 'Gender']
                print(DARK_RED, tabulate(student_list,header, tablefmt='fancy_grid'))
                break
                
    else:
        print(DARK_RED, 'Your search is empty')
            

    
welcome_screen()
    