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
django-admin startproject btre
py manage.py help
```
