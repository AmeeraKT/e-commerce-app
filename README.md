# == Assignment 2 Questions: ==

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
        1> I ran the command
                python manage.py runserver
        2> I checked the if the application is up, running and displayed properly by visiting this link http://localhost:8000/
    
    4>> Create a model in the application main with the name Product and have the mandatory attributes as follows.
        name
        price
        description

        1> I created a model in the models.py file in the main folder by adding the following code:
            from django.db import models

            class Product(models.Model):
                nameclass = models.CharField(max_length=255)
                name = models.CharField(max_length=255)
                price = models.IntegerField()
                description = models.TextField()

            I ensured that the class types matched the attributes 

    5>> Create a function in views.py to return to an HTML template that displays the name of the application and your name and class.
        1> I created a function that will display the details I want to show in the application
                def show_main(request):
                    context = {
                        'name' : 'Cookie',
                        'price': '5000',
                        'description': 'Homey chocolate chip cookies baked fresh everyday'
                    }

                    return render(request, "main.html", context)

    6>> Create a routing in urls.py for the application main to map the function created in views.py.
        
        1> I created a file called urls.py in the folder e-commerce-app
        2> I then added the following code in the file to configure URL routing for the main application:
                from django.urls import path
                from main.views import show_main

                app_name = 'main'

                urlpatterns = [
                    path('', show_main, name='show_main'),
                ]
        3> To configure URL routing for the project, I added the following code to the urls.py file in the e_commerce_app folder
                from django.urls import path, include
                path('', include('main.urls'))
    
    7>> Perform deployment to PWS for the application that has been created so that it can be accessed by others via the Internet.
        1>  I ran the command git remote add pws https://pbp.cs.ui.ac.id/ameera.khaira/ECommerceApplicationCookiePanda
        2> I then ran branch -M master
        3> Finally I ran push pws master to push to deploy my application to the PWS website
    
    8>> Create a README.md that contains a link to the PWS application that has been deployed, as well as answers to the following questions.

        1> I created the README.md file in the e-commerce-app folder locally and illed it with my answers and a link to the PWS application.
        2> I then pushed it to the PWS website using the command git push pws master


2>>> Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.

    The diagram can be viewed here:
    https://www.canva.com/design/DAGQa2NaV_w/lpAkdv4Nm4Nxq_DF9vyg2A/view?utm_content=DAGQa2NaV_w&utm_campaign=designshare&utm_medium=link&utm_source=editor

    The urls.py file handles any HTTP requests such as a user wanting to open a Django-based web application like in this assignment. Once the request is received,
    the show_main function in urls.py will call said function in views.py.

    The file views.py will call the show_main function with the request passed to it from urls.py as a parameter. The views.py file will then query the database containing the data of the objects which are stored in models.py.
    The views.py file will also look into the HTML file and organize the data obtained from models.py based on the format in main.html. The views.py file will then send a response, which is the way the web application and its data should be displayed on a browser, back to urls.py so the HTTP response is received and displayed on a browser.

    The file models.py contains information about the data types of the attributes, it provides the data of the web application to be displayed to views.py.
    
    The HTML file dictates how the data of the web application should be presented on a web browser. 


3>>> Explain the use of git in software development!

    Git is used to keep track of changes done in projects done in code. Whenever a user alters the source code or adds or removes files, git will automatically detect actions like this then document and store the data. These changes then can be checked and committed
    with a messsage from the user with reasons or details for said change. Git is very useful in software developement while working with teams as users can check the changes that have been committed and their reasons. This allows a team to keep track of any updates and
    it also enables them to back track if any mistakes have been committed.

    Git also allows users to push local projects to Github quickly and easily, so their projects can be viewed publicly by others.



4>>> In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?

    Since Python is the most commonly used computer language, I believe that Django is a suitable introduction to learning software
    development as it requires Python.
    The syntax is also straightforward, simple and human-friendly enough to understand just like Python as a language. 
    Django already creates a base template that's simple too so that users who are new to software development are able to familiarize
    themselves with it quicker.



5>>> Why is the Django model called an ORM?

    ORM stands for 'Object Relational Mapper'. An ORM is a technique that essentially connects object oriented programs to relational
    databases. This allows programmers to interact with relational databases through object oriented programming. Django has an ORM which lets it change default database structures into Python classes so that they can be worked with in full Python language, meaning there
    is no need to use SQL language to create or manage a database.


# == ASSIGNMENT 3 ==

1> Answer the following questions in README.md in the root folder.
 
    1>> Explain why we need data delivery in implementing a platform.
 
    2>> In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?
    
    3>> Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.

        The function is_valid() ensures that no faulty information is inputted into forms. This eliminates the need for administrators to read through and check forms that have wrong data inputted such as numbers in a query for words, thus saving time.
        This also prevents users from accidentally inputting the wrong or empty data in forms, giving them a chance to recheck their answers.
    
    4>> Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?

        They provide security.
    
    5>> Explain how you implemented the checklist above step-by-step (not just following the tutorial).

        1>>> Create a form input to add a model object to the previous app.

            1> I first created a base template for all the other web pages called base.html.
            2> I then added BASE_DIR / 'templates' in settings.py in e_commerce_app so that base.html will be detected as a base file.
            3> Next I added the following lines to main.html in main/templates {% extends 'base.html' %} {% block content %}{% endblock content %} so that the data in the django project will be loaded in HTML form easily.
            4> I then added the lines 'import uuid' and 'id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)'
            5> I then ran the following commands 'python manage.py makemigrations' and 'python manage.py migrate'
            6> To create the base of the form, I created a file 'forms.py' in main directory and created a new class ProductEntryForm
            7> I then added 'redirect' and these two lines 'from main.forms import ProductEntryForm' and 'from main.models import Product' at the top of views.py in main directory.
            8> In views.py, I then created a new function that takes a request and creates a form for the website.
            9> Then I added the following line in views.py 'product_entries = Product.objects.all()' so that the project can retrieve data about the Product objects from the database.
            10> To set up URL routing for the function that creates the form I added 'path('create-product-entry', create_product_entry, name='create_product_entry')' and imported create_product_entry.
            11> I then created create_product_entry.html that dictates how the form will be displayed on a web browser.
            12> Finally I added extra lines of code in main.html so that the table form can be displayed with a button.
        
        
        2>>> Add 4 views to view the added objects in XML, JSON, XML by ID, and JSON by ID formats. 

            1> I added these two libraries in views.py 'from django.http import HttpResponse' and 'from django.core import serializers'.
            2> In the same file, I added two functions show_xml and show_json that will translate the data into XML and JSON respectively before displaying them.
            3> In urls.py I imported the two functions above and added paths for them so that they can be routed to the view.
            4> To display the data in both XML and JSON by ID I added two more functions that display the two data types by ID in views.py
            5> In addition, I imported the functions and added URL paths for said functions in urls.py to complete URL routing

        
        3>>> Create URL routing for each of the views added in point 2.