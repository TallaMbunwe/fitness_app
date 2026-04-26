import csv


class AppUser:

    #def __init__(self, name, role, email, password,):
    def __init__(self, name, role, email, password, loginCount, subscriptionCredit):
        self.name = name
        self.role = role
        self.email = email
        self.password = password
        self.loginCount = loginCount
        self.subscriptionCredit = subscriptionCredit


    def __str__(self):
        return f" New User: {self.name}, {self.role}, {self.email}, {self.password}, {self.loginCount}" 

    def credit(self):
        credit = self.subscriptionCredit - self.loginCount
        return credit


    # To protect the role attribute from manual or adverserial change I use the following decorators for the getter and a setter 
    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, role):
        if role not in ["Admin", "Member", "Trainer", "Guest"]:
            raise ValueError ("Invalid role")
        self._role = role


    """ 
    @property
    def loginCount(self):
        return self._loginCount
    
    @loginCount.setter
    def loginCount(self, email, loginCount):
        
        file_path = "userfile.csv"
        try:
            with open(file_path, "r") as file:
                content = csv.reader(file)

                for line in content:
                    if email == line[1].strip():
                        print (f"user {line[1]} uses email {line[2]} with login count {line[3]}")
                    else:
                        pass

                #print(f"{user_emails}")
                    

        except FileNotFoundError:
                print("That file was not found Let me create it ")
                

        self._loginCount = 0
        """
""" 
    @property
    def email(self):
        return self._email
    
    @email.setter
    def role(self, email):
        #if role not in ["Admin", "Member", "Trainer"]:
        #    raise ValueError ("Invalid role")
        self._email = email

        """