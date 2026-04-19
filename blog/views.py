from django.shortcuts import render, get_object_or_404
from .models import Toy

def toy_list(request):
    data = Toy.objects.last()
    return render(request, "toy_list.html", {"data": data})

def toy_detail(request, slug):
    data = get_object_or_404(Toy, slug=slug)
    return render(request, "toy_list.html", {"data": data})