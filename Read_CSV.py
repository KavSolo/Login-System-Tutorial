import csv

filename = open('UserInfo.csv', 'r')

file = csv.DictReader(filename)

UserIDList = []
FirstNameList = []
LastNameList = []
UserPasswordList = []
UserEmailList = []

for column in file:
    UserIDList.append(column['UserId'])
    FirstNameList.append(column['FirstName'])
    LastNameList.append(column['LastName'])
    UserPasswordList.append(column['UserPassword'])
    UserEmailList.append(column['UserEmail'])

print("UserIdList: ", UserIDList)
print("FirstNameList: ", FirstNameList)
print("LastNameList: ", LastNameList)
print("UserPasswordList: ", UserPasswordList)
print("UserEmailList: ", UserEmailList)
