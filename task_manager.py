#Task 25 - Capstone Project IV

#import modules
from datetime import datetime #for getting today's date - source: https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
import os.path

#set initial variables
logged_in_user = ""
correct_password = ""
logged_in = False

#beginning of functions

def reg_user():
    #this task adds a user to the user.txt file
    
    new_user = input("\nEnter a new username: ")
            
    #check if new_user username exists
    user_exists=False
    
    #loop through user text file to see if the username has not been taken
    with open("user.txt", "r") as f:
        for line in f:
            line = line.split(", ")
            if (line[0] == new_user):
                user_exists = True
                
    #ask for a password if the username is not blank and does not exist
    if new_user != "" and user_exists == False:
        new_pwrd = input("Enter a password for the new user: ")
        new_pwrd_conf = input("Confirm password: ")
        
        #check if password and confirm password inputs match
        if new_pwrd == new_pwrd_conf:
        
            #store all current users in one string variable
            all_users = ""
            with open("user.txt", "r") as f:
                for line in f:
                    all_users += line
            
            #also add the new user to the string
            all_users += "\n"+new_user+", "+new_pwrd
            
            #write all the users back to the text file
            with open("user.txt", "w") as f:
                f.write(all_users)
                
            print(f"\nUser: {new_user} successfully added!")
            
        else:
            print("\nPassword does not match the confirmed password. Please try again.")
    
    elif user_exists != False:
        print("Please try a different username. This one has already been taken.")
        

def add_task():
    #this function adds a task to the tasks text file
    
    #user inputs for task
    task_user = input("\nWhich user is this task assigned to? ")
    task_title = input("\nEnter the task title: ")
    task_desc = input("\nEnter the task description: ")
    task_due = input("\nEnter the due date: ")
    
    #assigned variables
    task_date = datetime.today().strftime('%d %b %Y') #format found from source: https://www.w3schools.com/python/python_datetime.asp
    task_complete = "No"
    
    #get all tasks
    all_tasks = ""
    with open("tasks.txt", "r") as f:
        for line in f:
            all_tasks += line
            
    #also add the new task to the string
    all_tasks += task_user+", "+task_title+", "+task_desc+", "+task_date+", "+task_due+", "+task_complete+"\n"
    
    #write all the users back to the text file
    with open("tasks.txt", "w") as f:
        f.write(all_tasks)
                
    print(f"\n\nTask: {task_title} assigned to user: {task_user}")
    

def view_all():
    
    #print title
    print("\n\nAll Tasks:")
    print("-------------------------")
    
    #read from file
    with open("tasks.txt", "r") as f:
    
        #loop through lines from file
        for line in f:
            
            #take away the \n from the end value
            line = line.replace("\n","")
            
            #split username and password
            line = line.split(", ")
            
            #print the task in a readable format
            print("\n-"+line[1]+"-")
            print("\n"+line[2])
            print("\nAssigned to: \t "+line[0])
            print("Date Assigned: \t "+line[3])
            print("Date due: \t "+line[4])
            print("Task Complete: \t "+line[5])
            print("-------------------------")


def view_mine():
    #print title
    print(f"\n\nTasks for user: {logged_in_user}")
    print("-------------------------")
    
    #variable for counting task
    task_count = 0
    
    #read tasks from file
    with open("tasks.txt", "r") as f:
        
        #loop through lines in file
        for line in f:
        
            #take away the \n from the end value
            line = line.replace("\n","")
            
            #split username and password
            line = line.split(", ")
            
            #look specifically for the user's tasks
            if line[0] == logged_in_user:
        
                #print the task in a readable format
                print("\nTask "+str(task_count)+": "+line[1])
                print("\n"+line[2])
                print("\nAssigned to: \t "+line[0])
                print("Date Assigned: \t "+line[3])
                print("Date due: \t "+line[4])
                print("Task Complete: \t "+line[5])
                print("-------------------------")
                
                #increase the task count
                task_count += 1

    #user input for task
    task_selection = int(input('\nSelect a task number: '))
    
    while task_selection <- 1 or task_selection >= task_count:
        print("\nIncorrect input. Please enter again.")
        task_selection = int(input('\nSelect a task number (or -1 to go back): '))
        
    if task_selection > -1:
        
        #user input
        task_c_option = input("Would you like to mark this task as complete? (Y/N): ")
        
        task_e_option = input("Would you like to edit this task? (Y/N): ")
        
        #run functions if user input was Y:
        
        if task_c_option == "Y":
            mark_complete(task_selection)
            
        if task_e_option == "Y":
            edit_task(task_selection)
        

def edit_task(ts):
    #ask the questions and make it exactly the same as mark complete
    
    #variable for counting task
    task_count = 0
    
    #variable for new writes
    new_tasks = ""
    
    #read tasks from file
    with open("tasks.txt", "r+") as f:
        
        #loop through lines in file
        for line in f:
            
            #take away the \n from the end value
            line = line.replace("\n","")
            
            #split username and password
            line = line.split(", ")
            
            #only count tasks for specific user
            if line[0] == logged_in_user:
            
                #if correct task (number)
                if task_count == ts:
                    #line[5] = "Yes"
                    
                    #check if task can be edited
                    if line[5] == "No":
                        
                        #username input
                        print("\n1. Task is assigned to "+line[0]+".")
                        change_name = input("\nEnter the new username below\n[leave empty if you don't want to change it]\n: ")
                        
                        if change_name !="":
                            
                            #change username
                            line[0] = change_name
                            
                            #print success message
                            print("\nUsername has been changed!")
                        
                        #date input
                        print("\n\n2. This Task is due "+line[4]+".")
                        change_date = input("\nEnter the new due date below\n[leave empty if you don't want to change it]\n: ")
                        
                        if change_date !="":
                        
                            #change date
                            line[4] = change_date
                            
                            #print success message
                            print("\nDate has been changed!")
                    
                    else:
                    
                        #print error message
                        print("\nThis task has already been completed and cannot be edited.")
            
                #count task
                task_count += 1
                        
            
            #add to new tasks file string
            new_tasks += line[0]+', '+line[1]+', '+line[2]+', '+line[3]+', '+line[4]+', '+line[5]+'\n'
            
            
    #rewrite to tasks file
    with open("tasks.txt", "w") as f:
        f.write(new_tasks)
    
        
def mark_complete(ts):
    
    #variable for counting task
    task_count = 0
    
    #variable for new writes
    new_tasks = ""
    
    #read tasks from file
    with open("tasks.txt", "r+") as f:
        
        #loop through lines in file
        for line in f:
           
            #take away the \n from the end value
            line = line.replace("\n","")
            
            #split username and password
            line = line.split(", ")
            
            if line[0] == logged_in_user:
            
                if task_count == ts:
                    line[5] = "Yes"
                    
                    #print success message
                    print("\nTask has been marked as complete!")
            
                #add to task count variable
                task_count += 1
                
            
           #add to new tasks file string
            new_tasks += line[0]+', '+line[1]+', '+line[2]+', '+line[3]+', '+line[4]+', '+line[5]+'\n'
            
            
            
    #rewrite to tasks file
    with open("tasks.txt", "w") as f:
        f.write(new_tasks)
        


def gen_report():
    #print title
    print("\nGenerating report...")
    
    #variables for gen report
    count_tasks = 0
    count_complete = 0
    uncomplete_overdue = 0
    count_overdue = 0
    
    
    
    #read tasks from file
    with open("tasks.txt", "r+") as f:
    
        #loop through lines in file
        for line in f:
        
            #take away the \n from the end value
            line = line.replace("\n","")
            
            #split username and password
            line = line.split(", ")
        
            if line[5] == "Yes":
                #count as a completed task
                count_complete += 1
            
            #count line as a task
            count_tasks += 1
            
            #edit time format to compare variables
            task_due_date = datetime.strptime(line[4], '%d %b %Y')
            today_date = datetime.today()#.strftime('%d %b %Y')
            
            #if overdue
            if task_due_date < today_date:
                count_overdue += 1
            
            #if overdue and not complete
            if task_due_date < today_date and line[5] == "No": #found a similar solution at soure: https://stackoverflow.com/questions/20365854/comparing-two-date-strings-in-python
                uncomplete_overdue += 1
            
            
    
    #calculate incomplete tasks        
    count_uncomplete = count_tasks - count_complete
    
    #calculate % incomplete tasks
    perc_incomplete = count_uncomplete/count_tasks * 100
    perc_incomplete = round(perc_incomplete,2)
    
    #calculate % overdue tasks
    perc_overdue = count_overdue / count_tasks * 100
    perc_overdue = round(perc_overdue,2)
    
    
   
    #rewrite to tasks overview file
    with open("task_overview.txt", "w") as f:
        f.write(f"TASKS OVERVIEW")
        f.write(f"\n_____________________________________\n")
        f.write(f"Total tasks: \t\t\t\t{count_tasks}\n")
        f.write(f"Completed tasks: \t\t\t{count_complete}\n")
        f.write(f"Incomplete tasks: \t\t\t{count_uncomplete}\n")
        f.write(f"Incomplete and overdue: \t{uncomplete_overdue}\n")
        f.write(f"Percentage completed: \t\t{perc_incomplete}%\n")
        f.write(f"Percentage overdue: \t\t{perc_overdue}%\n")
        f.write(f"_____________________________________\n")
        
    #now for users
    
    
    
    #variables for user overview
    count_users = 0
    per_user_string = ""
    
    
    #read users from file
    with open("user.txt", "r+") as f:
    
        #for each user
        for line in f:
            
            #take away the \n from the end value
            line = line.replace("\n","")
            
            #split username and password
            line = line.split(", ")
            
            #count number of users
            count_users += 1
            
            #set user variables
            count_user_tasks = 0
            count_user_tasks_comp = 0
            count_user_tasks_incomp = 0
            count_user_overdue = 0
            perc_tasks_user = 0
            perc_tasks_user_comp = 0
            perc_tasks_user_incomp = 0
            perc_tasks_user_incomp_overdue = 0
            
            
            #read tasks from file
            with open("tasks.txt", "r+") as g:
            
                #for each task
                for tasks_line in g:
                
                    #take away the \n from the end value
                    tasks_line = tasks_line.replace("\n","")
                    
                    #split username and password
                    tasks_line = tasks_line.split(", ")
                    
                    #check if tasks is assigned to user
                    if tasks_line[0] == line[0]:
                        count_user_tasks += 1
                        
                        #check if task assigned to user is complete
                        if tasks_line[5] == "Yes":
                            count_user_tasks_comp += 1
                            
                        else:
                        
                            #count incomplete files
                            count_user_tasks_incomp += 1
                            
                            #check if overdue
                            task_due_date = datetime.strptime(tasks_line[4], '%d %b %Y')
                            today_date = datetime.today()#.strftime('%d %b %Y')
                            
                            if task_due_date < today_date:
                                count_user_overdue += 1
            
    
            if count_tasks > 0: #to prevent a division by 0 error
                perc_tasks_user = count_user_tasks / count_tasks * 100
                perc_tasks_user = round(perc_tasks_user,2)
            
            
            if count_user_tasks > 0: #to prevent a division by 0 error
            
                perc_tasks_user_comp = count_user_tasks_comp / count_user_tasks * 100
                perc_tasks_user_comp = round(perc_tasks_user_comp,2)
                
                perc_tasks_user_incomp = count_user_tasks_incomp / count_user_tasks * 100
                perc_tasks_user_incomp = round(perc_tasks_user_incomp,2)
                
                perc_tasks_user_incomp_overdue = count_user_overdue / count_user_tasks * 100
                perc_tasks_user_incomp_overdue = round(perc_tasks_user_incomp_overdue,2)
            
            
            
               
            
            #count_user_overdue
    
           
            #add string lines to user file string
            per_user_string += f"\tUser: {line[0]}\n"
            per_user_string += f"\t\tTotal tasks assigned: {count_user_tasks}\n"
            per_user_string += f"\t\tPercentage of total tasks assigned: {perc_tasks_user}\n"
            per_user_string += f"\t\tPercentage complete: {perc_tasks_user_comp}\n"
            per_user_string += f"\t\tPercentage incomplete: {perc_tasks_user_incomp}\n"
            per_user_string += f"\t\tPercentage incomplete & overdue: {perc_tasks_user_incomp_overdue}\n"
            per_user_string += "\t- - - - - - - - - - - - -\n"
            
            
    
    
    #rewrite to tasks overview file
    with open("user_overview.txt", "w") as f:
        f.write(f"\nUSERS OVERVIEW")
        f.write(f"\n_____________________________________\n")
        f.write(f"Total Number of Users: \t\t{count_users}\n")
        f.write(f"Total tasks: \t\t\t\t{count_tasks}\n")
        f.write(f"_____________________________________\n")
        f.write(f"PER USER INFORMATION:\n")
        f.write(f"\n{per_user_string}")
        
    

def disp_stats():
    #Tab spacing has been coded for the text file and might look different on the printed output.
    
    #print new line for space
    print("\n")
    
    #check if files exist, otherwise run gen_report function
    if os.path.isfile("task_overview.txt") == False and os.path.isfile("task_overview.txt") == False:
        gen_report()
        print("FALSEEEE")
    
    
    #read tasks_overview file
    with open("task_overview.txt", "r") as f:
        
        #loop through lines to count them
        for line in f:
        
            #each line is a task
            print(line)
            
    
    #read user_overview file
    with open("user_overview.txt", "r") as f:
        
        #loop through lines to count them
        for line in f:
        
            #each line is a user
            print(line)
            
    

#end of functions


#loop through login flow until a user is signed in
while logged_in_user=="" or logged_in==False:

    #user input
    username = input("Enter username: ")
    
    #read user database file
    with open("user.txt", "r") as f:
        
        #look for username
        for line in f:
        
            #take away the \n from the end value
            line = line.replace("\n","")
            
            #split username and password
            line = line.split(", ")
            
            #set variables if username found
            if (line[0]==username):
                logged_in_user = line[0]
                correct_password = line[1]
              
    #if username exists start password flow
    if logged_in_user!="":
        password = input("Enter password: ")
        
        if (password == correct_password):
            print(f"\nLogin successful! Welcome {logged_in_user}")
            
            #confirm login with logged_in boolean
            logged_in = True
        else:
            print("\nPassword Incorrect! Please try again.")
            
            #set logged_in_user to "" to start the process again
            logged_in_user=""
    else:
        print("\nUser does not exist! Please enter a valid username.")
        

#new section - after the login flow
if logged_in == True:

    #begin loop flow of main application
    app_active = True
    
    while app_active:
    
        #display menu if user has successfully logged in.
        print("\nPlease select one of the following options:")
        
        
        #additionally - if user is 'admin'
        if logged_in_user == "admin":
            print("\tr \t - \t register user")
        
        print("\ta \t - \t add task")
        print("\tva \t - \t view all tasks")
        print("\tvm \t - \t view my tasks")
        
        #additionally - if user is 'admin'
        if logged_in_user == "admin":
            print("\tgr \t - \t generate reports")
            
        #additionally - if user is 'admin'
        if logged_in_user == "admin":
            print("\tds \t - \t display statistics")
        
        print("\te \t - \t exit")
        
        
        #user input
        selected_option = input("Selection: ")

        #conditions for new user:
        if selected_option == "r" and logged_in_user=="admin": #additional condition to check if logged in user is admin
        
            #call reg_user function
            reg_user()
        
        #conditions for new task:
        elif selected_option == "a":
            
            #call add_task function
            add_task()
            
        #conditions to view all tasks:
        elif selected_option == "va":
        
            view_all()
        
       #conditions to view user's specific tasks:
        elif selected_option == "vm":
            
            view_mine()
            
        #conditions to generate user's reports:
        elif selected_option == "gr":
            
            gen_report()
            
        #conditions to display stats:
        elif selected_option == "ds" and logged_in_user=="admin": #additional condition to check if logged in user is admin
            
            disp_stats()
            
        #conditions to quit:
        elif selected_option == "e":
            
            print(f"\nSuccessfully logged out. Goodbye {logged_in_user}")
            
            #end the app loop
            app_active = False #it would not be most efficient to create an exit function for this one line of code
            
            
        else:
            #display general message
            print(f"\n{selected_option} is not an option. Please try again!")