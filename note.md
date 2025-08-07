# Very First Step: 

1. Creating the Virtual Environment 
   >python -m venv env 


2. Activating Virtual Environment 
   >. env/Scripts/activate

Output: Now and env folder is created insider our To-Do-App

3. Now Installing Django
   > pip install Django

4. Verifying Installation of Django 
   > pip freeze

5. Creating a Django Project 
   > django-admin startproject todo_main .

now todo_main project is created inside To-Do-App

6. Running the Django App
    > python manage.py runserver 9000


# Day 2: Creating Superuser and Home 

If I run my admin panel and http://127.0.0.1:9000/admin  this will not run and says a error called OperationalError:no such table:django_session 

7. so to solve this let's first migrate the unapplied migration.
    >python manage.py migrate

After this the Admin Panel will work and shows the login dashboard 

8. Creating the Super User 
   >python manage.py createsuperuser

now our admin site is open 

9. Creating a path for home page 
   > Going to urls.py in todo-main 
   > Adding this path in urls.py ` path('', views.home, name="Home")`    
   > Creating a views.py file and adding this code for home page 


from django.http import HttpResponse    
def home(request):
    return HttpResponse('<h3> This is Homepage </h3>')

# Creating a Todo Template using Bootstrap

we earlier were showing a home page through HttpResponse but now we have to show home.html and for this we have to render it 

The code: 
  >from django.shorcuts import render 
  >def home(request):
  > return render(request,'home.html') 

1. Now making the template folder in project level directory
2. In setting also have to add 'templates' in DIR 