from django.shortcuts import render


def wor_pad(request):
    return render(request, 'worpad.html')
