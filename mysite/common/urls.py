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
    path('japan/osaka/', views.osaka, name='japan/osaka'),
    path('japan/fukuoka/', views.fukuoka, name='japan/fukuoka'),
    path('japan/tokyo/', views.tokyo, name='japan/tokyo'),
    path('japan/kyoto/', views.kyoto, name='japan/kyoto'),
    path('china/', views.china, name='china'),
    path('france/', views.france, name='france'),
    path('thailand/', views.thailand, name='thailand'),
    path('spain/', views.spain, name='spain'),

]
