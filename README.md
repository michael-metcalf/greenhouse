# MoneySprouts

**Get in the black, by going green!**
MoneySprouts is a progressive web app that helps its users to save money and accomplish their personal environmental goals at the same time.

![moneysproutslogin](https://user-images.githubusercontent.com/22274994/123038338-2555e300-d42b-11eb-88ed-d46bd99825de.PNG) | width=50, height=50

### Current Features Include:
* Environmental facts
* Monthly budget setting
* Monthly savings target setting
* Expense input
* Eco-action input

## Team members

* [Alix](https://github.com/AlixFachin)
* [David](https://github.com/DavidofOrange)
* [Julie](https://github.com/dawndarkness)
* [Michael](https://github.com/michael-metcalf)
* [Russell](https://github.com/RussellPacheco)


# Getting Up and Running 

## The Backend Environment

1. Clone Repo

1. Create a virtual environment

    ```
    python3 -m venv <FOLDERNAME>
    ```

1. Start the virtual environment

    <details><summary><b>For Mac Users</b></summary>

    ```
    source /<VENV FOLDER>/bin/activate
    ```

    If you are using the M1 chip, you may need to use python 3.7 to be able to run the environment.
    </details>

    <details><summary><b>For Windows Users</b></summary>

    Navigate to where your virtual environment folder is, and within that folder you should find another folder called Scripts, and within that a number of files. To start the virtual environment, you would need to run either the `activate.bat` or `activate.ps1`. To run, just type one of these files in your terminal, and press enter. If the start of the VM was successful, you should see `(<FOLDER NAME>)` printed in your terminal. This would be written before the PATH. 

    Run one of the following based on the following requirements:

    if using command prompt:

    ```
    \<VENV FOLDER>\Scripts\activate.bat
    ```

    or 

    if using powershell:

    ```
    Run \<VENV FOLDER>\Scripts\Activate.ps1
    ```
    </details>

1. Install all dependencies

    ```
    pip install -r requirements.txt
    ```

1. Ensure that your IDE's Python Interpretor is set to the interpretor located in your virtual environment folder. This 
would be either in the `Scripts` folder if you are a Windows user, or in the `bin` folder for Linux and Mac users. The interpretor
would be the `python.exe` file. Have this set with your IDE. 


1. Create config for the flask development server
Create a '.flaskenv' file in the be-server folder and set it's environment variables. 

    ```
    FLASK_APP=main.py
    FLASK_ENV=development
    ```

1. Start Flask
Make sure you are in the be-server directory!!! 

    ```
    flask run
    ```


1. Create Initial Migration File

    ```
    alembic revision --autogenerate -m "initial"
    ```

1. Seed

    ```
    alembic upgrade head
    ```

## The Frontend Environment

### fe-moneysprouts

The frontend environment must be set up from within the fe-moneysprouts folder.

### Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```
### Customize configuration
See Vue CLI [Configuration Reference](https://cli.vuejs.org/config/).

## Credits

* Icons were created using [font awesome](https://fontawesome.com/)
* Image credit goes to [Leo Wieling](https://unsplash.com/photos/gaP0QDorAj8)
