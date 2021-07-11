class 26 - sunday 11/7/2021

1. create directory
2. poetry init -n
3. poetry add django
4. poetry add --dev black
5. poetry shell
6. `django-admin startproject <project_Name> .`  (start project)
7. `python manage.py runserver` (for run server)
8. `python manage.py migrate`  (sql lite )
9. `python manage.py startapp <app_Name>`
******************************

10. In setting in project file 
in `INSTALLED_APPS` : 
add 
 `app_name(folder).apps.className`

className -> in apps  folder, `app.py`. for example : `'moviesapp.apps.MoviesappConfig' `  

******************************


11. in same file Templates add this line: 

` 'DIRS': [os.path.join(BASE_DIR , 'templates')],` and create templates folder  with base,home , about


******************************

12. go to project file -> `urls.py` 

add : 

• `from django.urls import path, include.`

•in urlpatterns add path : 

`path ('', include('appName.urls'))` 
*******************************

13. go to views in app folder 

`from django.views.generic import TemplateView`

    class Home (TemplateView): 
        template_name="home.html"  

******************************

14. create `urls.py` in app folder 

import

   `from django.urls import path`

`from .views import HomeView , AboutView`

• create the paths and  call your classes

    urlpatterns = [
        path('', HomeView.as_view(), name='home'), 
        path('about', AboutView.as_view() , name='about' ),
    ]
******************************


15. in test file in app : 

• import  : 

    from django import urls

    from django.test import TestCase , SimpleTestCase

    from django.urls import reverse



  • create class and inherit (SimpleTestCase) 
  and  your tests as a method .

  • use `python manage.py test ` to run your cheak your tests.