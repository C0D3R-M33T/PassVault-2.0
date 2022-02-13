#!/bin/python3
# write your root password within quotation in place of 'password' at line 50 and 219.
# you can also change your host name in place of 'localhost' at line 8
import mysql.connector , random
cnt1=3
cnt2=0
cnt4=0
hostip="localhost"
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%0123456789"
lst=list(s)
lst2=[]
def usernamegen(name):
    global lst2
    global lst
    namer=name
    for i in range(5):
        r1=random.choice(lst)
        namer+=r1
    #print("ok")
    if namer in lst2:
        usernamegen(name)
    else:
        return namer
def passwordgen():
    global lst
    r3=""
    r2=random.randint(10,15)
    for i in range(r2):
        r4=random.choice(lst)
        r3+=r4
    return r3
n=input("Enter your first name: ")
a=input("Are you a registered user ? (y/n): ")
if a in "yesYESYes":
    while cnt1>0:
        try:
            username=input("Enter your username: ")
            password=input("Enter your password: ")
            connector=mysql.connector.connect(host=hostip,user=username,passwd=password,database='pass')
            cursor=connector.cursor()
            if connector.is_connected():
                print("Access granted for username:",username)
                cnt4=1
            #connector.close()
            break
        except:
            cnt1-=1
            print("Username or password is wrong. Re-check and enter again.",cnt1,"tries left.")
elif a in "noNONo":
    connector=mysql.connector.connect(host=hostip,user='root',passwd='Ayan15@26#Yo')
    cursor=connector.cursor()
    cursor.execute('select user from mysql.user')
    data=cursor.fetchall()
    for i in data:
        lst2.append(i[0])
    b=input("Do you want some suggestions for username ? (y/n): ")
    if b in "yesYESYes":
        for i in range(10):
            t=usernamegen(n)
            print(t)
    elif b in "noNONo":
        print("Ok.")
    else:
        print("Error occurred.")
    while True:
        username=input("Enter your username: ")
        if username in lst2:
            print("Username already in use. Choose another username.")
        else:
            break
    c=input("Do you want some suggestions for password ? (y/n): ")
    if c in "yesYESYes":
        for i in range(10):
            t=passwordgen()
            print(t)
    elif b in "noNONo":
        print("Ok.")
    else:
        print("Error occurred.")
    password=input("Enter your password: ")
    # execution of sql commands start here
    st="create database if not exists pass"
    cursor.execute(st)
    connector.commit()
    st="create user '{}'@'{}' identified by '{}'".format(username,hostip,password)
    cursor.execute(st)
    connector.commit()
    st="use pass"
    cursor.execute(st)
    connector.commit()
    st="create table {}(website_application_name varchar(100),username_userid varchar(100),password_pin varchar(100))".format(username)
    cursor.execute(st)
    connector.commit()
    st="grant all on pass.{} to '{}'@'{}'".format(username,username,hostip)
    cursor.execute(st)
    connector.commit()
    connector.close()
    connector=mysql.connector.connect(host=hostip,user=username,passwd=password,database='pass')
    cursor=connector.cursor()
    if connector.is_connected():
        print("Access granted for username:",username)
        cnt4=1
    #connector.close()
else:
    print("Error occurred.")
if cnt4==1:
    print("Type out the number that is associated with the work you want to do from the following options: ")
    while True:
        try:
            print("1. Add new username and password for a website/application to the database.\n2. Generate a random and secured password.\n3. Retrieve password from the database.\n4. Update the existing password from the database.\n5. List out all the accounts/websites that are using a particular password.\n6. Display all the details stored in the database to the user.\n7. Delete user account.\n8. Delete all records from user's database.\n9. Delete particular records from user's database.\n10. Reset user's database password.\n11. Exit")
            p=input("Enter your choice: ")
            if p=="1":
                z=int(input("Enter the number of records to be entered: "))
                for i in range(z):
                    q=input("Enter the name of the website/application: ")
                    r=input("Enter the USERNAME/USER ID : ")
                    x=input("Enter the password: ")
                    st="insert into {} values('{}','{}','{}')".format(username,q,r,x)
                    cursor.execute(st)
                    connector.commit()
                print("Data added successfully.")
                suggest=input("Do you want to go back to the menu ? (y/n) ")
                if suggest in"yesYESYes":
                    continue
                else:
                    break
            elif p=="2":
                z=int(input("Enter the number of passwords you want to generate: "))
                for i in range(z):
                    t=passwordgen()
                    print(t)
                suggest=input("Do you want to go back to the menu ? (y/n) ")
                if suggest in"yesYESYes":
                    continue
                else:
                    break
            elif p=="3":
                while True:
                    try:
                        q=input("Enter the name of the website/application: ")
                        r=input("Enter the USERNAME/USER ID : ")
                        st="select password_pin from {} where website_application_name='{}' and username_userid='{}'".format(username,q,r)
                        cursor.execute(st)
                        data=cursor.fetchall()
                        if len(data)==0:
                            print("No such data found. Re-enter the details.")
                        else:
                            for i in data:
                                print("Password: ",i[0])
                            print("Data retrieved successfully.")
                        break
                    except:
                        print("No such data found. Re-enter the details.")
                suggest=input("Do you want to go back to the menu ? (y/n) ")
                if suggest in"yesYESYes":
                    continue
                else:
                    break
            elif p=="4":
                while True:
                    try:
                        q=input("Enter the name of the website/application: ")
                        r=input("Enter the USERNAME/USER ID : ")
                        x=input("Enter new password: ")
                        st="update {} set password_pin='{}' where website_application_name='{}' and username_userid='{}'".format(username,x,q,r)
                        cursor.execute(st)
                        connector.commit()
                        print("Data updated successfully.")
                        break
                    except:
                        print("No such data found. Re-enter the details.")
                suggest=input("Do you want to go back to the menu ? (y/n) ")
                if suggest in"yesYESYes":
                    continue
                else:
                    break
            elif p=="5":
                while True:
                    try:
                        q=input("Enter a password: ")
                        st="select website_application_name from {} where password_pin='{}'".format(username,q)
                        cursor.execute(st)
                        data=cursor.fetchall()
                        if len(data)==0:
                            print("No such data found. Re-enter the details.")
                        else:
                            print("Name of the websites are: ")
                            for i in data:
                                print(i[0])
                            print("Data retrieved successfully.")
                        break
                    except:
                        print("No such data found. Re-enter the details.")
                suggest=input("Do you want to go back to the menu ? (y/n) ")
                if suggest in"yesYESYes":
                    continue
                else:
                    break
            elif p=="6":
                st="select * from {}".format(username)
                cursor.execute(st)
                data=cursor.fetchall()
                if len(data)==0:
                    print("No such data found. Your database is empty.")
                else:
                    print("Website/Application,Username,Password/PIN")
                    for i in data:
                        print(i[0]+","+i[1]+","+i[2])
                    print("Data retrieved successfully.")
                suggest=input("Do you want to go back to the menu ? (y/n) ")
                if suggest in"yesYESYes":
                    continue
                else:
                    break
            elif p=="7":
                x=input("This will shut down the program immediately. Are you sure you want to delete your account ? (y/n): ")
                if x in "yesYESYes":
                    connector.close()
                    connector=mysql.connector.connect(host=hostip,user='root',passwd='Ayan15@26#Yo')
                    cursor=connector.cursor()
                    st="use pass"
                    cursor.execute(st)
                    connector.commit()
                    st="drop table if exists {}".format(username)
                    cursor.execute(st)
                    connector.commit()
                    st="drop user '{}'@'{}'".format(username,hostip)
                    cursor.execute(st)
                    connector.commit()
                    #connector.close()
                    print("User account deleted successfully.")
                    print("Goodbye.")
                    break
                elif x in "noNONo":
                    print("Cancelling.")
                    suggest=input("Do you want to go back to the menu ? (y/n) ")
                    if suggest in"yesYESYes":
                        continue
                    else:
                        break
                else:
                    print("Error occurred.")
            elif p=="8":
                x=input("Are you sure you want to delete all the data from your database ? (y/n): ")
                if x in "yesYESYes":
                    st="delete from {}".format(username)
                    cursor.execute(st)
                    connector.commit()
                    print("All data deleted successfully.")
                elif x in "noNONo":
                    print("Cancelling.")
                else:
                    print("Error occurred.")
                suggest=input("Do you want to go back to the menu ? (y/n) ")
                if suggest in"yesYESYes":
                    continue
                else:
                    break
            elif p=="9":
                while True:
                    try:
                        st="select * from {}".format(username)
                        cursor.execute(st)
                        data=cursor.fetchall()
                        if len(data)==0:
                            print("No such data found. Your database is empty.")
                        else:
                            q=input("Enter the name of the website/application: ")
                            r=input("Enter the USERNAME/USER ID : ")
                            for i in data:
                                if q==i[0] and r==i[1]:
                                    st="delete from {} where website_application_name='{}' and username_userid='{}'".format(username,q,r)
                                    cursor.execute(st)
                                    connector.commit()
                                    print("Data deleted successfully.")
                                    cnt2=1
                            if cnt2==0:
                                print("No such data found. Your database is empty.")
                        cnt2=0
                        break
                    except:
                        print("No such data found. Re-enter the details.")
                suggest=input("Do you want to go back to the menu ? (y/n) ")
                if suggest in"yesYESYes":
                    continue
                else:
                    break
            elif p=="10":
                x=input("Are you sure you want to change your database password ? (y/n): ")
                if x in "yesYESYes":
                    y=input("Enter new password for your database: ")
                    st="set password for '{}'@'{}'='{}'".format(username,hostip,y)
                    cursor.execute(st)
                    connector.commit()
                    print("Password updated successfully.")
                elif x in "noNONo":
                    print("Cancelling.")
                else:
                    print("Error occurred.")
                suggest=input("Do you want to go back to the menu ? (y/n) ")
                if suggest in"yesYESYes":
                    continue
                else:
                    break
            elif p=="11":
                print("Goodbye.")
                break
            else:
                print("There's no such choice. Re-enter your choice carefully.")
                suggest=input("Do you want to go back to the menu ? (y/n) ")
                if suggest in"yesYESYes":
                    continue
                else:
                    break
        except:
            print("Error occurred. Try again.")
    connector.close()
