from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.views.static import serve
import os.path
import os
from django.conf import settings

from django.core.files.storage import FileSystemStorage
from .LSB.LSB import Encode,Decode
from .models import Music,BuyMusic
# Create your views here.
def index(request):
    arrayMusic = Music.objects.all()
    if request.user.is_authenticated:
        crUser = request.user
        print (crUser.username)
        ar = BuyMusic.objects.filter(user=crUser)
        print (len(ar))
        table = [0 for x in range(len(arrayMusic))]
        for x in range(len(arrayMusic)):
            if ar.filter(music=arrayMusic[x]):
                table[x] = 1
        list = zip(arrayMusic, table)
        return render(request, 'pages/index.html', {'list': list, 'damua': ar})
    else:
        return render(request, 'pages/index.html',{'list' : [], 'damua' : []})
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
    return render(request,'pages/register.html',{'form': form})

def buyMusic(request,id):
    user = request.user
    baihat = Music.objects.get(id=id)
    buymusic = BuyMusic()
    buymusic.user = user
    buymusic.music = baihat
    buymusic.save()
    return render(request, 'pages/buymusic.html', {'check': 'ok'})
def upLoad(request):
    if request.method == 'POST' and request.FILES['myfile'] and request.POST.get('namesong')  and request.POST.get('singer'):
        myfile = request.FILES['myfile']
        namesong = request.POST.get('namesong')
        singer = request.POST.get('singer')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        BASE = os.path.dirname(os.path.abspath(__file__))
        folder = os.path.join(BASE, "media")
        root = os.path.join(os.path.join(BASE,"static"),"musics")
        Encode(os.path.join(root,filename),os.path.join(folder,filename))
        fs.delete(myfile.name)
        Music.objects.create(name=namesong, casi=singer, link=myfile.name)
        return render(request, 'pages/upload.html', {
            'uploaded_file_url': 'Upload thành công!'
        })
    return render(request, 'pages/upload.html')
def check(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        BASE = os.path.dirname(os.path.abspath(__file__))
        folder = os.path.join(BASE, "media")
        result = Decode(os.path.join(folder, filename))
        return render(request, 'pages/check.html', {
            'result': result
        })
    return render(request, 'pages/check.html')
def download(request, path):
    BASE = os.path.dirname(os.path.abspath(__file__))
    root = os.path.join(os.path.join(BASE, "static"), "musics")
    file_path = os.path.join(root,path)
    if os.path.exists(file_path):
        return serve(request, os.path.basename(file_path), os.path.dirname(file_path))
    return HttpResponse ("Error 404.")