from django.shortcuts import render


def lite(request):
    return render(request, 'lite.html')