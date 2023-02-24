from django.urls import path
from .views import *
 #http://127.0.0.1:8000/pro/ 
urlpatterns = [
    path('main/', view_main ,name='main'),
    path('home/',  view_home,name='home'),
    path('about/', view_about,name='about'),
    path('contactus/',  view_contactus,name='contactus'),
    path('gallery/',  view_gallery,name='gallery'),
    path('blogs/', view_blogs,name='blogs'),
    path('reviews/', view_reviews ,name='reviews'),
    path('components/',  view_components,name='components'),
    path('book_table/', view_book_table,name='booktable'),
    path('register/',view_registeration,name='register'),
    path('login/',view_login,name='login'),
    path('logout/',view_logout,name='logout'),
    

    

    

]

