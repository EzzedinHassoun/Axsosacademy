from django.urls import path
from . import views
urlpatterns = [    
    path('', views.index ),  
    path('add_course',views.add_course),
    path('destroy/<int:courseid>',views.confirm_delete),
    path('courses/delete/<int:courseid>',views.delete_course)
]
