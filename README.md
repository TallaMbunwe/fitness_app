# fitness_app
This is a fitness club membership application. 




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

