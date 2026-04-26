# fitness_app
This is a fitness club membership application. 


MINI PROJECT: FITNESS CLUB MEMBERSHIP System


In this mini-project I will create a Simple Membership system for a fitness club using python, where Members can sign-up, sign-in, train, use special equipements. The system will track the members attendances, BMI (Body mass index), and endurance.  
I will need to apply Python core concepts such as Modules, APIs and OOP concepts like Classes, Inheritance, Encapsulation, Polymorphism, and Abstraction to build a flexible, reusable and well-structured game.

Requirements:

1. Modules:






2. APIs:








3. OOP:

3.1. Class Design:

Class: User (Abstract Base Class)

	Attributes: 

		- mame:

Class: Character (Abstract Base Class)

	Attributes:

		- name: The name of the character,

		- role: The user's role in the system (Admin, Trainer, Member, ).

		- role_id: Identity for access granting to user interfaces

		- date_of_birth: The date of birth of the user.

		- gender: The sex of the user

		- email: Email address bound to the user's account

		- phone_number: user's telephone number 

		- credit: numbers of sessions in months the member posseses 

	Methods:

		- __init__(self, name, role, date_of_birth, sex): Constructor to initialise
		  character attributes.

		- account_recharge (self): This method will add credits to a user.

		- credit_consumption (self): This method will deduce credit from a user's account

		- account_balance (self): This method will provide the current account balance.

		- age(self): gives user's age based on his date of birth. 

		- view_details (self): List the member's attributes (name, role, date_of_birth, 
		                       gender, email, phone_number, credit)



		- Abstract Method attack(self,other): This method will define how a character
		  attacks another character. Must be implemented by classes.

		- take_damage(self, damage): Reduces the character's health is by the amount of 
		  damage.

		- is_alive(self): Returns True if the character's health is above 0, False otherwise.

		- level_up(self): Increases the character's level and boosts stats like health
		  and attack power.



Class: Player (Inherits from Character)

	Attributes:

		- Experience: The amount of experience the player has accumulated.

		- Special_ability: A unique ability the player can use during battle.

	Methods:

		- __init__(self, name, health, attack_power, special_ability): Initialises a player
		  with a special ability.

		- attack(self,other): Allows the player to attack an opponent, reducing their
		  health.

		- use_special_ability(self,other): Uses the player's special ability to deal
		  extra damage or affect the opponent.



Class: Monster(Inherits from Character)

	Attributes:

		- monster_type: Type of the monster (e.g "Goblin", "Dragon").

		- attack_multiplier: A multiplier that increases the monster's attack damage.

	Methods:

		- __init__(self,name,health,attack_power, monster_type, attack_multiplier):
		  Initialises a monster with a type and attack multiplier.

		- attack(self,other): Attacks a player, causing damage based on the attack
		 multiplier



3.2. Encapsulation:

	- Keep attributes like health and experience private to prevent direct access from
	  outside the class. Use getters and setters to control how these attributes are modifiec

	- Ensure that the level_up() method increases stats like health and attack power safely
	 through encapsultation.


3.3. Inheritance:

	- Use inheritance to create a hierarchy where both Player and Monster inherit from the 
	  Character class.

	- Extend the base Character class by adding specific behaviors and attributes in the 
	  player and Monster subclasses.


3.4. Polymorphism:

	- Both the Player and Monster classes will have an attack() method, but they will behave
	  differently depending on the class. The Player may use special abilities, while the Monster
	  will have different attack strategies based on its type.


3.5. Abstraction:

	- The Character class should be abstract, meaning it cannot be instantiated on its own
	  Only specific characters like Player and Monster should be instantiated from this 
	  abstract class.

	- Hide the inner workings of methods like level_up() to keep the internal details abstract




Regimen Class:

def regimen(bmi):
	if bmi < 18.5 :
		r = {'Mon' : 'Chest', 'Tue' :'Biceps', 'Wed':'Rest', 'Thu': 'Back','Fri':'Triceps', 'Sat':'Rest', 'Sun':'Rest'}
	elif bmi >= 18.5 and bmi < 25 :
		r = {'Mon' : 'Chest', 'Tue' :'Biceps', 'Wed':'Cardio/Abs', 'Thu': 'Back','Fri':'Triceps', 'Sat':'Legs', 'Sun':'Rest'}
	elif bmi >= 25 and bmi < 30 :
		r = {'Mon' : 'Chest', 'Tue' :'Biceps', 'Wed':'Cardio/Abs', 'Thu': 'Back','Fri':'Triceps', 'Sat':'Legs', 'Sun':'Cardio'}
	elif :
		r = {'Mon' : 'Chest', 'Tue' :'Biceps', 'Wed':'Cardio', 'Thu': 'Back','Fri':'Triceps', 'Sat':'Cardio', 'Sun':'Cardio'}

	return r









I have created an email sender using SMTP 

    It requires python-dotenv package for storing environment variables such as email connection strings 
    refs:
    - https://www.youtube.com/watch?v=QJobMzcmoMo - How to Send Emails in Python with Gmail (SMTP Tutorial!)
    - https://www.youtube.com/watch?v=pyUyeepCOjE 

Create a GitHub Repository

    In the GitHub home page, select the Repositories tab.
    In the top right corner, click the New button to create a new repository.
    In the Create a new repository page, set the following paramters:

    Owner: Select yourself from the dropdown menu.
    Repository name: Enter TerraformCI.
    Add a README file: Check the box next to it.
    Add .gitignore: Enter terraform* and select Terraform from the dropdown menu.

    Click the Create repository button.

Configure Continuous Delivery

    Return to the browser window or tab with GitHub open.

    Click the Actions button.

    Create github actions

       Python application
       By Github Actions

    Create and test a Python application 

    add the following commands to the Test with pytest

	  pip install pytest
	  export PYTHONPATH=src
	  pytest
    
    Click the Start commit button to commit this to the main branch.

    Select Settings.

    In the left-hand navigation menu, select Secrets and variables under Security.

    Select Actions.

    Click the New repository secret button.

    Under Name, enter TF_API_TOKEN.

    Return to the browser window or tab with Terraform Cloud open.

    In the left-hand navigation menu, click the user profile icon in the top right corner of the menu.

    From the menu, select User Settings.

    In the left-hand navigation menu, select Tokens.

    Click the Create an API token button.

    Under Description, enter GitHub Actions.

    Click the Create an API token button.

    Copy the generated token.

    Return to GitHub and paste the token under Secret.

    Click the Add secret button.

Configure Branch Protection Rules

    In the left-hand navigation menu, under Code and automation, select Branches.
    Click the Add branch protection rule.
    Under Branch name pattern, enter main for the main branch.
    Click the checkbox next to Require a pull request before merging.
    Click the checkbox next to Do not allow bypassing the above settings.
    Click the Create button.

