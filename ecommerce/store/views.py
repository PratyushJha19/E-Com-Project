from django.shortcuts import render

def store(request):
    return render(request, 'store/store.html')

def base(request):
    return render(request, 'store/base.html')