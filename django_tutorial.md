## Table of Contents

- [Introduction](#introduction)
  - [What is Django?](#what-is-django?)
  - [Project v/s App](#project-v/s-app)
    - [Resources](#resources)
- [Project Setup and Getting Started](#project-setup-and-getting-started)
    - [Virtual Environment Setup](#virtual-environment-setup)
    - [Installing Django and setting up Project](#installing-django-and-setting-up-project)
    - [Exploring the initial files and Running the server](#exploring-the-initial-files-and-running-the-server)
- [Apps, URLs & Templates](#apps,-urls-&-templates)
  - [Creating apps](#creating-apps)
  - [Creating a view and including the urls](#creating-a-view-and-including-the-urls)
  - [Pages Templates & base Layout](#pages-templates-&-base-layout)
    - [Rendering a html page as the response for a view method](#rendering-a-html-page-as-the-response-for-a-view-method)
    - [Extending from a base layout](#extending-from-a-base-layout)
  - [Static Files and Paths](#static-files-and-paths)
  - [Bootstrap Layout Markup](#bootstrap-layout-markup)
    - [Using the static files in django templates](#using-the-static-files-in-django-templates)
    - [Setting up reusable html components in partials](#setting-up-reusable-html-components-in-partials)
  - [Index, About & Linking](#index,-about-&-linking)
  - [Listings, URLs and Templates](#listings,-urls-and-templates)
    - [Adding a query parameter in the url](#adding-a-query-parameter-in-the-url)
- [Models, Migrations & Admin](#models,-migrations-&-admin)
  - [Install Postgress & Admin](#install-postgress-&-admin)
  - [Django postgres setup and migrate](#django-postgres-setup-and-migrate)
    - [Install psycopg2](#install-psycopg2)
    - [Updating the settings.py file and applying the default migrations](#updating-the-settings.py-file-and-applying-the-default-migrations)
  - [Planning our schemas](#planning-our-schemas)
    - [LISTING](#listing)
    - [REALTOR](#realtor)
    - [CONTACTS](#contacts)
  - [Create Listing Model](#create-listing-model)
  - [Realtor Model and Run Migrations](#realtor-model-and-run-migrations)
  - [Create Superuser and Register models with Admin](#create-superuser-and-register-models-with-admin)
  - [Media Folder and Adding Data](#media-folder-and-adding-data)
  - [Admin Logo and CSS](#admin-logo-and-css)
  - [Customize Admin Display](#customize-admin-display)
- [View Methods, Display & Search](#view-methods,-display-&-search)
  - [Pull Data from Listing Model](#pull-data-from-listing-model)
    - [Pass in values as a dictionary in the render function call along with the html template (MVC Architecture)](#pass-in-values-as-a-dictionary-in-the-render-function-call-along-with-the-html-template-(mvc-architecture))
  - [Display Listings In Template](#display-listings-in-template)
    - [Pull the field values from a model](#pull-the-field-values-from-a-model)
  - [Pagination, Order & Filter](#pagination,-order-&-filter)
  - [Home & About Page Dynamic Content](#home-&-about-page-dynamic-content)
  - [Single Listing Page](#single-listing-page)
  - [Search Form Choices](#search-form-choices)
  - [Search Form Filtering](#search-form-filtering)
  - [Preserving Form Input](#preserving-form-input)
- [Accounts & Authentication](#accounts-&-authentication)
  - [Account App & URLs](#account-app-&-urls)
  - [Register & Login Templates](#register-&-login-templates)
  - [Message Alerts (setting up bootstrap-django message alerts)](#message-alerts-(setting-up-bootstrap-django-message-alerts))
  - [User Registration](#user-registration)
  - [User Login](#user-login)
  - [Logout & Navbar Auth Links](#logout-&-navbar-auth-links)
    - [Logout](#logout)
  - [Dynamic Page Titles](#dynamic-page-titles)
- [Contact Inquiries](#contact-inquiries)
  - [Contacts App & Model](#contacts-app-&-model)
  - [Contacts Admin Customization](#contacts-admin-customization)
  - [Contact Form Prep](#contact-form-prep)
  - [Contact Form Submission](#contact-form-submission)
  - [Inquiry Check & Send Email](#inquiry-check-&-send-email)
  - [Dashboard Functionality](#dashboard-functionality)

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

NOTE: Install pylint-django to remove django related syntactic errors  
[Stackoverflow Thread](https://stackoverflow.com/questions/45135263/class-has-no-objects-member)
```python
def index(request):
	# VS code may mark Listing as error
    listings = Listing.objects.all()
```

### Pass in values as a dictionary in the render function call along with the html template (MVC Architecture)
```python
# listings/views.py

from django.shortcuts import render
from .models import Listing

# Create your views here.

def index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)
```

```html
<!-- templates/listings/listings.html -->

{% if listings %}
    {% for listing in listings %}
    	<!-- Dynamically display the contents of each listings -->
    {% endfor %}
{% else %}
    <!-- If there are no listings in the database -->
     <div class="col-md-12">
        <p>No Listings Available</p>
     </div>
{% endif %}
```

## Display Listings In Template

### Pull the field values from a model
```html
<!-- templates/listings/listings.html -->

<img class="card-img-top" src="{{ listing.photo_main.url }}" alt="">
<h4 class="text-primary">{{ listing.title }}</h4>

<!-- Will dipslay name since Realtor model returns self.name for __str__ function -->
<div class="col-12">
    <i class="fas fa-user"></i> {{ listing.realtor }}</div>
</div>

<!-- add model data in link url -->
<a href="{% url 'listing' listing.id %}" class="btn btn-primary btn-block">
    More Info
</a>
```

[A set of Django template filters useful for adding a “human touch” to data.](https://docs.djangoproject.com/en/5.1/ref/contrib/humanize/)
```python
# settings.py

INSTALLED_APPS = [
	# 
    'django.contrib.humanize',
]
```
```html
<!-- templates/listings/listings.html -->

{% load humanize %}

<!-- Converts an integer or float (or a string representation of either) to a string containing commas every three digits. -->
<span class="badge badge-secondary text-white">
    ${{ listing.price | intcomma }}
</span>
```

## Pagination, Order & Filter

[Fetching what we need from the database](https://docs.djangoproject.com/en/5.1/topics/pagination/#using-paginator-in-a-view-function)
```python
# listings/views.py
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    listings = Listing.objects.all()

    # Pagination
    paginator = Paginator(listings, 3)
    page = request.GET.get('page') # page parameter from client request
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)
```

Displaying the right way
[django](https://docs.djangoproject.com/en/5.1/topics/pagination/#paginating-a-listview)
[bootstrap](https://getbootstrap.com/docs/4.0/components/pagination/#disabled-and-active-states)
```html
<!-- templates/listings/listings.html -->

<div class="row">
    <div class="col-md-12">
        <!-- If there are further pages -->
        <!-- Eg: listings per page is 6 but we only have 6 listings, then dont paginate -->
        {% if listings.has_other_pages %}
            <ul class="pagination">
                <!-- checking for previous pages for the back arrow -->
                {% if listings.has_previous %}
                    <li class="page-item">
                        <a href="?page={{ listings.previous_page_number }}" class="page-link">&laquo;</a>
                    </li>
                <!-- otherwise the link should be disabled without any href -->
                {% else %}
                    <li class="page-item disabled">
                        <a class="page-link">&laquo;</a>
                    </li>
                {% endif %}
                
                <!-- looping through our page range -->
                {% for page_number in listings.paginator.page_range %}
                    <!-- We are currently on the active page which has the current listings -->
                    {% if listings.number == page_number %}
                        <li class="page-item active">
                            <a class="page-link">{{ page_number }}</a>
                        </li>
                    <!-- The inactive pages which contain the remaining listings -->
                    {% else %}
                        <li class="page-item">
                            <a href="?page={{ page_number }}" class="page-link">{{ page_number }}</a>
                        </li>
                    {% endif %}
                {% endfor %}

                <!-- checking for next pages for the forward arrow -->
                {% if listings.has_next %}
                <li class="page-item">
                    <a href="?page={{ listings.next_page_number }}" class="page-link">&raquo;</a>
                </li>
                <!-- otherwise the link should be disabled without any href -->
                {% else %}
                    <li class="page-item disabled">
                        <a class="page-link">&raquo;</a>
                    </li>
                {% endif %}
            </ul>
        {% endif %}
    </div>
</div>
```

Filtering out and ordering the listings objects to be rendered in the front end webpage
```python
# listings/views.py

def index(request):
    listings = Listing.objects.order_by('-price').filter(is_published=True)
    #
```

## Home & About Page Dynamic Content

```python
# pages/views.py

from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }
    return render(request, 'pages/about.html', context)
```
```html
<!-- templates/pages/about.html -->

<div class="col-md-4">
    {% if mvp_realtors %}
        {% for realtor in mvp_realtors %}
            <div class="card">
                <img src="{{ realtor.photo.url }}" alt="{{ realtor.name }}">
                <div class="card-body">
                    <h5 class="card-title">Seller Of The Month</h5>
                    <h6 class="text-secondary">{{ realtor.name }}</h6>
                    <p class="card-text">{{ realtor.description }}</p>
                </div>
            </div>  
        {% endfor %}
    <!-- No need of an else, because we are not going to display anything if there are no mvp_realtors -->
    {% endif %}
</div>

<div class="row text-center">
    {% if realtors %}
        {% for realtor in realtors %}
            <div class="col-md-4">
                <img src="{{ realtor.photo.url }}" alt="{{ realtor.name }}" class="rounded-circle mb-3">
                <h4>{{ realtor.name }}</h4>
                <p class="text-success">
                <i class="fas fa-award text-success mb-3"></i> Realtor</p>
                <hr>
                <p>
                <i class="fas fa-phone"></i> {{ realtor.phone }}</p>
                <p>
                <i class="fas fa-envelope-open"></i> {{ realtor.email }}</p>
            </div>
        {% endfor %}
    {% else %}
        <div class="col-md-12">
            <p>No Realtors Available</p>
        </div>
    {% endif %}
</div>

<!-- templates/pages/index.html -->

<div class="row">
    {% if listings %}
        {% for listing in listings %}
            <div class="col-md-6 col-lg-4 mb-4">
                <div class="card listing-preview">
                    <img class="card-img-top" src="{{ listing.photo_main.url }}" alt="{{ listing.title }}">
                    <div class="card-img-overlay">
                        <h2>
                        <span class="badge badge-secondary text-white">${{listing.price | intcomma}}</span>
                        </h2>
                    </div>
                    <div class="card-body">
                        <div class="listing-heading text-center">
                        <h4 class="text-primary">{{ listing.title }}</h4>
                        <p>
                            <i class="fas fa-map-marker text-secondary"></i> 
                            {{ listing.city }} {{ listing.state }}, {{ listing.zipcode }}
                        </div>
                        <hr>
                        <div class="row py-2 text-secondary">
                        <div class="col-6">
                            <i class="fas fa-th-large"></i> Sqft: {{ listing.sqft }}</div>
                        <div class="col-6">
                            <i class="fas fa-car"></i> Garage: {{ listing.garage }}</div>
                        </div>
                        <div class="row py-2 text-secondary">
                        <div class="col-6">
                            <i class="fas fa-bed"></i> Bedrooms: {{ listing.bedrooms }}</div>
                        <div class="col-6">
                            <i class="fas fa-bath"></i> Bathrooms: {{ listing.bathrooms }}</div>
                        </div>
                        <hr>
                        <div class="row py-2 text-secondary">
                        <div class="col-6">
                            <i class="fas fa-user"></i> {{ listing.realtor }}</div>
                        </div>
                        <div class="row text-secondary pb-2">
                        <div class="col-6">
                            <i class="fas fa-clock"></i> {{ listing.list_date | timesince }}</div>
                        </div>
                        <hr>
                        <a href="{% url 'listing' listing.id %}" class="btn btn-primary btn-block">
                            More Info
                        </a>
                    </div>
                </div>
            </div>
        {% endfor %}
    {% else %}
        <div class="col-md-12">
            <p>No Listings available</p>
        </div>
    {% endif %}
</div>
```

## Single Listing Page

get object or return 404 error
```python
# listings/views.py
from django.shortcuts import get_object_or_404

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)
```
```html
<!-- template/listings/listing.html -->

<img class="card-img-top" src="{{ listing.realtor.photo.url }}" alt="{{ listing.realtor }}">
```

## Search Form Choices

required key value pairs as dictionaries
```python
# listings/choices.py

price_choices = {
	# dictionary key -> html value attribute, dictionary value -> html innertext
	'100000':'$100,000',
	'200000':'$200,000',
	# 
}

# pages/views.py
from listings.choices import price_choices, bedroom_choices, state_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'price_choices': price_choices, 
        'bedroom_choices': bedroom_choices, 
        'state_choices': state_choices
    }
    return render(request, 'pages/index.html', context)
```
```html
<!-- templates/pages/index.html -->
<!-- templates/listings/search.html -->

<!-- calls the search view function in the listings/views.py by assigning it to the action attribute -->
<form action="{% url 'search' %}">	
	{% for key, value in price_choices.items %}
	    <option value="{{ key }}">{{ value }}</option>
	{% endfor %}
</form>


```

## Search Form Filtering

For each keyword:
1. Check whether its available in the request which is a GET request
2. Pull it out from the query set and store into a variable
3. Make it part of the filter condition of the query set

[Query Set Field Lookups - icontains](<!-- calls the search view function in the listings/views.py -->)
```python
# listings/views.py

def search(request):
    queryset_list = Listing.objects.all().order_by('-list_date')
    
    # Keywords
    if 'keywords' in request.GET:
        # Get the value from the form field which has the attribute name=keywords
        # <input type="text" name="keywords" class="form-control" placeholder="Keyword (Pool, Garage, etc)"/>
        keywords = request.GET['keywords']
        # Handling case of empty string by nesting a second if
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    context = {
    	# 
        'listings': queryset_list,
    }
    return render(request, 'listings/search.html', context)
```

## Preserving Form Input

Giving the GET request parameters to the html page through the render function
```python
# listings/views.py

def search(request):
	# 

    context = {
    	# 
        'values': request.GET,
    }
    return render(request, 'listings/search.html', context)
```
```html
<!-- listings/search.html -->

<!-- {{ values.<<param>> }} -->
<!-- param should be the parameter in the GET request which is actually the name attribute of the html form element -->

<!-- text input fields -->
<div class="col-md-4 mb-3">
  <label class="sr-only">City</label>
  <input
      type="text"
      name="city"
      class="form-control"
      placeholder="City"
      value="{{ values.city }}"
  />
</div>

<!-- select drop down input fields -->
<label class="sr-only">Bedrooms</label>
<select name="bedrooms" class="form-control">
  <option selected="true" disabled="disabled">
      Bedrooms (Any)
  </option>
  {% for key, value in bedroom_choices.items %}
    <option value="{{ key }}"
      {% if key == values.bedrooms %}
        selected
      {% endif %}
    >
      {{ value }}
    </option>
  {% endfor %}
</select>
```

# Accounts & Authentication

## Account App & URLs

Django already has user module (auth_user table in db). We just need to reuse it.
But when user is created through front end, they should not marked as staff and given admin access.

1. startapp accounts and add to settings.py
2. create urls.py file and add the required path routes
3. include in the urls.py of the project

## Register & Login Templates

Changing form method to POST from the default GET. Add csrf token to tie the form with the user session.
csrf token is actually a hidden input element with the value as the token.
```html
<!-- templates/accounts/login.html -->
<!-- templates/accounts/register.html -->

<form action="{% url "register" %}" method="POST">
    {% csrf_token %}
    <!--  -->
    <input type="submit" value="Login" class="btn btn-secondary btn-block">
</form>
```
modifying the view functions to handle both GET and POST methods
```python
# accounts/views.py

def register(request):
    if request.method == 'POST':
        print('SUBMITTED REG')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')
```

## Message Alerts (setting up bootstrap-django message alerts)

[Django already has a messages app that we can configure and reuse](https://docs.djangoproject.com/en/5.1/ref/contrib/messages/#message-tags)
```python
# settings.py

# Messages

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}
```
```html
<!-- templates/partials/_alerts.html -->
<!-- reusable across any bootstrap-django projects as an error/message output -->

<!-- check if there are any messages -->
{% if messages %}
    <!-- If so, loop through each message -->
    {% for message in messges %}
        <div id="message" class="container">
            <!-- bootstrap markup -->
            <!-- We already confifured messages.ERROR = 'danger' in MESSAGE_TAGS in settings.py -->
            <!-- alert-dismissible with a close button to dismiss the alert -->
            <div class="alert alert-{{ message.tags }} alert-dismissible text-center" role="alert">
                <!-- button to close the dismissible alert -->
                <buttton type="button" class="close" data-dismiss="alert">
                    <!-- X mark for the button text -->
                    <span aria-hiddent="true">&times;</span>
                    <strong>
                        <!-- Check if the message is an error -->
                        {% if messsage.level == DEFAULT_MESSAGE_LEVELS.ERROR %}
                            Error
                        {% else %}
                            {{ message.tags | title }}
                        {% endif %}
                    </strong>
                    <!-- show the actual message -->
                    {{ message }}
                </buttton>
            </div>
        </div>
    {% endfor %}
{% endif %}
```
linking the partials alert.html to the register template
```html
<!-- templates/accounts/register.html -->
<!-- templates/accounts/login.html -->

<div class="card-body">
    <!-- ALERTS -->
    {% include "partials/_alerts.html" %}
    <form action="{% url "register" %}" method="POST">
        {% csrf_token %}
        <!--  -->
        <input type="submit" value="Register" class="btn btn-secondary btn-block">
    </form>
</div>
```
testing the message.error alert
```python
# accounts/views.py

from django.contrib import messages

def register(request):
    if request.method == 'POST':
        # REGISTER
        messages.error(request, 'testing error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')
```
setting a timeout for the error to dismiss on its own
```js
// btre/static/js/main.js

setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);
```
Since we modified static, we need to run createstatic again so that it goes to the main static folder.
This moves the jQuery to BASE_DIR/static/js/main.js
```console
$ py manage.py collectstatic

You have requested to collect static files at the destination
location as specified in your settings:

    C:\Users\anand\OneDrive\Documents\Projects\btre_project\static

This will overwrite existing files!
Are you sure you want to do this?

Type 'yes' to continue, or 'no' to cancel: yes

130 static files copied to 'C:\Users\anand\OneDrive\Documents\Projects\btre_project\static', 29 unmodified.
```
**Debugging when jQuery in js file does not work**
1. Right click
2. View page source
3. Check main.js in the script tag
4. Ensure that collectstatic has added the new js code

## User Registration

```python
# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        # Get Form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_2 = request.POST['password2']

        # Check if passwords match
        if password == password_2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                # Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    # Validations passed
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'User registered and logged in')
                    # return redirect('index')

                    # Register but redirect to login page for manual login
                    user.save()
                    messages.success(request, 'User registered. Please proceed to log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')
```
- passwords are automatically hashed by django

Adding the alerts notification on the index page
```html
<!-- templates/pages/index.html -->

<!-- Alerts from partials/_alerts.html -->
{% include "partials/_alerts.html" %}
```

## User Login

```python
# accounts/views.py

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        # User found
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in succesfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')
```

## Logout & Navbar Auth Links

Setting up the dashboard.html page and updating breadcrumb links

**Note: user object is available in all templates by default**
```python
# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',  # <- This one adds `user`
                'django.template.context_processors.csrf',
            ],
        },
    },
]
```
### Logout
Logout should be a POST request and hence we are adding it as form in the navbar that will look like a link
```html
<!-- templates/partials/_navbar.html -->

<li class="nav-item mr-3">
	<!-- Clicking on the logout link, will trigger the javascript code to submit the hidden form -->
    <a href="javascript:{document.getElementById('logout').submit()}" class="nav-link">
        <i class="fas fa-sign-out-alt"></i>Logout
    </a>
    <form action="{% url "logout" %}" id="logout" method="POST">
        {% csrf_token %}
        <input type="hidden">
    </form>
</li>
```
```python
# accounts/view.py

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'User has been logged out')
        return redirect('index')
```
Adding the alerts notification on the dashboard page
```html
<!-- templates/pages/dashboard.html -->

<!-- Alerts from partials/_alerts.html -->
{% include "partials/_alerts.html" %}
```

## Dynamic Page Titles

Each page should have a relevant title so that if our site comes up on google search, then the link shows the title
```html
<!-- templates/base.html -->

<head>
	<!--  -->
    <title>BT Real Estate {% block title %}{% endblock title %}</title>
</head>

<!-- Other pages. Eg: templates/listings/search.html -->
{% block title %}
    | Search BTRE Listings
{% endblock title %}
```

# Contact Inquiries

## Contacts App & Model

1. startapp for contacts
2. setting up contact model
3. adding to the installed apps in settings.py
4. makemigrations
5. migrate

## Contacts Admin Customization

1. Set up the admin for the model
2. Choose list_display, list_display_links, search_fields, list_per_page

## Contact Form Prep

```html 
<!-- templates/listings/listing.html -->

  <form action="{% url "contact" %}" method="POST">
    {% csrf_token %}
    <!-- Pass in the user id of the authenticated user -->
    {% if user.is_authenticated %}
      <input type="hidden" name="user_id" value="{{ user.id }}">
    {% else %}
      <input type="hidden" name="user_id" value="0">
    {% endif %}
    <!-- We need to notify the realtor when there is a contact submission. So passing in realtor email -->
     <input type="hidden" name="realtor_email" value={{ listing.realtor.email }}>
     <input type="hidden" name="listing_id" value={{ listing.id }}>
    <div class="form-group">
      <label for="property_name" class="col-form-label">Property:</label>
      <input type="text" name="listing" class="form-control" value="{{ listing.title }}" disabled>
    </div>
    <div class="form-group">
      <label for="name" class="col-form-label">Name:</label>
      <input type="text" name="name" class="form-control"
        {% if user.is_authenticated %}
          value=user.name
        {% endif %}
      required>
    </div>
    <div class="form-group">
      <label for="email" class="col-form-label">Email:</label>
      <input type="email" name="email" class="form-control"
      {% if user.is_authenticated %}
        value=user.email
      {% endif %}
      required>
    </div>
    <div class="form-group">
      <label for="phone" class="col-form-label">Phone:</label>
      <input type="text" name="phone" class="form-control">
    </div>
    <div class="form-group">
      <label for="message" class="col-form-label">Message:</label>
      <textarea name="message" class="form-control"></textarea>
    </div>
    <hr>
    <input type="submit" value="Send" class="btn btn-block btn-secondary">
  </form>
```
- setting up the urls, adding the include in the main urls.py
- setting up the method in views.py

## Contact Form Submission

I made a few changes of my own
```python
# contacts/views.py

def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        
        contact = Contact(
            listing=Listing.objects.get(id=listing_id),
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
            realtor_email=realtor_email
        )

        contact.save()

        messages.success(request, 'Your inquiry has been submitted. A realtor will soon reach out to you.')

        return redirect('/listings/'+listing_id)

# contacts/models.py

class Contact(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    # User who is logged in should also be able to make inquiry. So making it optional.
    user_id = models.IntegerField(blank=True)
    realtor_email = models.CharField(max_length=100)

def __str__(self):
    return self.name
```
```html
<!-- templates/listings/listing.html -->

<!-- Alerts from partials/_alerts.html -->
{% include "partials/_alerts.html" %}

<input type="hidden" name="listing_id" value={{ listing.id }}>

<!-- Property field was removed later -->
 <!--  
  <div class="form-group">
    <label for="property_name" class="col-form-label">Property:</label>
    <input type="text" name="listing" class="form-control" value="{{ listing.id }}">
  </div>
-->
```

## Inquiry Check & Send Email

Checking whether user has already inquired about the listing
```python
# contacts/views.py

def contact(request):
	# 
	
    # Check if user has already made an inquiry for the listing
    if request.user.is_authenticated:
        user_id = request.user.id
        has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
        if has_contacted:
            messages.error(request, 'You have already made an inquiry for the listing')
            return redirect('/listings/'+listing_id)
```

[Sending email](https://docs.djangoproject.com/en/5.1/topics/email/#module-django.core.mail)
```python
# contacts/views.py

from django.core.mail import send_mail

def contact(request):
    # 
    send_mail(
        "Property Listing Inquiry : " + listing.title,
        "There has been an inquiry for " + listing.title + '. Sign in to the admin panel for more info.',
        "amc.fullstack@gmail.com",
        ["anandcherian.585@gmail.com", realtor_email],
        fail_silently=False,
    )

# settings.py

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '****@gmail.com'
EMAIL_HOST_PASSWORD = '******'
EMAIL_USE_TLS = True
```

## Dashboard Functionality

```html
<!-- templates/accounts/dashboard.html -->

{% if contacts %}
    <h2>Welcome {{ user.first_name }}</h2>
    <p>Here are the property listings that you have inquired about</p>
    <table class="table">
        <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Property</th>
            <th></th>
        </tr>
        </thead>
        <tbody>
            {% for contact in contacts %}
                <tr>
                    <td>{{ contact.id }}</td>
                    <td>{{ contact.listing }}</td>
                    <td>
                    <a class="btn btn-light" href="{% url "listing" contact.listing_id %}">
                        View Listing
                    </a>
                    </td>
                </tr>     
            {% endfor %}
        </tbody>
    </table>
{% else %}
    <p>You have not made any inquiries</p>
{% endif %}
```
```python
# accounts/dashboard.py

from contacts.models import Contact

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)
```
