
from urllib import request
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse
from.models import  post
from .forms import postform  # Import your postform from the appropriate module


def home(request):
    return render (request,'home.html',{})
    
def about_us(request):
     return render (request,'about.html',{})
       


def articles(request):
    posts = [
        {
            'title': 'Blog post 1',
            'content': 'First post content',
            'date': 'August 10, 2020'
        },
        {
            'title': 'Blog post 2',
            'content': 'Second post content',
            'date': 'August 1, 2020'
        }
    ]
    blog =post.objects.all()

    return render(request, 'post.html', {'posts': posts,"blogs":blog})
#blog =post.objects.all()


 
 






     
 #return render(request, 'post_details.html',  context)from .models import Post  # Import the Post model (replace '.models' with your app name)

def articles_details(request, pk):
    blog = post.objects.get(pk=pk)  # Correct the model name to 'Post'
    context = {
        "post": blog,  # Assign the retrieved blog post to the "post" key
    }
    return render(request, 'post_details.html', context)

 
def articles_create(request):
    if request.method=="POST":
        form=postform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('articles'))
    else:
        form = postform()

    context = {
        "form": form,
    }
    return render(request, "create.html", context)





def articles_update(request, ):
    # Assuming you have an Article model with a primary key 'id' for articles
    article = get_object_or_404(articles, )

    if request.method == "POST":
        form = postform(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect(reverse('articles'))
    else:
        form = postform(instance=article)

    context = {
        "form": form,
        "article": article,  # You can pass the article object to the template for reference
    }
    return render(request, "update.html", context)







#def product_delete(request, pk):
  #  product_obj = get_object_or_404(Product, pk=pk)
   # product_obj.delete()
  #  return redirect(reverse("crudapp:product_list"))



    


      
    