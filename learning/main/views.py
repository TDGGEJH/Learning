from django.shortcuts import render, get_object_or_404, redirect
from .models import Shodki
from .forms import ShodkaForm

def index(request):
    shodki = Shodki.objects.order_by('id')
    return render(request, "main/home.html", {'title':'Дом', 'shodki':shodki})
def about(request):
    shodki = Shodki.objects.order_by('id')
    return render(request, "main/home.html", {'title':'Про нас', 'shodki':shodki})

def shodka_detail(request, shodki_id):
    shodki = Shodki.objects.order_by('id')
    shodka = get_object_or_404(Shodki, id=shodki_id)
    return render(request, "main/shodki_detail.html", {'title':shodka.title, 'shodki':shodki, 'shodka':shodka})

def create_shodka(request):
    if request.method == "POST":
        form = ShodkaForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')

    shodki = Shodki.objects.order_by('id')
    form = ShodkaForm
    return render(request, "main/create_shodka.html", {'form':form,'title':'Создать сходку', 'shodki':shodki})
    