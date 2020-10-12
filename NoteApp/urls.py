from django.urls import path,include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns =[

    path('', views.index, name='index'),
    path('create-note/',views.CreateNote,name="create-note"),
    path('more-info/<int:id>', views.MoreInfo, name="more-info"),
    path('delete/<int:id>', views.Delete, name="delete")
]