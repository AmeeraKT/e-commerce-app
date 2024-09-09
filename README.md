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

    3>> Perform routing in the project so that the application main can run.
    Create a model in the application main with the name Product and have the mandatory attributes as follows.
    name
    price
    description

    4>> Create a function in views.py to return to an HTML template that displays the name of the application and your name and class.

    5>> Create a routing in urls.py for the application main to map the function created in views.py.
    
    6>> Perform deployment to PWS for the application that has been created so that it can be accessed by others via the Internet.
    
    7>> Create a README.md that contains a link to the PWS application that has been deployed, as well as answers to the following questions.



2.Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.

3.Explain the use of git in software development!

4.In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?

5.Why is the Django model called an ORM?