from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic import TemplateView
from .models import Publisher,Book
# Create your views here.
def myapp1(request):
    return render(request,'index.html')

class AboutView(TemplateView):
    template_name = "Hello.html"

class PublisherListView(ListView):
    model = Publisher #just need to call class name which is avalible in the models.py file..
    # template_name = "myapp/Hello.html"
    # We are able to call teplates using this method as well..
    #Defalt content object is ==Publisher_list.html

class BookListView(ListView):
    model = Book

class BookDetailsViews(DetailView):

    model = Book
    # template_name = 'mysite/templates/myapp/book_details.html'
    # Defalt content object is ==book_details.html