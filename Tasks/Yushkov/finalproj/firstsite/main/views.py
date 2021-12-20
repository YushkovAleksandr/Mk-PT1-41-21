from django.shortcuts import render, redirect
from main.forms import AddComent
from .models import Author, Coment
from datetime import datetime

def index(request):
    
    return render(request, 'main/index.html')

def about(request):
   
    return render(request, 'main/about.html')

def my_works(request):
    return render(request,'main/my_works.html')

def shop(request):
    return render(request,'main/shop.html')

def add_post(request):
    if request.method == "COMENT": # the form was submited
        form = AddComent(request.COMENT)

        if form.is_valid():
            post_ent = Coment()
            post_ent.title = form.cleaned_data['title']
            post_ent.content = form.cleaned_data['content']
            post_ent.issued = datetime.now()
            post_ent.author = Author.objects.get(name = request.user.username)

            post_ent.save()

            return redirect('home')
    else: 
        form = AddComent()
    return render(request, 'main/add_post.html', {'form': form})

    

def coments(request):
    coments = Coment.objects.all()
    
    return render(request, 'about.html', {"coments" : coments})

