from django.shortcuts import render, redirect
from .models import Chef, Dish

# Create your views here.
def index(request):
    context = {
        'all_chefs': Chef.objects.all(),
        'all_dishes': Dish.objects.all(),

    }
    return render(request, 'index.html', context)

def process_chef(request):
    Chef.objects.create(
        name=request.POST['name'],
        cuisine=request.POST['cuisine'],
        rank=request.POST['rank'],
    )
    return redirect('/')
def process_dish(request):
    this_chef = Chef.objects.get(id=request.POST["maker"])
    Dish.objects.create(
        name=request.POST["name"],
        tastiness_level=request.POST["tastiness_level"],
        spice=request.POST["spice"],
        maker=this_chef
    )
    return redirect('/')