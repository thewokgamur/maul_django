from django.shortcuts import render

# Create your views here.
def tranding(request):
    return render(request, 'menu/tranding.html')
def topik(request):
    return render(request, 'menu/topik.html')
def Shoping(request):
    return render(request, 'menu/shoping.html')
def News(request):
    return render(request, 'menu/News.html')
def Berita(request):
    return render(request, 'menu/Berita.html')
def Acation(request):
    return render(request, 'menu/Acation.html')
def profile(request):
    return render(request, 'menu/profile.html')
def all(request):
    return render(request, 'menu/all.html')