# TPOPortal
Complete Working model of traning and placement portal for college.

## Process of deployment on server:

1) Clone this repository with 'git clone <remote_url>'.

2) Go to your server and create new virtualenv with same python version (https://virtualenv.pypa.io/en/stable/reference/#cmdoption-p)

3) Activate virtualenv on server. 'source venv/bin/activate'

4) Install requirements.txt with pip. 'pip install -r requirements.txt'

5) Django migrations. 'python manage.py migrate'

6) Start django with runserver (to test) or connect webserver (nginx, uwsgi, gunicorn, ...). 'python manage.py runserver'


## Remote installation in your local machine.

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