#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from flask import request, redirect

#Function Definitions 
#Create a New Account

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
        
@app.route("signup", methods=["GET", "POST"])
def signup():
    username = request.form['username']
    password = request.form['password']
    Login(username, password)
    return redirect ('index.html')
# In[ ]:




