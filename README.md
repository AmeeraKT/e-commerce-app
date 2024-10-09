<details>
<summary>ASSIGNMENT 6 </summary>

# == ASSIGNMENT 6 QUESTIONS AND ANSWERS: =

 ## 1. Explain the benefits of using JavaScript in developing web applications!
    Java script supports object-oriented, imperative, event-driven and functional programming. This allows web developers to create complex functions that can work on websites. It can increase interaction between web pages and users and enables dynamic page manipulation.   In event-driven programming which increases web page and user interaction, some functions can be run after a certain event is triggered on the website at any time. 
    For example clicking on a button that changes the color of the website will immediately make the website change color. JavaScript can also create buttons on websites that will change color once clicked on or make the website automatically change appearance based on the time of the day, which all increase interactivity. Another example is this dynamism technique called AJAX or Asynchronous JavaScript And XML.
    With AJAX, asynchrnous data exchange between the server and browser can occur in the background. AJAX can also send data in different file types to the server.
    In addition, JavaScript code is not executed on the server side but on the client side, hence the server performance is not affected if many users are interacting with the website, rather the performance of the website depends on the user's device specifications. JavaScript can also let certain parts of a page get updated without refreshing the entire page.
 
 ## 2. Explain why we need to use await when we call fetch()! What would happen if we don't use await?
    The await function is used to tell the web browser to wait for the result or promise of an async function before the rest of that function is executed. Without an await keyword the function will be executed synchronously and not asynchronously. Await keywords make sure that the function will be executed step by step in the background.
 
 ## 3. Why do we need to use the csrf_exempt decorator on the view used for AJAX POST?
    The decorator tells Django to not check the CSRF token when a POST request is sent with AJAX. This eliminates the need for the user to get their CSRF token checked for validation each time AJAX POST is requested.
 
 ## 4. On this week's tutorial, the user input sanitization is done in the back-end as well. Why can't the sanitization be done just in the front-end?
    Since front-end sanitization does not cover client-side code manipulation tactics such as XSS or injection attacks such as with SQL, implementing back-end sanitization is necessary.

 ## 5. Explain how you implemented the checklist above step-by-step (not just following the tutorial)!
    
    Modify the previously created assignment 5 to use AJAX.

    1. AJAX GET:
        a.  Modify the codes in data cards to able to use AJAX GET.

            1. In main.html in main/templates I added the code below so that it can retrieve data with AJAX
  <html>  
      <script>
          async function getProductEntries(){
              return fetch("{% url 'main:show_json' %}").then((res) => res.json())
          }
      </script>
  </html>
        b. Retrieve data using AJAX GET. Make sure that the datas retrieved are only the datas belonging to the logged in user.
        
            1.  To do this, I changed the paramater in Product.objects.filter from pk=id to user=request.user in views.py
   
   ```python
           def show_xml_by_id(request, id):
               data = Product.objects.filter(user=request.user)
               return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

           def show_json_by_id(request, id):
               data = Product.objects.filter(user=request.user)
               return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```
   
    2. AJAX POST:
        a. Create a button that opens a modal with a form for adding a mood entry.

            1. In main/templates main.html, I inserted code that with the help of Tailwind will create a modal

   <html>
                <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
                    <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
                        <!-- Modal header -->
                        <div class="flex items-center justify-between p-4 border-b rounded-t">
                        <h3 class="text-xl font-semibold text-gray-900">
                            Add New Product Entry
                        </h3>
                        <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
                            <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="sr-only">Close modal</span>
                        </button>
                        </div>
                        <!-- Modal body -->
                        <div class="px-6 py-4 space-y-6 form-style">
                        <form id="ProductEntryForm">
                            <!-- Added csrf token -->
                            {% csrf_token %}
                            <div class="mb-4">
                            <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                            <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-blue-700" placeholder="Enter cookie name" required>
                            </div>
                            <div class="mb-4">
                            <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
                            <textarea id="price" name="price" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-blue-700" placeholder="Enter the price" required></textarea>
                            </div>
                            <div class="mb-4">
                            <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                            <input type="text" id="description" name="description" min="1" max="10" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-blue-700" placeholder="Enter the description" required>
                            </div>
                        </form>
                        </div>
                        <!-- Modal footer -->
                        <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
                        <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
                        <button type="submit" id="submitProductEntry" form="ProductEntryForm" class="bg-blue-700 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
                        </div>
                    </div>
                    </div>
   </html>
   
            2. I also added this to make a button for opening the modal form for making a cookie entry with AJAX
<html>
                        <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-blue-800 hover:bg-blue-900 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
                            Add New Cookie Entry by AJAX
                        </button>
</html>

        b. Create a new view function to add a new mood entry to the database.

            1. I imported the following in views.py
<html><
      from django.views.decorators.csrf import csrf_exempt
      from django.views.decorators.http import require_POST
</html>

            2. I then created a new function called add_mood_entry_ajax to add new moods with AJAX in views.py

```python
                @csrf_exempt
                @require_POST
                def add_product_entry_ajax(request):
                    name = strip_tags(request.POST.get("name"))
                    price = strip_tags(request.POST.get("price"))
                    description = strip_tags(request.POST.get("description"))
                    user = request.user

                    new_product = Product(
                        name=name, price=price,
                        description=description,
                        user=user
                    )
                    new_product.save()

                    return HttpResponse(b"CREATED", status=201)
```

            3. Next I did URL routing for the new function by importing add_product_entry_ajax in urls.py

        c. Create a /create-ajax/ path that routes to the new view function you created.

            1. To do this, I added this line path('create-mood-entry-ajax', add_mood_entry_ajax, name='add_mood_entry_ajax') in urpatterns in urls.py

        d. Connect the form you created inside the modal to the /create-ajax/ path.

            1. I connected it by adding the function addProductEntry() in main.html in main/templates. The line that connects the modal to creating a new product entry with AJAX is this fetch("{% url 'main:add_product_entry_ajax' %}" ...).

 <html>
        <script>
                function addProductEntry() {
                    const form = document.querySelector('#ProductEntryForm'); 
                    const formItems = new FormData(form);
                    fetch("{% url 'main:add_product_entry_ajax' %}", {
                        method: "POST",
                        body: formItems,
                    })
                    .then(response => {
                        if (response.ok) {
                        refreshProductEntries();
                        form.reset();
                        } else {
                        alert('Failed to add cookie.');
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        alert('An error occurred.');
                    });
                    return false;
                    }    
        </script>
</html>

        e. Perform asynchronous refresh on the main page to display the latest item list without reloading the entire main page.

            1. Asynchronous refresh happens automatically after I create a new product entry with AJAX. This snippet of code refreshese the page automatically after a product entry is made with AJAX as it calls hideModal();.
<html>
              <script>
                document.getElementById("ProductEntryForm").addEventListener("submit", (e) => {
                    e.preventDefault();
                    addProductEntry();
                    hideModal();
                    })
               </script>
</html>

        f. Making AJAX GET and AJAX POST secure
            
            1. I added this line in views.py and forms.py
                from django.utils.html import strip_tags

            2. I then added strip_tags in the following code snippets:

                This snippet is in forms.py:
                    def clean_name(self):
                        name = self.cleaned_data["name"]
                        return strip_tags(name)

                    def clean_price(self):
                        price = self.cleaned_data["price"]
                        return strip_tags(price)
                    
                    def clean_description(self):
                        description = self.cleaned_data["description"]
                        return strip_tags(description)
                        
                This snippet is in views.py:
                    @csrf_exempt
                    @require_POST
                    def add_product_entry_ajax(request):
                        name = strip_tags(request.POST.get("name"))
                        price = strip_tags(request.POST.get("price"))
                        description = strip_tags(request.POST.get("description"))
                        ...



</details>

<details>
<summary>ASSIGNMENT 5</summary>

# == ASSIGNMENT 5 QUESTIONS AND ANSWERS: ==

 ## 1. If there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors!

    There are four CSS selectors: inline styles, ID selectors, classes selector and element selector.
    The most prioritized are the inline styles and the least prioritized are the element selectors.

    Each selector has a specifity value, with inline styles having the highest value. Selectors with the higher value are prioritized more.

 
 ## 2. Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!

    Responsive design is important because it ensures that a website fits the resolution of the device it is being viewed on. Websites should look like it fit the screens of desktops, mobile phones and tablets because if they did not then navigating them would be tedious. For instance, a user navigating a website that is meant to fit a desktop screen on a mobile phone would have to scroll a lot or some buttons on the website would be unaccessible, essentially making the website unuseable -this is unresponsive design.

    For example the Fasilkom SCELE website has responsive design because it can fit both on a desktop and mobile phone screen.  
        
    Responsive design makes interacting with websites more engaging and they provide the user with feedback and information regarding their actions on the website. Responsive designs can also indicate if the website is working properly or not. In addition, responsive design follows some of Shneideran's 8 Golden Rules of Interface Design which is offering informative feedback, seek universal usability, strive for consistency and supporting internal locus of control.
    
    For example in the mental health tracker website when the cursor hovers over the mood card, it rotates slightly. Another example are buttons that change color when hovered or clicked on.

    Unresponsive design is the opposite. For example buttons can be unresponsive when they are disabled, meaning they cannot be clicked.
 
 ## 3. Explain the differences between margin, border, and padding, and how to implement these three things!
 
    The CSS box model consists of a margin, border, padding and content. With the margin and padding on the outermost and innermost areas respectively. 
    The margin is an area around the border, padding and content.
    The border is an area around the content and padding.
    The padding is an area inside the content.

    There are ways to implement the margin, border and padding which are all implemented in the global.css file.
    
    The border can be used in various to style areas around text which is content. They are used to enclose text in a box and the color and thickness of the border can be styled. Examples of such ways as follows border-color: #674ea7, border: 2px solid #bcbcbc; and border-radius: 0.375rem. Borders can also be used to style buttons.

    The padding can be used to style buttons, header, forms and content sections. It specifies color and the area the content will occupy. and  For example this is padding used for a header's dimensions, 20px 20px 20px 40px. In another example, giving a button padding: 10px means that it will be 10 pixels in length and height. Padding color can be changed through this way background-color: rgb(231, 168, 86).

    The margin can be used to style content sections and for managing the placement of the layers inside of the CSS box model. It can be used to justify, or align ext and content to the left or right. For example margin: 0 auto; means that the content will be placed in the center of a the CSS box and a margin can be added to the top, left, right or bottom of content. For example margin-top: 20px; means that the closest other content can be above the first content is 20 pixels.

    Here is an example of all three aspects used together:

    .box-element {
            margin: 30px; /* the space outside the element */
            border: 2px solid black; /* the border around the element */
            padding: 20px; /* the space inside the element */
        }
    
 ## 4. Explain the concepts of flex box and grid layout along with their uses!

    The flex box is a CSS3 layout and is backwards compatible. It eliminates the need to use float and positioning for content such as margins. To create a FlexBox, a flex container has to be made. For example, this flex container:
    <div class="flex-container">
        <div>1</div>
        <div>2</div>
        <div>3</div>
    </div>
    looks like a long blue rectangle with three smaller white squares in it with the numbers 1, 2 and 3 on each box in black, default arial font.
    To make it flexible, its display must be set this way
    .flex-container {
        display: flex;
    }.

    A flexible flex box can be used to stack flex items horizontally or vertically in the flex box, to add the order of stacking can be changed as well. Flex items can also be warped, not warped or warped in reverse order in the flex box.
    Flex items can also be justified and aligned in various ways.

    The flex items can also have their size, order and alignment stylized. To add, the area of the entire flex box can be warped to fit on both desktop and mobile phone screens.


    The grid layout is a module that uses rows and columns and seperates the space of a webpage into two-dimensional sections. It is used for exact placement of images or items and for creating complex layouts. Grid layouts also enable layering of items.

 ## 5. Explain how you implemented the checklist above step-by-step (not just following the tutorial)!

    1. Implement functions to delete and edit products.

        1. I created a new function called edit_product in views.py.
    
        2. I then imported reverse as part of the django.shortcuts.

        3. In main/templates I made a file called edit_product.html.

        4. I then made URL routing for the edit_product.html so that my project will be able to handle editing requests and actually edit products.

        5. In main.html in main/templates I added code to create a button for editing products

        6. In views.py I created a function that will delete products 

        7. Next I did URL routing for delete_products

    2. Customize the design of the HTML templates that have been created in previous assignments using CSS or a CSS framework (such as Bootstrap, Tailwind, Bulma) with the following conditions:

        2. a. Customize the login, register, and add product pages to be as attractive as possible.

            1. In the templates directory I connected my Django project with Tailwind by adding the line below
            <script src="https://cdn.tailwindcss.com"> </script>.

            2. Then I created a new directory in root called static/css and created a file called global.css.

            3. I then linked global.css in base.html by adding     <link rel="stylesheet" href="{% static 'css/global.css' %}"/>

            4. In global.css I added some styles so that the style on every page will be consistent.

            5. Then I updated the code of login.html in /main/templates to stylize it

            6. Next, I changed the code of register.html in the same directory to add styles

            7. To create the product page I added product_card.html in /main/templates

            8. To display the styled product cards, I changed the code in main.html in /main/templates by including product_card.html


        2. b. Customize the product list page to be more attractive and responsive. Then, consider the following conditions:

            i. If there are no products saved in the application, the product list page will display an image and a message that no products are registered.
            
                1. To allow my project to display images I went to settings.py in /e_commerce_app and added 'whitenoise.middleware.WhiteNoiseMiddleware' in the MIDDLEWARE section.

                2. Then I created a new directory in root called /static/css and created a folder called images in /static

                3. I added a png image of a sad face in /static and named it sad.png

                4. To display the image, I added a path to it in main.html

                5. To ensure that it will appear if there are no products available, I created an if statement {% if not product_entry %} and included the image source below it

                6. I also added text stating that "There are no cookies data in Cookie Panda."
 
            ii. If there are products saved, the product list page will display details of each product using cards (must not be exactly the same as the design in the Tutorial!).

                1. Following the if statement from earlier, to display the details of each product I created an else statement {% for product_entry in product_entries %}
            
                2. Under this statement I included the product cards that will present the product details

                3. I customized the design of each card in card_product.html

    3. For each product card, create two buttons to edit and delete the product on that card!

        1. I put the buttons in card_product.html in their own class
        
        2. I then set their colors to blue

        3. The edit and delete button are url routed to edit_product and delete_product respectively so that they can both do what they are supposed to do

    4. Create a navigation bar (navbar) for the features in the application that is responsive to different device sizes, especially mobile and desktop.

        1. To make sure that the website is responsive to different device sizes in general, I added this line in base.html in /templates
             <meta name="viewport" content="width=device-width, initial-scale=1">.
        
        2. To start, I created a file called navbar.html in templates/ directory and filled it with code that will stylize it.

        3. I then linked the navbar.html to main.html, edit_product.html and create_product_entry.html by adding this line {% include 'navbar.html' %} below {% block content %}.

        4. I set the color of the navigation bar to yellow.

        5. The code in navbar.html is divided into two parts, the first part is for showing up on desktops while the other part is for showing up on mobile phones.

</details>

<details>
<summary> ASSIGNMENT 4 </summary>

# == ASSIGNMENT 4 QUESTIONS AND ANSWERS: ==

## 1. What is the difference between HttpResponseRedirect() and redirect()?

    HttpResponseRedirect() takes a URL as the first argument. It's used to direct the user between different web pages on a browser that have a URL.
    While redirect() is more flexible because it can take URLs, models and views as a parameter. This function will return a HttpResponseRedirect to the respective URL of the parameter given.
    In this app, it's used to bring the user back to the main page after creating an account. It's shown in this code snippet:
            
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')

## 2. Explain how the Product model is linked with User!
    
    The product model is linked with every user via foreign key as shown here in models.py

    class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    So each instance of a product model along with all the data of said model is associated with one user

    In views.py, when a product is created it is associated with a user as shown here, as well as the data associated with the product created by the user

                product = form.save(commit=False)
                roduct.user = request.user
 
## 3. What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.

    Authentication is the process of verifying the correct identity of a user logging in.
    While authorization is granting said users persmissions for actions based on their role or level in the database, for example an admin of a database has permission to read and write all data.

    When a user logs in, they first undergo authentication.
    Using the AuthenticationForm module, Django checks if both the username and password inputted both match a user account's login information in the database. When both match then the user logging in is granted access to the website. The get_user() function is ran and it retrieves the user model, alongside all the models and data associated with said user. While getting logged in, Django checks what roles, levels or permission the logged in user has and grants them their permissions. The user is then redirected to the main  page. The login function gives the user a session ID and their requests are tracked via cookies.

    Django uses the modules below for authentication:

    from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
    from django.contrib.auth import authenticate, login, logout
    from django.contrib.auth.decorators import login_required

    This decorator @login_required(login_url='/login') restricts website access to users who are logged in, this is a form of authorization.

## 4. How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.

    It remembers logged-in users based on cookies and sessions. When a user logs in, a cookie is created with a session ID and CSRF Token associated with the same user on their web broswer. This cookies data is stored on the server side and every time the user makes a request, their session ID and cookie is checked. This allows Django to identify the user based on their session ID and cookies and retrieve data associated with the user's session.

    Cookies can be used to track and study how a user interacts with a website, store items put in a shopping cart and maintain website preferences of the user.

    Cookies that are not secure are not safe to use and they can be used maliciously if stolen from users by hackers, allowing them to impersonate them. 

 
## 5. Explain how did you implement the checklist step-by-step (apart from following the tutorial).
  
    1. Implement the register, login, and logout functions so that the user can access the application freely.
    

        1. I first activated the python environment
        
        2. I then exported the following functions to views.py

            from django.contrib.auth.forms import UserCreationForm
            from django.contrib import messages

            So that user accounts can be created

        3. There needs to be a function that uses the UserCreationForm module so I added this in views.py

            def register(request):
                form = UserCreationForm()

                if request.method == "POST":
                    form = UserCreationForm(request.POST)
                    if form.is_valid():
                        form.save()
                        messages.success(request, 'Your account has been successfully created!')
                        return redirect('main:login')
                context = {'form':form}
                return render(request, 'register.html', context)

        4. I then created a HTML file caled register.html for showing the user registration form on a web browser in the directory main/templates

        5. I then did URL routing for register in urls.py by importing register and creating an URL path for it

        6. To create the login funtion I imported the following modules in views.py and created a function called login_user

            from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
            from django.contrib.auth import authenticate, login

            def login_user(request):
                if request.method == 'POST':
                    form = AuthenticationForm(data=request.POST)

                    if form.is_valid():
                            user = form.get_user()
                            login(request, user)
                            return redirect('main:show_main')

                else:
                    form = AuthenticationForm(request)
                context = {'form': form}
                return render(request, 'login.html', context)


        7. I then created another HTML file called login.html in the directory main/templates

        8. Finally, I did URL routing for login in urls.py

        9. For the logout feature I imported these modules and created a function called logout_user in views.py

            from django.contrib.auth import logout

            def logout_user(request):
                logout(request)
                return redirect('main:login')

        10. In main.html I added these lines to create a button for logging out

            <a href="{% url 'main:logout' %}">
                <button>Logout</button>
            </a>

        11. Before the functions above can be used, I have to block access from the main page for users who are not logged in. To do that I imported this module in views.py

            from django.contrib.auth.decorators import login_required

        12. I then added this line above the show_main function

    2. Make two user accounts with three dummy data each, using the model made in the application beforehand so that each data can be accessed by each account locally.

        1. I created a folder in main directory called management and added an empty file called __init__.py
        
        2. I then created another folder called commands and added the files __init__.py which is empty and create_dummy_users.py

        3. I imported libraries and added information for the two dummy users. Here are their login data.

        Account 1:
            Username: CookieCat
            Password: cookiecookie123

        Account 2:
            Username: ChocoDog
            Password: choco123
        
        4. I then ran python manage.py create_dummy_users to create the dummy users


    3. Connect the models Product and User.


        1. To start I added the following lines in models.py, one at the top and the other below the Product class

            from django.contrib.auth.models import User

            user = models.ForeignKey(User, on_delete=models.CASCADE)

        2. In views.py I altered this if statement under create_product_entry function to this
            
                if form.is_valid() and request.method == "POST":
                    product_entry = form.save(commit=False)
                    product_entry.user = request.user
                    product_entry.save()
                    return redirect('main:show_main')

        3. I added this as a new context in views.py

                    'name': request.user.username,

            and changed .all() in show_main to this

                    filter(user=request.user)


    4. Display logged in user details such as username and apply cookies like last login to the application's main page.

        1. To set the cookies up for the latest logged in user, I imported the following modules in views.py

            import datetime
            from django.http import HttpResponseRedirect
            from django.urls import reverse

        2. Then in views.py, I changed the code for if form.is_valid() to the following 

            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response

        3. I added this line in context of the show_main function in views.py so that the cookies data can be displayed 

                'last_login': request.COOKIES['last_login'],

        4. I changed the code under logout_user to this:

                logout(request)
                response = HttpResponseRedirect(reverse('main:login'))
                response.delete_cookie('last_login')
                return response

        5. I then added this line below the log out button

            <h5>Last login session: {{ last_login }}</h5>
</details>

<details>
<summary> ASSIGNMENT 3 </summary>

# == ASSIGNMENT 3 QUESTIONS AND ANSWERS: == #

<< Link for Screenshots for XML, JSON, XML by ID and JSON by ID >>
<< https://docs.google.com/document/d/1_K4jK-_b2kweG8Sl_gUZz0fhp48jUh3XQXMI37tgUaM/edit >>
 
## 1>>> Explain why we need data delivery in implementing a platform.

    So that different parts of a platform can communicate with each other and accomplish tasks they are required to do.
    URL routing is one such method and it allows an application to be displayed on a web browser. Without data delivery in a platform, applications would run very slowly and inconvenient and primitive methods would have to be implemented for data delivery.
    The platform is not static anymore as with data delivery, synchronous communication is enabled between the users, platform and the administrators.


## 2>>> In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?

    I think JSON is better because its size is generally smaller than XML, its data can be transferred quicker and it is more human-readable. XML takes more time to read due to its hierarchical structure while JSON is more compact and shorter.

    JSON is more popular because it is flexible in applications and is easy to parse.
    JSON is also widely used for data transfer in mobile applications in which data transfer needs to be completed as quick as possible.


## 3>>> Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.

    The method is_valid() performs a validation check on data entered in Django forms, it makes sure that the data entered matches the type and constraints set for each data query. This eliminates the need for administrators to read through and check forms that have wrong data type inputted such as numbers in a query for words, thus saving time.
    This also prevents users from accidentally inputting the wrong or empty data in forms, giving them a chance to recheck their answers and input them correctly.
    

## 4>>> Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?

    A CSRF token is a large randomly generated number given to each authenticated user that visits a django-based website. This token ensures that requests from the user cannot be done on malicious websites without their consent, called cross site request forgery. They provide security for authenticated users by allowing them and them only to issue forms and requests, stopping malicious users from making requests in place of the authenticated user without consent. 
    Without CSRF tokens, stealing money from accounts on banking websites would be so easy. The thief would send a link that has a request to send money from the victim's account to their account on their website and have the authenticated user click it. After the user connects to the malicious site, the request will be sent to the bank and the money will be transferred.
    

## 5>>> Explain how you implemented the checklist above step-by-step (not just following the tutorial).

        1>> Create a form input to add a model object to the previous app.

            1> I first created a base template for all the other web pages called base.html.

            2> I then added 
            ```
            'DIRS': [BASE_DIR / 'templates']
            ```
            in settings.py in e_commerce_app so that base.html will be detected as a base file.

            3> Next I added 
            ```
            {% extends 'base.html' %} 
            ...
            {% block content %}
            {% endblock content %}
            ```
            main.html in main/templates so that the data in the django project will be loaded in HTML form easily.

            4> In the same file I added the lines
            ```
            import uuid
            id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
            ```

            5> I then ran the following commands 'python manage.py makemigrations' and 'python manage.py migrate'.

            6> To create the base of the form, I created a file 'forms.py' in main directory and created a new class ProductEntryForm.

            7> I then imported redirect from the django.shortcuts library and added
            ```
            from main.forms import ProductEntryForm
            from main.models import Product
            ``` 
            at the top of views.py in main directory.

            8> In views.py, I then created a new function that takes a request and creates a form for the website.

            9> Then I added
            ```
            product_entries = Product.objects.all()
            ```
            so that the project can retrieve data about the Product objects from the database.

            10> To set up URL routing for the function that creates the form I added
            ```
            path('create-product-entry', create_product_entry, name='create_product_entry')
            ```
            and imported create_product_entry.

            11> I then created create_product_entry.html that dictates how the form will be displayed on a web browser. The code in the file is as follows:
            ```
            {% extends 'base.html' %} 
            {% block content %}
            <h1>Add New Product Entry</h1>

            <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Product Entry" />
                </td>
                </tr>
            </table>
            </form>

            {% endblock %}
            ```
            
            12> Finally I added extra lines of code in main.html so that the table form can be displayed with a button.
        
        
        2>> Add 4 views to view the added objects in XML, JSON, XML by ID, and JSON by ID formats. 

            1> I added and imported the following libraries and modules in views.py
            ```
            from django.http import HttpResponse
            from django.core import serializers
            ```

            2> In the same file, I added two functions show_xml and show_json that will translate the data into XML and JSON respectively before displaying them.
            ```
            def show_xml(request):
                data = Product.objects.all()
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

            def show_json(request):
                data = Product.objects.all()
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")
            ```

            3> To display the data in both XML and JSON by ID I added two more functions that display the two data types by ID in views.py
            ```
            def show_xml_by_id(request, id):
                data = Product.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

            def show_json_by_id(request, id):
                data = Product.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")
            ```

        
        3>> Create URL routing for each of the views added in point 2.

            1> In urls.py I imported the two functions above from the main.views library and added paths in url_patterns for them so that they can be routed to the view, the paths are like this:
            ```
            path('xml/', show_xml, name='show_xml'),
            path('json/', show_json, name='show_json'),
            ```

            2> In addition, I imported the functions and added URL paths for said functions in urls.py to complete URL routing
            the paths look like this:
            ```
            path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
            path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
            ```
</details>

<details>
<summary> ASSIGNMENT 2 </summary>

# == ASSIGNMENT 2 QUESTIONS AND ANSWERS: ==

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
</details>
