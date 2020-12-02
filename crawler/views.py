from django.shortcuts import render, HttpResponse
from crawler.models import Impressora
from crawler.forms import ImpressoraForm
from crawler.manager import ImpressoraManager

# Create your views here.

def index(request):
    impressoras = Impressora.objects.all()

    for impressora in impressoras:
        tmp = ImpressoraManager(impressora.id);
        tmp.obter_status();

    return render(request, 'crawler/index.html', {'impressoras': impressoras})

def impressora_adicionar(request):
    form = ImpressoraForm(request.POST or None)


    if form.is_valid():
        form.save()
        return HttpResponse('<script>location.reload();<script>')
    
    return render(request, 'crawler/impressora_adicionar.html', {'form': form})