# Table of Contents

1. [Milestone 1](#milestone-1--2oct-13oct)
2. [Milestone 2](#milestone-2--16oct-27oct)
3. [Milestone 3](#milestone-3--30oct-10nov)
<!-- 3. [Subsection 1.1](#subsection-1-1)
4. [Section 2](#section-2)
5. [Conclusion](#conclusion) -->

# Feedback | Group 1

## Milestone 1 | 2Oct-13Oct

1. **Define the problem:** <span style='color:green'>done</span>
    - Overall Good
    - By the end of 2nd milestone, it is expected to specify the CLV calculation method (we are going to cover it)
    - There is a need to define business settings
2. **Finalizing roles:** <span style='color:green'>done</span>
3. **Create a product roadmap and prioritize functionality (items):** <span style='color:red'>not done</span> 
    - The Front-End part is confusing. Are going to have a UI Layout? Where is DB developer?
    - In must-have, you have mentioned Visualizations?
4. **Creating the GitHub repository included readme.md and `.gitignore` (for Python) files:**  <span style='color:green'>done</span>
    - done partially:  during the remote repository initialization, you should have selected add .gitingorne with the Python option
5. **Create a virtual environment in the above repo and generate requirements.txt (`venv` must be ignored in git)** <span style='color:green'>done</span>
    - it seems you did with conda create, without adding  `--no-default-packages` option. As a result, we have a bunch of extra packages. 
    - please fix it and push it to GitHub by the end of Milestone 2 
6. **Push *point 1, point 3, point 5 (requirements.txt).*** <span style='color:red'>not done</span>: 
    - see point 5
7. **Complete the first chapter of  Developing Python Packages:** <span style='color:green'>done</span>
    - completed by everyone
8. **Create a private Slack channel in our Workspace and name it Group-{number}** <span style='color:green'>done</span>
9. **Schedule a call with me and Garo or come during the office hours:** <span style='color:green'>done</span>

By the end of the Milestone 2, you must complete the tasks mentioned above. Feel free to reach out if you have any questions.
- CLV calculation method
- Business Model
- Add high-level tasks for DB developer (this one you will find on Milestone 2  as well)
- Fix requirements.txt 

Grade 5/10


# Milestone 2 | 16Oct-27Oct

## Fixes From the Milestone 1

I can see that you have managed to fix:

- The requirements.txt
- `gitignore`

## Milestone 2


1. **DB developer:**
    - Design the database using Star schema (provide ERD): <span style='color:green'>done</span>
    - Insert Sample to data <span style='color:green'>done</span>
3. **Data Scientist:**
    - Complete data generation/acquisition/research: <span style='color:green'>done</span>
    - Select data from DB: <span style='color:green'>done</span>
    - Insert data to DB: <span style='color:green'>done</span>
    - <span style='color:red'>I couldn't reproduce data insertion as csv files are in data_csv folder,unlike in your code</span>
4. **API developer:**
    - Select data from DB <span style='color:green'>done</span>
    - Insert data to DB <span style='color:green'>done</span>
    - Update data in DB <span style='color:red'>wrong arguments</span>
5. Finish the second chapter of Datacamp course <span style='color:green'>done</span>
6. Finalize file/folder structure: relative imports must work properly <span style='color:red'>not done</span>
    - docs folder: putting all the documents there <span style='color:red'>not done</span>
    - models folder: putting modeling-related classes, functions <span style='color:red'>not done</span>
    - api folder: api related stuff <span style='color:red'>not done</span>
    - db folder: db related stuff <span style='color:red'>not done</span>
    - initialize `__init__.py` files accordingly (see Datacamp assignment chapter 1 and chapter 2) <span style='color:red'>not done</span>
    - logger folder: I will provide this module <span style='color:green'>done</span>

*I can see only Anahit's contribution on GitHub*  


In order to improve you performance I would recommend:

- approach the datacamp course seriously (it is obvious You are just taking the hints and completing it)
- come to office hours
- request calls **in advance**
- if you are stacking on one problem too long, it simply means you are doing it wrong: the goal of the project is not a panishment
- no need to have too much code, without proper environment setup



By the end of the 3rd Milestone you must:

Fix folders and their relationships. 

If you manage the complete the above points by Friday(before the class) you will get **20/20** 

**10/10**


# Milestone 3 | 30Oct-10Nov


1. Complete things from *Milestone 2*
3. remove M2 M1 folders, we need to have one folder- the name of the package, and its subfolder- modules
2. Finish the **third** chapter of Datacamp course (please complete only the 3rd one)
3. **API Developer:** 
    - Create a `run.py` file for an API (find the minimum workable example [here](https://github.com/hovhannisyan91/fastapi)) 
    - Test it on swagger
    - following request types must be available to test (GET, POST, PUT), will provide more details on Friday.
4. **DB developer:**
    - complete/fix the methods from `SQLHandler()` class
    - finalize the documentation for `schema.py` by using `pyment` package
    - finalize the documentation for `SQLHandler()` by using `pyment` package
5. **Data Scientist:** start working on modeling part, by selecting the date from SQL DB
    - we just need to run sample model and store the output to sql