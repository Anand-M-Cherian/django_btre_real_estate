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
<!-- templates/pages/about.html -->

<a href="{% url 'index' %}">
```

Using conditionals
```html
<!-- templates/partials/_navbar.html -->

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
# listings/urls.py

urlpatterns = [
    path('<int:listing_id>', views.listing, name='listing')
]
```

# Models, Migrations & Admin

## Install Postgress & Admin
- use postgres user while doing the development
- password setup will be during the postgres install
- create a database with owner as postgres
- grant all permissions for the postgres user

## Django postgres setup and migrate

### Install psycopg2
1. pip install psycopg2
2. pip install psycopg2-binary

Error: 
```console
building 'psycopg2._psycopg' extension
  error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
  error: subprocess-exited-with-error
```
Solution:
1. Download Microsoft C++ Build Tools: Visit Microsoft C++ Build Tools and download the installer.
2. Install the Required Components: During installation, select the Desktop development with C++ workload. Ensure the following components are selected:
	1. MSVC v143 - VS 2022 C++ x64/x86 Build Tools
	2. Windows 10 SDK (or newer)
3. Restart the Terminal: After installation, restart your terminal or IDE to apply changes.

Before the above steps solved my problem, I also tried the the below workarounds.
1. Add bin folder PostgreSQL to the PATH variables
2. Update pip

### Updating the settings.py file and applying the default migrations
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "btredb",
        "USER": "postgres",
        "PASSWORD": "pguser1234",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

Error: 
```console
"C:\Users\anand\OneDrive\Documents\Projects\btre_project\.venv\Lib\site-packages\django\db\backends\postgresql\base.py", line 29, in <module>
    raise ImproperlyConfigured("Error loading psycopg2 or psycopg module")
```
Solution: It seems we should use psycopg for newer projects. psycopg2 is being maintained for legacy codebases.

Before the above steps solved my problem, I also tried the the below workarounds.
1. Added postgressql_psycopg2 in the settings.py file
2. Tried keeping the binary version of psycopg2 alone in the virtual environment
3. Verified that virtual environment is active and python version of interpreter is correct

## Planning our schemas
- id (int) is automatically inserted and incremented

### LISTING
id: INT
realtor: INT (FOREIGN KEY [REALTOR])
title: STR
address: STR
city: STR
state: STR
zipcode: STR
description: TEXT
price: INT
bedrooms: INT
bathrooms: FLOAT
garage: INT (default 0)
sqft: INT
lot_size: FLOAT (Eg: 1.2 acres)
is_published: BOOL [default true]
list_date: DATE
photo_main: STR
photo_1: STR
photo_2: STR
photo_3: STR
photo_4: STR
photo_5: STR
photo_6: STR

### REALTOR
id: INT
name: STR
photo: STR
description: TEXT
email: STR
phone: STR
is_mvp: BOOLEAN [default 0]
hire_date: DATE

### CONTACTS
id: INT
user_id: INT
listing: INT
listing_id: INT
name: STR
email: STR
phone: STR
message: TEXT
contact_date: DATE

## Create Listing Model
- model name should always be the singular version of the app name. (Eg: Listing model in Listings App)
- every model should inherit from the models.Model

```python
# listings/models.py
from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.

class Listing(models.Model):
	# if realtor is deleted, do nothing to the listings which have that realtor as the foreign key
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)

    # basic text field
    address = models.CharField(max_length=200)

    # longer text field
    # optional field
    description = models.TextField(blank=True)

    # integer
    price = models.IntegerField()

    # Eg: 2.5, 3.7
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)

    # default value
    garage = models.IntegerField(default=0)

    # string value of the location of the photo
    # anything that we upload in through the admin goes to the media folder
    # Within that media folder, we are organizing photos by year, month and day
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')

    # true / false
    is_published = models.BooleanField(default=True)

    # datetime package from python
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
```

## Realtor Model and Run Migrations
Create the migrations files
```console
py manage.py makemigrations
```

To see the SQL query that is going to create the table in the database
```console
py manage.py sqlmigrate listings 0001
```
Output:
```sql
CREATE TABLE "listings_listing" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "title" varchar(200) NOT NULL, "address" varchar(200) NOT NULL, "city" varchar(100) NOT NULL, "state" varchar(100) NOT NULL, "zipcode" varchar(20) NOT NULL, "description" text NOT NULL, "price" integer NOT NULL, "bedrooms" integer NOT NULL, "bathrooms" numeric(2, 1) NOT NULL, "garage" integer NOT NULL, "sqft" integer NOT NULL, "lot_size" numeric(5, 1) NOT NULL, "photo_main" varchar(100) NOT NULL, "photo_1" varchar(100) NOT NULL, "photo_2" varchar(100) NOT NULL, "photo_3" varchar(100) NOT NULL, "photo_4" varchar(100) NOT NULL, "photo_5" varchar(100) NOT NULL, "photo_6" varchar(100) NOT NULL, "is_published" boolean NOT NULL, "list_date" timestamp with time zone NOT NULL, "realtor_id" bigint NOT NULL);
ALTER TABLE "listings_listing" ADD CONSTRAINT "listings_listing_realtor_id_90583529_fk_realtors_realtor_id" FOREIGN KEY ("realtor_id") REFERENCES "realtors_realtor" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "listings_listing_realtor_id_90583529" ON "listings_listing" ("realtor_id");
COMMIT;
```

Change the Database by commiting the new tables as part of the migration
```console
py manage.py migrate
```

## Create Superuser and Register models with Admin
```console
py manage.py createsuperuser
```

- staff_status = True means that the user log in to the admin console

```python
# listings/admin.py
from django.contrib import admin
from .models import Listing

admin.site.register(Listing)
```

- In the admin console, the bold paramters are the ones that are mandatory.
- Each model field gets the required type of input field

## Media Folder and Adding Data
To redirect all the uploads done through the admin area to the media folder
```python
# BASE_DIR/settings.py

MEDIA_ROOT = path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# BASE_DIR/urls.py

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Admin Logo and CSS
Adding the company logo
- templates/admin/base_site.html - these folder and file namings are necessary
- extending the base.html page of admin
- load the static assets
- "branding" block for the company name

```html
<!-- templates/admin/base_site.html -->
{% extends 'admin/base.html' %}
{% load static %}

{% block branding %}
    <h1 id="head">
        <img src="{% static 'img/logo.png' %}" alt="BT Real Estate" height="50" width="80" class="brand_img">
        Admin Area
    </h1>
{% endblock branding %}
```

Adding CSS colors
- extrastyle block for linking the required css files
```css
/* templates/admin/base_site.html */

{% block extrastyle %}
    <link rel="stylesheet" href="{% static 'css/admin.css' %}">
{% endblock extrastyle %}
```

- css file with all the required changes for each elements
```css
/* ========= HEADER ========= */

#header {
    height: 50px;
    background: #10284e;
    color: white;
}

#branding h1 {
    color: white;
}

a:link, a:visited {
    color: #10284e;
}

div.breadcrumbs {
    background: #30caa0;
    color: #10284e;
}

div.breadcrumbs a {
    color: #333;
}

/* ========= MAIN CONTENT ========= */

.module h2, .module caption, .inline-group h2 {
    background: #30caa0;
}

/* ========= MODELS CONTENT ========= */

.button, input[type=submit], input[type=button], .submit-row input, a.button {
    background: #10284e;
    color: white;
}
```

## Customize Admin Display
Adding multiple fields to show in the model table
```python
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
```

Adding links to the model
```python
class ListingAdmin(admin.ModelAdmin):
	#
	list_display_links = ('title',)
```

Adding filter
```python
class ListingAdmin(admin.ModelAdmin):
	#	
	list_filter = ('realtor',)
```

Change boolean field values from the table listing itself
```python
class ListingAdmin(admin.ModelAdmin):
	#
	list_editable = ('is_published',)
```

Add searchable fields
```python
class ListingAdmin(admin.ModelAdmin):
	#
	search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
```

Add pagination to the admin model page
```python
class ListingAdmin(admin.ModelAdmin):
	#
	list_per_page = 10
```

# View Methods, Display & Search

## Pull Data from Listing Model
