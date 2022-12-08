import json
import requests
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import SaveMemeForm
from .models import Meme


def random_meme():
    '''api call for random meme'''
    url = 'https://meme-api.com/gimme'
    response = json.loads(requests.get(url).text)
    meme = response['preview'][-1] # url to img
    return meme

# Create your views here.

def home(request):
    meme = request.session.get('meme', None)
    if not meme:
        meme = random_meme()
        request.session.flush()
        request.session['meme'] = meme
    form = SaveMemeForm(
                    initial={'img_url': meme}
                )
    if request.method == 'POST':
        form = SaveMemeForm(request.POST)
        if form.is_valid():
            Meme.objects.create(
                    img_url=form.cleaned_data.get('img_url')
                )
            return redirect(reverse('memes:home'))
    return render(request, 'home.html', {'meme': meme, 'form': form})
    

def new_meme(request):
    meme = random_meme()
    request.session['meme'] = meme
    return redirect(reverse('memes:home'))
    
    
def meme_list(request):
    items = Meme.objects.all().order_by('-time')
    if request.method == 'POST':
        meme_id = request.POST.get('id')
        obj = get_object_or_404(Meme, id=meme_id)
        obj.delete()
        return redirect(reverse('memes:meme_list'))
    return render(request, 'meme_list.html',{'items': items})


def about(request, *args, **kwargs):
    return render(request, 'about.html', {})
