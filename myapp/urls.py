
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.myapp1,name='myapp1'),
    path('about',views.AboutView.as_view(),name="AboutView"),
    path('publishers', views.PublisherListView.as_view(), name="PublisherListView"),
    path("BookListView",views.BookListView.as_view(),name="BookListView"),
    path("<int:pk>",views.BookDetailsViews.as_view(),name="BookDetailsViews"),
]
