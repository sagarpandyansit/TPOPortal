from django.core.files.storage import default_storage, FileSystemStorage
from django.shortcuts import render, redirect

from student.forms import LoginForm
from .models import StudentApplicationForm, StudentLogin, TPO

                #### Student Views ####


##########  View to handle login for both TPO and Student ##########

def login(request):

    ## If login form submitted.
    if request.method == 'POST':
        form = LoginForm(request.POST)

        ## Check whether submittted form is valid or not.
        if form.is_valid():

            ## Retrieve all data from StudentLogin table.
            student = StudentLogin.objects.all()

            ## Check whether student is registered or not
            # for stud in student:
                if form.cleaned_data['email'] == stud.email and form.cleaned_data['password'] == stud.password:

                    ## Set session variables for student
                    request.session['course'] = stud.course
                    request.session['semester'] = stud.semester
                    request.session['department'] = stud.department
                    request.session['email'] = stud.email
                    request.session['mobno'] = stud.mobno

                    ## Redirect student to the dashboard.
                    return redirect('stdDashboard')
                else:
                    ## If credential is not match, check for other data in the table.
                    pass

            ## retrieve all data from TPO table.
            TPOtable = TPO.objects.all()

            ## Check whether TPO is registered or not
            for tpo in TPOtable:
                if form.cleaned_data['email'] == tpo.email and form.cleaned_data['password'] == tpo.password:

                    ## set session variable for TPO.
                    request.session['name'] = tpo.name

                    ## Redirect TPO to the tpoDashboard.
                    return redirect('tpoDashboard')
                else:
                    pass

            ## If email and password doesn't match to any data from any table, redirect to login page.
            form = LoginForm()
            return render(request, 'login.html', context={'form':form})

    else:
        form = LoginForm()
    # return render(request, 'login.html', {'form': form})

##########  View for handle login for both TPO and Student END ##########


##########   View for Stuent Dashboard   ##########

def stdDashboard(request):

    ## Check whether student logged in or not by session variable
    if 'fullname' in request.session:
        fullname = request.session['fullname']

        ## Retrieve all applications of logged in student.
        obj = StudentApplicationForm.objects.filter(email=request.session['email'])

        dict = {
            'fullname': fullname,
        }

        ## pass dictionary for student Dashboard to identify that user is logged in.
        return render(request, 'stdDashboard.html', context=dict)

    ## User is not logged in that's why no information will be passed to the student Dashboard.
    else:
        return render(request, 'stdDashboard.html')

##########   View for Stuent Dashboard END   ##########


##########  View for Student Application    ##########

def stdApplicationForm(request):

    ## Form is submitted
    if request.method == 'POST':
        app = StudentApplicationForm()

        ## Set all fields with the data coming from form.
        app.email = request.session['email']
        app.companyname = request.POST.get('companyname')
        app.position = request.POST.get('position')
        app.reason = request.POST.get('reason')

        ## File handling for resume.
        myfile = request.FILES['resume']
        fs = FileSystemStorage(
            location='statics/student/resumes')  # defaults to   MEDIA_ROOT
        filename = fs.save(myfile.name, myfile)
        file_url = fs.url(filename)
        app.resume = file_url
        app.save()

        ## Get the data for Student Dashboard
        stud = StudentLogin.objects.get(email=app.email)
        fullname = request.session['fullname']
        obj = StudentApplicationForm.objects.filter(email=stud.email)
        dict = {
            'obj': obj,
            'stud': stud,
            'fullname': fullname,
        }

        ## redirect to the student Dashboard
        return render(request, 'stdDashboard.html', context=dict)

    else:
        if 'fullname' in request.session:

            ## pass the session variable for Student Application page.
            course = request.session['course']
            department = request.session['department']
            semester = request.session['semester']
            email= request.session['email']
            mobno = request.session['mobno']
            dict = {
                'fullname':fullname,
                'course':course,
                'semester':semester,
                'department':department,
                'email':email,
                'mobno':mobno,
            }

            ## Redirect to the Student Application form.
            return render(request, 'stdApplicationForm.html', context=dict)

        ## Prevent student to access page without login.
        else:
            dict = {
                'login':1,
            }
            return render(request, 'stdApplicationForm.html', context=dict)

##########  View for Student Application    ##########


##########  View for Student Logout    ##########

def logoutStudent(request):

    # Session.objects.all().delete()

    ## delete all session variable to destroy session.
    for keys in list(request.session.keys()):
        del request.session[keys]

    ## Redirect to the Login page.
    return redirect('login')

##########  View for Student logout END    ##########


                #### Student Views END ####


                #### TPO views ####


##########  View for TPO Dashboard    ##########

def tpoDashboard(request):

    ## Check whether TPO  is logged in orr not
    if 'name' in request.session:
        name = request.session['name']

        ## Get all the student info
        stdobj = StudentLogin.objects.all()

        ## get all the application info
        obj = StudentApplicationForm.objects.all()
        dict = {
            'stdobj': stdobj,
            'obj': obj,
            'name': name,
        }

        ## Redirect to the Dashboard.
        return render(request, 'tpoDashboard.html', context=dict)

    ## TPO  is not logged in so, ask for login.
    else:
        return render(request, 'tpoDashboard.html')

##########  View for TPO Dashboard END    ##########


##########  View for TPO Review    ##########

def tpoReview(request, pk):

    ## Check whether form is submitted or not.
    if request.method == 'POST':

        ## Check for Approve button
        if 'approve' in request.POST:
            app = StudentApplicationForm.objects.get(pk=pk)

            ## Change status from 'Under Review to 'Approve'.
            app.status = 2
            app.save()
            return redirect('tpoDashboard')

        ## Check for Reject button.
        elif 'reject' in request.POST:
            app = StudentApplicationForm.objects.get(pk=pk)

            ## Change status from 'Under Review to 'Reject'.
            app.status = 0
            app.save()
            return redirect('tpoDashboard')

    ## Check whether TPO is logged in or not.
    if 'name' in request.session:

        ## Get all applications data.
        application = StudentApplicationForm.objects.get(pk=pk)

        ## Get all applications detail
        std = StudentLogin.objects.all()
        dict = {

            ## Get Desired Student info with getstudent() function.
            'student':getstudent(std, application.email),
            'application':application,
            'set':1,
            'name':request.session['name'],
        }

        ## Redirect to the TPOReview page.
        return render(request, 'tpoReview.html', context=dict)

    ## Redirect to the TPOReview page without dictionary.
    return render(request, 'tpoReview.html')

##########  View for TPO Review END    ##########

## function to get desired student info from table
# def getstudent(obj, appemail):
#     for iterator in obj:
#         if (appemail == iterator.email):
#             return iterator


##########  View for TPO logout    ##########

def logoutTPO(request):

    ## Clear session varibles
    for keys in list(request.session.keys()):
        del request.session[keys]

    ## Redirect to the login page.
    return redirect('login')

##########  View for TPO logout END    ##########


                #### TPO views END ####
