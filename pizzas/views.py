from django.shortcuts import render, redirect
from pizzas.models import *
from .forms import *

# Create your views here.
#(request) is what the webpage is doing, getting info from the database

# since this is our homepage, not doing much but just displaying our homepage
# and the view points to a html template
# this is where we connect the template to the view
def index(request):
    return render(request, 'pizzas/index.html')

#page displaying all pizza types
def pizzas(request):

#sorts it by pizza_name asc. put -pizza_name for desc
# this line retrieves the data from datbase
    pizzas =  Pizza.objects.all().order_by('pizza_name')

    # context gives us our data
    # the key is the variable name that we are using for our html file
    # the value is the variable name that we are using in our view
    context = {'pizzas':pizzas}

    # this renders both templates and our data
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)
    toppings = Topping.objects.filter(pizza=p)
    new_comments = Comment.objects.filter(pizza=pizza_id).order_by('-date_added')
    image = Image.objects.filter(pizza=pizza_id)

    context = {'pizza':p, 'toppings': toppings, 'new_comments': new_comments, 'image': image}

    return render(request, 'pizzas/pizza.html', context)
    
def comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
        
    else:
        form = CommentForm(data=request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pizza = pizza
            comment.save()

            return redirect('pizzas:pizza', pizza_id=pizza_id)
    
    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/comment.html', context)

