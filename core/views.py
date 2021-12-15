from django.shortcuts import render
from core.models import University, Book, Project, Contact
from core.forms import ContactForm
from django.contrib import messages

# Create your views here.


def home(request):
    university_left = University.objects.all().order_by('-id')

    context = {
        'university_left' : university_left,
        # 'university_right' : university_right
    }
    # print(context)
    return render(request, 'index.html', context)










def about(request):
    return render(request, 'about.html')

def book(request):
    book = Book.objects.all().order_by('-id')
    context = {
        'book' : book
    }
    return render(request, 'book.html', context)

def project(request):
    project = Project.objects.all().order_by('-id')
    context = {
        'project' : project
    }
    return render(request, 'project.html', context)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        contact_data = request.POST
        form = ContactForm(data=contact_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız qeydə alındı')
            print('Form save')
        else:
            messages.success(request, 'Bosluqlari duzgun doldurun')
            print('Form is invalid')
    context = { 
        'form':form
    }
    return render(request, 'contact.html', context)