#Full Name: Kevin T Le

#Student ID: 2406054

#Chapman Email: kevle@chapman.edu

#Course Number and Section: CPSC 230-07

#In Class Programming Assignment 3: Loops; Exercise #1

#Purpose: This program asks the user to enter a username, password,
#and answers to three security questions to be stored into the program.
#Then, the program will prompt the user to sign into their username and password.
#The program will stop anyone from "logging into" a username if they
#do not get the password or any three security questions correct.

print("\n\nThe program’s main purpose is to secure your username and password against hackers.") #Explanation of the program

#Program prompts User to create new Username and Password.
username = input("\nCreate a new Username: \n\n")
password = input("\nCreate a new Password: \n\n")

print("\nTHE FOLLOWING QUESTIONS ARE CASE SENSITIVE.") #Explain that answers must have the same character case to be correct.

#Program asks three security questions to verify authorized users.
question_1 = input("\nSecurity Question 1: What is your Favorite Food? \n\n")
question_2 = input("\nSecurity Question 2: What Month were you Born in? \n\n")
question_3 = input("\nSecurity Question 3: What is Your Mother's Maiden Name? \n\n")

#Program prompts User to Sign In using stored Username and Password.
username_login = input("\nEnter your username: \n\n")

#Loop used to have User retype username if inputted username does not match the stored username.
while username_login != username:
    username_login = input("\nThis username does not exist. Try again:\n\n")

#After User enters stored username, program prompts for password.
password_login = input("\nEnter your password: \n\n")

#Conditions for Password if Password is Incorrect.
while password_login != password:

    answer_1 = input("\nIncorrect Password.\n\nSecurity Question 1: What is your Favorite Food? \n\nPlease enter here: ")
    if answer_1 == question_1: #If the Inputted Password is Incorrect, the User is prompted the First Security Question.
        break #User Logs In if they get the First Security Question correct.

    answer_2 = input("\nIncorrect Answer.\n\nSecurity Question 2: What Month were you Born in? \n\nPlease enter here: ")
    if answer_2 == question_2: #If the Answer to Question 1 is incorrect, the user is prompted the Second Security Question.
        break #User Logs In if they get the Second Security Question correct.

    answer_3 = input("\nIncorrect Answer.\n\nSecurity Question 3: What is Your Mother's Maiden Name? \n\nPlease enter here: ")
    if answer_3 == question_3: #If the Answer to Question 2 is incorrect, the user is prompted the Third Security Question.
        break #User Logs In if they get the Third Security Question correct.

    else: #If the Answer to Question 3 is incorrect, the user is prompted to re-enter their password and it loops back.
        password_login = input("All three answers are incorrect. Please re-enter your password: ")

print("\nSuccessfully logged in!\n") #The User is Logged In.
