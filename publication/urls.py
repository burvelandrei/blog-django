from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('publication/<int:id>', views.publication_detail, name='publication_detail')
]