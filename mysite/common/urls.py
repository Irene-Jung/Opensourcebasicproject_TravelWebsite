from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('country/', auth_views.LoginView.as_view(template_name='common/country.html'), name='country'),

    path('usa/', views.usa, name='usa'),
    path('japan/', views.japan, name='japan'),
    path('china/', views.china, name='china'),

]
