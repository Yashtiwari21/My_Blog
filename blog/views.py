from django.shortcuts import render
import datetime
from .models import Post


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)
def forms(request):
    return render(request,"blog/forms.html")

def about(request):
    return render(request, "blog/about.html", {"title": "About"})

def submit(request):
    title=request.POST['title']
    author=request.POST['author']
    content=request.POST['content']
    date_posted=datetime.datetime.today()
    msg="Blog Is Uploaded Successfully"
    ps=Post(title=title,author=author,content=content,date_posted=date_posted,)
    ps.save()
    return render(request,'blog/forms.html',{'msg':msg})
    return redirect('forms')

