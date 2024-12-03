# Introduction

## What is Django?
High level python framework for developing applications. Unlike Flask which is a low level microframework where 
you can a certain thing in multiple ways, in Django there is really only one way you can do things and that means
less room for error and faster development times. Some other additional benefits are:
1. Admin
2. Authentication
3. Built in security features
4. CLI tools for starting projects, applications etc

## Project v/s App
Project is your complete application and app is the different submodules. Different apps should work differently
and we should be able to plug it into different projects without any dependancy. 

### Resources
1. [Project v/s App](https://stackoverflow.com/questions/19350785/what-s-the-difference-between-a-project-and-an-app-in-django-world)
2. [Django Official Documentation](https://www.djangoproject.com/start/overview/)
3. [Django cheat sheet](https://gist.github.com/bradtraversy/0df61e9b306db3d61eb24793b6b7132d)

# Project Setup and Getting Started

### Virtual Environment Setup
NOTE: bash terminal
```console
python -m venv .venv
source .venv/Scripts/activate
```

### Installing Django and setting up Project
```console
django-admin help
django-admin startproject btre .
py manage.py help
```

### Exploring the initial files and Running the server
```console
py manage.py runserver
```

1. dbsqlite 			: not a suitable database for production grade applications
2. __pycache__ 			: caching for easier executions
3. __init__				: to use files as packages and prevents directories with common names from unintentionally hiding valid modules
4. settings				:
	1. BASE_DIR			: project base directory
	2. SECURITY_KEY		: hide it while deployment and in github repository
	3. DEBUG			: false in production and true during development
	4. ALLOWED_HOST		: need to put in list host domains while deployment
	5. INSTALLED_APP	: default and custom apps
	6. MIDDLE_WARE		: mostly security related middleware
	7. ROOT_URLCONF		: string value of full import path to the root url where initial url file is
	8. TEMPLATES		: HTML for our application - location, options etc
	9. WSGI_APPLICATION	: path of the wsgi application object which is used by the django built in server uses.
	10. DATABASES		: connect the db
	11. AUTH_PASSWORD	: where we can set rules for our passwords
	12. STATIC_URL		: path for static files (css, js, images)
5. urls					: routing file with list of urls where we can link a url to the corresponding view method or urls from other file
6. wsgi 				: Web Server Gateway Interface - protocol of server to app communication and how apps can be chained together

# Apps, URLs & Templates

## Creating apps
```console
py manage.py startapp pages
```
**Don't forget to add the app into the settings.py file of the project**
```python
INSTALLED_APPS = [
    'pages',
    #
]
```

## Creating a view and including the urls
```python
# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]

# pages/views.py
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello World</h>')

# urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
```

## Pages Templates & base Layout

**Don't forget to add the templates folder into the settings.py file of the project**
```python
from os import path

TEMPLATES = [
    {
        # 
        'DIRS': [path.join(BASE_DIR, 'templates')],
        #
    },
]
```

### Rendering a html page as the response for a view method
```python
# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]

# pages/views.py
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')
```

### Extending from a base layout 
- Need not repeat the head section, css references, js references in every html page
- use of jinja template tags
- **{% extends "base.html" %} should always be the first line in the html**
```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BT Real Estate</title>
</head>
<body>
    {% block content %}
        
    {% endblock %}
</body>
</html>

<!-- index.html -->
{% extends "base.html" %}
{% block content %}
    <h1>Home</h1>
{% endblock %}
```

## Static Files and Paths
- setting up the static folder within the project folder
- STATIC_ROOT 		: the root folder where collectstatic command will put all the fetched static files
- STATICFILES_DIRS	: the paths where we specifically tell django to fetch the static files
- STATIC_URL		: URL prefix for serving static files. When you use the {% static %} template tag, Django will prepend this URL to the static file path.
```html
<!-- STATIC_URL = '/static/' in the settings.py file -->
<!-- actual code in django template -->
<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">

<!-- this will generate as below -->
<link rel="stylesheet" type="text/css" href="/static/css/style.css">
```
[Django static files](https://docs.djangoproject.com/en/dev/ref/settings/#static-files "Offical documentation for static files in django")
```python
# settings.py
from os import path

STATIC_ROOT = path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    path.join(BASE_DIR, 'btre/static')
]
```
- add the media and static folder into the .gitignore file

## Bootstrap Layout Markup

### Using the static files in django templates
```html
<!-- base.html -->
{% load static %}

<link rel="stylesheet" href="{% static 'css/all.css' %}">
<!-- Other css files -->
<script src="{% static 'js/main.js' %}"></script>
<!-- Other js files -->
```

### Setting up reusable html components in partials
- naming convention starts with an underscore
```html
<!-- base.html -->

<!-- Top Bar -->
{% include "partials/_topbar.html" %}
```

## Index, About & Linking
Linking href of anchor tags to urls defined in urls.py
```html
<a href="{% url 'index' %}">
```

Using conditionals
```html
<li
    {% if '/' == request.path %}
        class="nav-item active mr-3"
    {% else %}
        class="nav-item mr-3"
    {% endif %}
>
<a class="nav-link" href="{% url 'index' %}">Home</a>
</li>
<li
    {% if 'about' in request.path %}
        class="nav-item active mr-3"
    {% else %}
        class="nav-item mr-3"
    {% endif %}
>
<a class="nav-link" href="{% url 'about' %}">About</a>
</li>
```

## Listings, URLs and Templates

### Adding a query parameter in the url
```python
urlpatterns = [
    path('<int:listing_id>', views.listing, name='listing')
]
```