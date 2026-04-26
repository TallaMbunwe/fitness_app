#import required modules csv, date, 
import os
import csv
import datetime

# create csv for connection user connection tracking
# Tracking data points user_email, login_date, 

def user_login_counter():

    # get user id for 
     
    # create user login count file

    print (f" This is creating the user account ")
    login_count_csv_file_path = "user_count_file.csv"

    # Create csv file to save user data
    if os.path.exists(login_count_csv_file_path):
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
                              userfile.write(f"{data[0]}, {data[1]}, {data[2]}\n")
                         
                         
    else:
         print("File does not exist, initialising it")
         with open(csv_file_path, mode="x",newline='') as userfile:

                fieldnames = ['user_email', 'login_date']
                writer = csv.DictWriter(userfile, fieldnames=fieldnames)
                writer.writeheader()
                userfile.write(f"{data[0]}, {data[1]}, {data[2]}\n")
    
    #return value for unit test
    return f"{data[0]}, {data[1]}, {data[2]}"



#with open(user_connection.csv,a)



