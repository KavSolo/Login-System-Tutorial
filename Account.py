import csv
import random
import Read_CSV

PasswordTest1 = "A"
PasswordTest2 = "B"
AppendList = []

class Person:
    UserId = 0
    FirstName = ""
    LastName = ""
    UserPassword = ""
    UserEmail = ""

    def SignUp():

        global PasswordTest1
        global PasswordTest2
        global AppendList

        Person.UserEmail = input("Enter Email: ").strip()

        for email in Read_CSV.UserEmailList:
            if Person.UserEmail == email:
                print("Account with this email already exists")
                Person.UserEmail = False
                break
            else:
                continue
        
        if Person.UserEmail != False:
            Person.FirstName = input("Enter First Name: ").strip()
            Person.LastName = input("Enter Last Name: ").strip()

            while PasswordTest1 != PasswordTest2:
                PasswordTest1 = input("Enter Password: ")
                PasswordTest2 = input("Enter Password Again: ")

            Person.UserPassword = PasswordTest1

            if len(Read_CSV.UserIDList) == 0:
                Person.UserId = 1
            if len(Read_CSV.UserIDList) != 0:
                lastID = Read_CSV.UserIDList[-1]
                Person.UserId = int(lastID) + 1
            
            print("Your Name is", Person.FirstName, Person.LastName)
            print("Email:", Person.UserEmail)
            print("Password:", Person.UserPassword)
            print("UserID:", Person.UserId)

            AppendList = [Person.UserId, Person.FirstName, Person.LastName, Person.UserPassword, Person.UserEmail]

            with open('UserInfo.csv', 'a', newline="") as f:
                writer = csv.writer(f)
                writer.writerow(AppendList)
                f.close()
        
        elif Person.UserEmail == False:
            Person.SignUp()

    def SignIn():

        index = -1
        listpassword = ""

        Person.UserEmail = input("Enter Email: ").strip()

        for email in Read_CSV.UserEmailList:
            index+=1
            if Person.UserEmail == email:
                Person.UserPassword = input("Enter Password: ")
                print(Read_CSV.UserPasswordList[index])
                listpassword = str(Read_CSV.UserPasswordList[index])
                print(Person.UserPassword)
                if Person.UserPassword.__eq__(listpassword):
                    print("Logged In!")
                    break
                else:
                    print("Incorrect Password")
                    Person.SignIn()

Person.SignIn()
