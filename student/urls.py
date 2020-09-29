from .views import login, stdDashboard, stdApplicationForm, tpoDashboard, tpoReview, logoutStudent, logoutTPO

## these are for staic file handling.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    ## url for login page
    path('', login, name='login'),

    ## urls for Student Dashboard and Student Application Form
    path('stdDashboard/', stdDashboard, name='stdDashboard'),
    path('stdApplication/', stdApplicationForm, name='stdApplication'),

    ## urls for TPO Dashboard and Review
    path('tpoDashboard/', tpoDashboard, name='tpoDashboard'),
    path('tpoReview/<int:pk>', tpoReview, name='tpoReview'),

    ## urls for student and TPO logout
    path('logouts/', logoutStudent, name='logoutStd'),
    path('logoutt/', logoutTPO, name='logoutTPO'),

]

## urls for handling the static files like resumes.
## urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
