def userPage():
    print(f"Select")
    print(f"Enter 1 for My Regimen, 2 for My Profile and 3 to Exit")

    #select connection Type i.e Login or Create Account
    entry_Types = ["My Regimen", "My Profile", "My Account", "Exit"]
    i=0
    try:
        while i<len(entry_Types):
            print(f"{i+1}. { entry_Types[i]}")
            i+=1
        choosen_user_role = int(input("Select Page: "))
        
            
        match choosen_user_role:
            case 1:
                print(f"My Regimen")
                userRegimen()
            #return "zero"

            case 2:
                print(f"My Profile")
                userProfile()
                userAccounting()

                #return "one"

            case 3:
                print(f"My Profile")
                userProfile()
                userAccounting()

                #return "one"

            case 4:
                print(f"Exit")
                #connection_page_page()
                return 0
            
            case default:
                print(f"Enter a correct digit for Entry Type number")
                #return "something"

    except ValueError:
        print(" Please enter the corresponing Integer")
        userPage()


def  userRegimen():
    print(f"Your Regimen")

    regimen = f""" 
            Monday : Chest
            Tuesday: Biceps
            Wednesday: Cardio
            Thursday: Triceps
            ...
            Sunday: Cardio
        
        """


    print(f"{regimen}")

def  userProfile():
    print(f"Your Profile")

    regimen = f""" 
            Name : Chest
            Age : Biceps
            Gender : Cardio
            Phone Number: Triceps
            ...
            BMI : Cardio
        
        """


    print(f"{regimen}")

def userAccounting():
    print(f"Your Accounting")

    accounting = f""" 
            Chest : 3.5€
            Biceps : 1.5€
            Swim : 2.0€ 
            Cardio : 3.0€ 
            Triceps : 2.5€
        
        """


    print(f"{accounting}")

if __name__  == "__main__":
    userPage()