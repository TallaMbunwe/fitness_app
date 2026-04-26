import os
#import re
import csv

#from src.appUser import AppUser
from appUser import AppUser
#from mytotp import main
#import src.mytotp
import mytotp
#import src.userPage
import userPage

def main():
    # Connection/Access page
    connection_page()
    # Home page
    # home_page()
    # User's page
    #user_page()
   
    
def connection_page():
    print(f"Welcome to Bob Ds Gym")
    print(f"Enter 1 for Email/Login If already registered else enter 2 to create account")

    #select connection Type i.e Login or Create Account
    entry_Types = ["Create Account", "Login"]
    i=0
    while i<len(entry_Types):
        print(f"{i+1}. { entry_Types[i]}")
        i+=1
    choosen_entry_type = int(input("Entry Type Number: "))

    if choosen_entry_type == 1:
         newUser = get_user_credentials()
         create_user_account(newUser)

         #connection to home page
         connection_to_home_page()
      
    else:
         if choosen_entry_type == 2:
           #connection to home page
           connection_to_home_page()
           
#connection to home page
def connection_to_home_page():
           
           # Check if user exists to Log in
           newLogin = get_user_Login_credentials()
           #read_user_file()

           # Create user account if it does not exist
           Login_verification(newLogin)

           # user name and password check
           print(f" User logged in Successfully")
           # Connection counting
           connection_notification()
           #log_user_in()
           home_page()

def connection_notification():
     print (f"Welcome user : ")
         

def get_user_credentials():

    print(f" **** Account Creation ***** ")

    userLogin = input("Enter User Login from def: ")
    userRole = input("Enter user role from def: ")
    userEmail = input("Enter User Email from def: ")
    try:
        userPassword = input("Enter User Password from def: ")
        #print(f"Passwords do not match")
        userPasswordConfirmation = input("Enter User Password for confirmation from def: ")
    
        userPassword == userPasswordConfirmation

    except:
         print("Passwords do not match")
    
    userLoginCount = 0

    newAppUser = AppUser(name =userLogin , role = userRole, email= userEmail, password = userPassword, loginCount = userLoginCount)
    
    # Test user creation
    #print(newAppUser)
    #print(newAppUser.name)

    return(newAppUser)

    #pass


# Create user account, create csv file for users if not yet existing
# add user to file if it exists

def create_user_account(newUser: AppUser):
    #with open("userfile.csv", mode='w', newline='') as userfile:

    print (f" this is the new user for the create user acount {newUser}")
    csv_file_path = "userfile.csv"

    data = [newUser.name, newUser.email, newUser.password, newUser.loginCount]

    # Create csv file to save user data
    if os.path.exists(csv_file_path):
                    #Check user existance in file
                    login_check = user_login_verification(newUser)
                    print(f"{login_check}")

                    if login_check == 0:
                         pass
                    else:
                         # send an OTP to user for email verification
                         mytotp.totpCode(newUser.email)
                         #write user information in csv_file_path
                         with open(csv_file_path, mode="a",newline='') as userfile:
                              userfile.write(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}\n")
                         
                         
    else:
         print("File does not exist, initialising it")
         # send an OTP to user for email verification
         mytotp.totpCode(newUser.email)
         with open(csv_file_path, mode="x",newline='') as userfile:

                fieldnames = ['first_name', 'user_email', 'user_Password', 'login_count']
                writer = csv.DictWriter(userfile, fieldnames=fieldnames)
                writer.writeheader()
                userfile.write(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}\n")
    
    #return value for unit test
    return f"{data[0]}, {data[1]}, {data[2]}"

# Read user data csv file
def read_user_file():
    file_path = "userfile.csv"
    try:
        with open(file_path, "r") as file:
            content = csv.reader(file)

            user_emails = []
            for line in content:
                print(line)
                #print (f"user {line[1]} uses email {line[2]} with login count {line[3]}")
                user_email = line[1].strip()
                print(line[1])
                user_emails.append(user_email)
            #print(f"{user_emails}")
                                

    except FileNotFoundError:
               print("That file was not found Let me create it ")
        
    pass

# Verification method for registered users
def Login_verification(newLogin):
    csv_file_path = "userfile.csv"
    trans_csv_file_path = "trans_userfile.csv"
    print(f"This is Login verification for {newLogin[0]}")
    
    # Skip header with column titles in the csv sheet
    #next(csv_file_path)

    # get user login list
    try:
      with open(csv_file_path, "r") as file:
            content = csv.reader(file)

            user_emails = []
            for line in content:
                #print(line)
                print(f"user {line[1]} uses email {line[2]} with login count {line[3]}")
                user_email = line[1].strip()
                #print(line[1])
                user_emails.append(user_email)
                
    except FileNotFoundError:
               print("That file was not found Let me create it ")

    for email in user_emails:
      #if newUser.email == email:
      if newLogin[0] == email:
           #pUser = newUser.email
           print(f"User {newLogin[0]} found, connection successful")
           
           # increase login count 
           #new_loginCount = "n+1"
                    
                      
           try:
            # Update user file with login count
            # This involves creating a file object for reading and a file object for writing
            # I creates a temp csv file which later on replaces the original userfile
            with open(csv_file_path, mode='r') as infile, open(trans_csv_file_path, mode='w', newline='') as outfile:
                 reader = csv.DictReader(infile)
                 fieldnames = reader.fieldnames

                 writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                 writer.writeheader()

                 for row in reader:
                    strUserEmail = str(row["user_email"])
                    reqUserEmail = str(newLogin[0])
                    currentLoginCount = int(row["login_count"])

                    print(f" {row} from csv file opened for current login ")

                    if (strUserEmail.strip()) == (reqUserEmail.strip()):
                        #print(f'Column names are {", ".join(row)}')
                        print(f" updating {newLogin[0]} login count for current login")
                        currentLoginCount += 1

                        row["login_count"] = currentLoginCount
                        print(f" updating {row} login count to {row["login_count"]} for current login")
                        writer.writerow(row)

                    else:
                         writer.writerow(row)   


            #rename userfile.csv to olduserfile.csv, trans_userfile to userfile then 
            os.replace('userfile.csv', 'olduserfile.csv')  
            os.replace('trans_userfile.csv', 'userfile.csv')                   


           except FileNotFoundError:
                    print("That file was not found Let me create it ")

           break
      else:
           #print(f"User {newUser.email} Not found, connection Failed")
           print(f"User {newLogin[1]} Not found, connection Failed")
           #pass
    pass
     
def account_verification(newUser):
    csv_file_path = "userfile.csv"
    print(f"This is account verification for {newUser.name}")

    # get user login list

    try:
      with open(csv_file_path, "r") as file:
            content = csv.reader(file)

            user_emails = []
            for line in content:
                # print(line)
                user_email = line[1].strip()
                #print(f"user {line[1]} uses email {line[2]} with login count {line[3]}")
                print(line[1])
                user_emails.append(user_email)
                
    except FileNotFoundError:
               print("That file was not found Let me create it ")
    # return (user_emails)

    for email in user_emails:
      if newUser.email == email:
           #pUser = newUser.email
           print(f"User {newUser.email} found, connection successful")
           break
      else:
           #print(f"User {newUser.email} Not found, connection Failed")
           pass
    pass


def user_login_verification(newUser):
    csv_file_path = "userfile.csv"
    print(f"This is account verification for {newUser.name}")

    # get user login list

    try:
      with open(csv_file_path, "r") as file:
            content = csv.reader(file)

            user_emails = []
            for line in content:
                #print(line)
                user_email = line[1].strip()
                print(line[1])
                print(f"user {line[1]} uses email {line[2]} with login count {line[3]}")
                user_emails.append(user_email)

            #print(f"{user_emails}")
                
    except FileNotFoundError:
               print("That file was not found Let me create it ")

    
    # return (user_emails)

    for email in user_emails:
      if newUser.email == email:
           #pUser = newUser.email
           print(f"User {newUser.email} already exists")
           #break
           return (0)
      else:
           #print(f"User {newUser.email} Not found, Account creation underway ")
           pass
           #return 1
    pass


def get_user_Login_credentials():

    print(f" **** Login to your Account ***** ")

    userLogin = input("Enter User Login/email: ")
    userPassword = input("Enter User Password from def: ")

    #newAppUser = AppUser(name =userLogin ,  password = userPassword)
    check_user_password(userLogin,userPassword)

    return (userLogin, userPassword)

#Check user password and validate
def check_user_password(userLogin,userPassword):
    csv_file_path = "userfile.csv"
    try:
      with open(csv_file_path, "r") as file:
            content = csv.reader(file)

            user_emails = []
            user_passwords = []
            for line in content:
                #print(line)
                user_email = line[1].strip()
                user_password = line[2].strip()
                #10/11 print(line[1], line[2])
                print(f"{line[1]} {line[2]} is line 1")
                user_emails.append(user_email)
                user_passwords.append(user_password)

            #10/11 print(f"{user_emails} user logins from check_user_password")
            #10/11 print(f"{user_passwords} user passwords from check_user_password")

            login_password_dic= {}
            #i=0
            l = len(user_emails)
            print(f"This is the users email list {user_emails}")

            if userLogin not in user_emails:
                 print (f" User Not Found")
                 get_user_Login_credentials()
            else:
            #while (i <= l):
                for i in range(len(user_emails)):
                    login_password_dic[user_emails[i]] = user_passwords[i]
                    
                    if (userPassword == login_password_dic[user_emails[i]]) & (userLogin == user_emails[i]):
                            if userLogin == user_emails[i]:
                                print (f"{login_password_dic[user_emails[i]]} and user Login {user_emails[i]} and print userLogin variable {userLogin}")
                                #userLogin 
                            else:
                                print (f" Wrong password or Login")
                                get_user_Login_credentials()
                    elif  userLogin == user_emails[i] :
                                print (f" Wrong password or Login")
                                #i+=1
                                get_user_Login_credentials()
                    else:
                        #i+=1
                        pass
                
    except FileNotFoundError:
               print("That file was not found Let me create it ")


# Check User OTP on 

# Home page for Admin, Member, Visitor menu
def home_page():
    print(f"Select")
    print(f"Enter 1 for Admin, 2 for Member and 3 to Exit")

    #select connection Type i.e Login or Create Account
    entry_Types = ["Admin", "Member", "Trainer", "Exit"]
    i=0
    try:
        while i<len(entry_Types):
            print(f"{i+1}. { entry_Types[i]}")
            i+=1
        choosen_user_role = int(input("Entry user role: "))
        
            
        match choosen_user_role:
            case 1:
                print(f"Admin")
            #return "zero"
            case 2:
                print(f"Member")
                userPage.userPage()
                #return "one"
            case 3:
                print(f"Trainer")
                #return "two"
            case 4:
                print(f"Exit")
                #connection_page_page()
                return 0
            case default:
                print(f"Enter a correct digit for Entry Type number")
                #return "something"

    except ValueError:
        print(" Please enter the corresponing Integer")
        home_page()
      

if __name__ == "__main__":
    main()
