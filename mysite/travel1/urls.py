from django.urls import path
from . import views

app_name = 'travel1'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:review_id>/', views.detail, name = 'detail'),
    path('answer/create/<int:review_id>/', views.answer_create, name='answer_create'),
    path('review/create/', views.review_create, name='review_create'),
    path('country/', views.country, name='country'),


]
