from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('publication/<int:id>', views.publication_detail, name='publication_detail'),
    path('publication/add', views.add_publication, name="add_publication"),
    path('publication/<int:pk>/delete/', views.delete_publication.as_view(), name="delete_publication"),
    path('publication/<int:id>/comments/', views.add_comment, name='add_comment'),
    path('publication/<int:id>/edit', views.edit_publication, name="edit_publication"),
]