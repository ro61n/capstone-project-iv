# Capstone Project IV

Task Management System created with python. This project demonstrates a user-management system where tasks can be asssigned to users and where users have different controls based on administrative privileges. User and task data is read and written to text files.

The code is broken up into different functions which are positioned at the top of the 'task_manager.py' file. These serve different purposes from registering a user to adding/viewing tasks. There is also a function to generate a report which uses the data stored in text files to calculate statistics such as incompleted tasks and percentage overdue per user. These statistics are then written to task and user overview files to display in a user-friendly format.

Below the functions is the loop flow of the application. It first starts off with a login loop where the user has to enter a correct username and password. Once logged in, the user is displayed various options to choose from such as to generate a report or add a task. The admin user has more functionality. These options then run the functions described in the previous paragraph.

Robin Titus is the maintainer and contributor of this project.

To run this project, download it, and run the following command from your terminal: 'py task_manager.py'.
