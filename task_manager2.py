#=====importing libraries===========
# opens both files that programme will read and write to. 
'''This is the section where you will import libraries'''
t = open('user.txt', 'r+')
f = open('tasks.txt', 'r+')
from datetime import date
import datetime
#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
# Takes input from user and loops until correct input is entered. 
while True:
    user_name = input("Enter username:").lower()
    if user_name == "admin":
        print("Username correct")
        break
    else:
        print("Please try again")

while True:
    pass_word = input("Enter password:").lower()
    if pass_word == "adm1n":
        print("Password Correct")
        break
    else:
        print("Please try again")

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
ds - Display Statistics
e - Exit
: ''').lower()
    # Only if user enters 'admin' for username will programme allow registering a user. 
    if menu == 'r' and user_name == "admin":
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        # takes input from user and uses an if statment to confirm that correct password is entered. 
        new_username = input("Enter new user name:")
        new_password = input("Enter new password:")
        confirm_password = input("Confirm password:")
        user_details = (new_username, new_password)
        if confirm_password in new_password:
            # Opens user.txt file and writes user name and password to file. 
            with open('user.txt', 'a') as ofile: 
                ofile.write((str(user_details))+"\n")
            #Closing file after use.     
            ofile.close() #close the file!
        else:
            print("Passwords do not match:")
            
    elif menu == 'a':
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
         # Takes user input and writes this to tasks.txt file.    
        user_name = input("Enter username of who task is assigned to:")
        title_task = input("Enter tile of task:")
        desc_task = input("Enter description of task:")
        due_date = (int(input("Enter due date of task in DDMMYYYY:")))
        today = int(date.today().strftime('%d%m%Y'))
        if today > due_date:
            task_comp = ""
        else:
            task_comp = "No"
        write_task = ("Task:    "+title_task+","+"Assigned to:    "+user_name+","+"Date assigned:    "+str(today)+","+"Due date:    "+str(due_date)+","+"Task Complete?    "+task_comp+","+"Task description:    "+desc_task+",")
        with open('tasks.txt', 'a') as ofile: # Open the file again!
            ofile.write(str(write_task)+"\n")
        ofile.close() #close the file!


    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''
        # Reads tasks.txt and prints contents of file.     
        contents = ""
        with open('tasks.txt', 'r+') as f: # Open the file again!
            for line in f:
                contents = contents + line
            print('\n'.join(contents.split(",")))

    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
        # If user_name is in tasks.txt the entire file will be printed on seperate lines with use of join and split functions. 
        contents = " "
        with open('tasks.txt', 'r+') as f:
                for line in f:
                    if user_name in line:
                        contents = contents + line
        print('\n'.join(contents.split(",")))
        
    #Allows users to count number os user name entries and number of task entries into tasks.txt  
    elif menu == 'ds':
        #Opens tasks.txt for reading and counts len of lines in file. 

        with open('tasks.txt', 'r') as f:
            x = len(f.readlines())

            #Prints total amounts of lines in tasks.txt    
            print("Total number of tasks is: " + (str(x)))

        #Opens tasks.txt for reading and counts len of lines in file. 
        with open('user.txt', 'r') as t:
            n = len(t.readlines())
            #Prints total number of lines in user.txt.   
            print("Total number of users is :"+ (str(n)))


    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    
      

    else:
        print("You have made a wrong choice, Please Try again")
