Questions:

1>>> Explain how you implemented the checklist above step-by-step (not just following the tutorial).


    1>> Creating the Django project.

        1> I first made a folder called e-commerce-app and then iniated an environment in the same directory.
        2> I then made a requirements.txt file with the needed dependencies for the project and installed them. 
        3> After that, I configured the project and ran the server after adding "localhost" and "127.0.0.1" to the list of allowed hosts in settings.py. 
        4> I checked if the django application has been deployed successfully by visiting the link http://localhost:8000/ to see.
        5> I exited the virtual environment by typing deactivate.
        6> I created a repository on GitHub called 'e-commerce-app'.
        7> I created a gitignore file in the local folder.
        8> To start connecting my local repository with the GitHub one,
            I typed git branch -M main to initialize a new main branch called 'name'.
        9> Then I typed git remote set-url origin https://github.com/AmeeraKT/e-commerce-app.git to connect the local repo
            with the one on GitHub.
        10> I typed 'git add .' so that all changes I made will be recorded/
        11> Then I typed 'git commit -m "Created E Commerce App"' to establish all the changes to git.
        12> Finally I typed 'git push -u origin main' to transfer all the files I created on the local repo to the GitHub repo.
        13> I typed 'git status' to check if all changes have been committed.


    2>> Create an application with the name main in the project.

        1> I first typed in 'env\Scripts\activate' to enter the virtual environment in the terminal. This environment prevents
            conflicts from happening on the computer   
        2> Then I input the command 'Python manage.py startapp main' to create an application with the name main in the project
        3> I registered the application 'main' by adding it to the list of installed apps


    3>> Perform routing in the project so that the application main can run.
        1> I created a file called urls.py in the folder e-commerce-app
        2> I then added the following code in the file:
            from django.urls import path
            from main.views import show_main

            app_name = 'main'

            urlpatterns = [
                path('', show_main, name='show_main'),
            ]
        
    
    4>> Create a model in the application main with the name Product and have the mandatory attributes as follows.
        name
        price
        description

    5>> Create a function in views.py to return to an HTML template that displays the name of the application and your name and class.

    6>> Create a routing in urls.py for the application main to map the function created in views.py.
    
    7>> Perform deployment to PWS for the application that has been created so that it can be accessed by others via the Internet.
    
    8>> Create a README.md that contains a link to the PWS application that has been deployed, as well as answers to the following questions.

        1> I created the README.md file in the e-commerce-app folder locally and illed it with my answers and a link to the PWS application.
        2> I then pushed it to the PWS website using the command ...


2>>> Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.

    A 


3>>> Explain the use of git in software development!

    Git is used to keep track of changes done in projects done in code. Whenever a user alters the source code or adds or removes files, git will automatically detect actions like this then document and store the data. These changes then can be checked and committed
    with a messsage from the user with reasons or details for said change. Git is very useful in software developement while working with teams as users can check the changes that have been committed and their reasons. This allows a team to keep track of any updates and
    it also enables them to back track if any mistakes have been committed.

    Git also allows users to push local projects to Github quickly and easily, so their projects can be viewed publicly by others.



4>>> In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?

    Since Python is the most commonly used computer language, I believe that Django is a suitable introduction to learning software
    development as it requires Python.
    The syntax is also straightforward, simple and human-friendly enough to understand just like Python as a language. 



5>>> Why is the Django model called an ORM?

    ORM stands for 'Object Relational Mapper'. An ORM is a technique that essentially connects object oriented programs to relational
    databases. This allows programmers to interact with relational databases through object oriented programming. Django has an ORM which lets it change default database structures into Python classes so that they can be worked with in full Python language, meaning there
    is no need to use SQL language to create or manage a database.