# greenhouse


# Team members
- Alix
- Michael
- David
- Russell
- Julie

##Getting Up and Running

1. Clone Repo

1. Create a virtual environment
    `
    python3 -m venv <FOLDERNAME>
    `
1. Start the virtual environment

    For Mac Users
    `
    source /<VENV FOLDER>/bin/activate
    `

    For Windows Users

    Navigate to where your virtual environment folder is, and within that folder you should find another folder called Scripts, and within that a number of files. To start the virtual environment, you would need to run either the `activate.bat` or `activate.ps1`. To run, just type one of these files in your terminal, and press enter. If the start of the VM was successful, you should see `(<FOLDER NAME>)` printed in your terminal. This would be written before the PATH. 

    Run one of the following based on the following requirements:

    if using command prompt:

    `
    \<VENV FOLDER>\Scripts\activate.bat
    `

    or 

    if using powershell:

    `
    Run \<VENV FOLDER>\Scripts\Activate.ps1
    `

1. Install all dependecies

    `
    pip install -r requirements.txt

    `

1. Ensure that your IDE's Python Interpretor is set to the interpretor located in your virtual environment folder. This 
would be either in the `Scripts` folder if you are a Windows user, or in the `bin` folder for Linux and Mac users. The interpretor
would be the `python.exe` file. Have this set with your IDE. 


1. Start the flask development server
Set the Flask Environment global variable to be development

`
$env:FLASK_ENV:"development"
`

Set the location of the app.py file

`
$env:FLASK_APP:"be-server.app:app"
`

Then:

`
flask run
`