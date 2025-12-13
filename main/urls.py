from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:subject_slug>/', views.subject_detail, name='subject_detail'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
]