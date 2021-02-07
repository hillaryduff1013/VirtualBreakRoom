#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Function Definitions 
#Create a New Account
def CreateLogin(username, password):
    #Set the login information in the login_info file for the new users
    database = open("login_info", "a")
    database.write("\n")
    database.write(username)
    database.write("\t")
    database.write(password)
    database.close()

def GetInfo(fname,lname,empID,pEmail,DOB,s1,s2,s3, username, password):
    database = open("Database","a")
    database.write("Employee Number ")
    database.write(empID)
    database.write("\nUsername ")
    database.write(username)
    database.write("\nPassword ")
    database.write(password)
    database.write("\nFirst Name ")
    database.write(fname)
    database.write("\nLast Name ")
    database.write(lname)
    database.write("\nPersonal Email ")
    database.write(pEmail)
    database.write("\nDate Of Birth ")
    database.write(DOB)
    database.write("\nSecurity Question #1 ")
    database.write(s1)
    database.write("\nSecurity Question #2 ")
    database.write(s2)
    database.write("\nSecurity Question #3 ")
    database.write(s3)
    database.write("\n")
    database.write("\n")
    database.close()

#Login to an Existing Account
tryAgain = "yes"
def Login(username, password):
    global tryAgain
    #Set counters to check the length of the file with the amount of incorrect tries
    incorrect = 0
    count = 0
    #read each line in the file
    database = open("login_info", "r")
    for loginInfo in database:
        #Increase count to set the length of the file
        count += 1
        #set the username and password in their own variables
        login = loginInfo.split("\t")
        user = login[0]
        passphrase = login[1].strip("\n")
        #check if the user-entered username and password corresponds with one in the file
        if (username == user) and (password == passphrase):
            break
        else:
            incorrect += 1
    #Welcome them into the program or tell them to try again
    if (incorrect == count):
        print("Wrong Username or Password, Please Try Again")
    else:
        print("Welcome!")
        tryAgain = "no"
        


#Ask whether they want to create a new account or login to an existing account
accountType = input("Do You Want to Create a New Account? (Yes/No)")
accountType = accountType.lower()

if (accountType == "yes"):
    #Get the User to Answer All of the Questions
    fname = input("What is Your First Name? ")
    lname = input("What is Your Last Name? ")
    empID = input("Input your Employee ID Number ")
    pEmail = input("What is your personal email? ")
    DOB = input("What is your date of birth? ")
    s1 = input("What is your Mother's Maiden Name? ")
    s2 = input("What is the name of your first best friend? ")
    s3 = input("What street did you grow up on? ")
    username = input("Enter Your Desired Username")
    password = input("Enter Your Desired Password")

    #Input it in the database
    GetInfo (fname, lname, empID, pEmail, DOB, s1, s2, s3, username, password)
    print("completed database entry")

    #Input it into the login_info file
    CreateLogin(username, password)
    print("completed login_file entry")

    
else:
    #Login to a New Account
    while tryAgain == "yes":
        username = input("Enter Username ")
        password = input("Enter Password ")
        Login(username, password)
        #print(tryAgain)


# In[ ]:




