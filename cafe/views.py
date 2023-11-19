from django.shortcuts import render,redirect
from .forms import CafeForm
from .models import Cafe


# Create your views here.
def index(request):
    context = {
    }
    return render(request, 'index.html', context)


def cafes(request):
    queryset = Cafe.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'cafes.html', context)


def add(request):
    form = CafeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CafeForm()
        return redirect(cafes)

    context = {'form': form}
    return render(request, 'add.html', context)
