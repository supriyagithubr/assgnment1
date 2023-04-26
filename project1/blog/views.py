from django.shortcuts import render, redirect
from .forms import BlogFrom
from .models import Blog
# Create your views here.
def addBlogView(request):
    form = BlogFrom()
    template_name = 'blog/add.html'
    context = {'form': form}
    if request.method=='POST':
        form = BlogFrom(request.POST)
        if form.is_valid():
            form.save()
    return render(request,template_name,context)



def showBlogView(request):
    data = Blog.objects.all()
    template_name = 'blog/show.html'
    context = {'obj':data}
    return render(request, template_name, context)



def updateBlogView(request, pk):
    print("value of pk:", pk)
    ord = Blog.objects.get(id = pk)
    #print(ord)
    form = BlogFrom(instance=ord)
    template_name = 'blog/add.html'
    context = {'form': form}
    if request.method == 'POST':
        form = BlogFrom(request.POST, instance=ord)
        if form.is_valid():
            form.save()
            return redirect('showblog_url')
    return render(request, template_name, context)


def deleteBlogView(request, pk):
    ord = Blog.objects.get(id=pk)
    template_name = 'blog/confirm.html'
    context = {'data':ord}
    if request.method=="POST":

        ord.delete()
        #print(ord)
        return redirect('showblog_url')
    return render(request,template_name, context)