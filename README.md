# TPOPortal
Complete Working model of traning and placement portal for college.

CONTENTS OF THIS FILE
---------------------
 * [**Introduction**](#Introduction)
 * [**Working Model**](#WorkingModel)
 * [**Deploy over the server**](#deploy)
 * [**Installation on the local machine**](#local)

<a name="Introduction"></a>
## Introduction

* Developed a fully-functional Training and Placement Portal having an Training and Placment Officer and a student section.
* TPO controls all the activities in the portal.
* TPO can add new openings, and moderate application of students.
* Students can fill the application and see the status of their applications whether it is Rejected, Accepted or Under Review.
* **Technologies used**: Django, Bootstrap, JavaScript.

<a name="WorkingModel"></a>
## Working Model

 **Selected Snapshots of Portal:**
 
 ![Image of Student Dashboard](https://github.com/sagarpandyansit/TPOPortal/blob/master/Screenshots/LoginPageforboth.png)
 
 * Student Dashboard
 ![Image of Student Dashboard](https://github.com/sagarpandyansit/TPOPortal/blob/master/Screenshots/StudentDashboard.png)
 
 * TPO Dashboard
 ![Image of TPO Dashboard](https://github.com/sagarpandyansit/TPOPortal/blob/master/Screenshots/TPODashboard.png)
 
 * Student Application Form and Moderate by TPO
 ![Image of Student Application Form](https://github.com/sagarpandyansit/TPOPortal/blob/master/Screenshots/20200930_163956.gif)

<a name="deploy"></a>
## Deploy over the server:

1) Clone this repository with 'git clone <remote_url>'.

2) Go to your server and create new virtualenv with same python version (https://virtualenv.pypa.io/en/stable/reference/#cmdoption-p)

3) Activate virtualenv on server. 'source venv/bin/activate'

4) Install requirements.txt with pip. 'pip install -r requirements.txt'

5) Django migrations. 'python manage.py migrate'

6) Start django with runserver (to test) or connect webserver (nginx, uwsgi, gunicorn, ...). 'python manage.py runserver'

<a name="local"></a>
## Installation on the local machine:

1) Download and Install Python required version on your OS.

2) Install pip if working on Python 2, pip is package manager of Python it comes along with Python 3 but not with Python 2.

3) Read about virtualenv in Python. 

4) Create a virtual environment for your project.

5) Activate the environment in cmd.

6) Clone this repository with 'git clone <remote_url>'.

7) Install requirements.txt with pip. 'pip install -r requirements.txt'

8) Migrate Database to your local admin panel with 'python manage.py makemigrations' followed by 'python manage.py migrate'.

9) Create superuser with 'python manage.py createsuperuser' command.

10) You are done with installation process.

11) Run 'python manage.py runserver' and open '127.0.0.1:8000'(defualt_url) url into your browser.
