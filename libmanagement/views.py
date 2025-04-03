from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Members, Book,Records

def dashboard(request):
    context = {
        'total_members':  Members.objects.count(),
        'total_books': Book.objects.count(),
        'total_records': Records.objects.count(),
        'recent_members': Members.objects.order_by('-membership_date')[:5],
    }
    return render(request, './dashboard.html', context)

def Memberlist(request):
    context = {
        'members': Members.objects.all()
    }
    return render(request,'./student/student_list.html',context)

class Books(ListView):
    model = Book
    template_name = "courses/course_list.html"
    context_object_name = 'books'