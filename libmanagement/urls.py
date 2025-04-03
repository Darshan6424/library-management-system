from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('member/',views.Memberlist, name="member_list"),
    path('books/', views.Books.as_view(), name="books" )

]