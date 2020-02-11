from django.shortcuts import render


def watch(request):
    return render(request, 'watch.html')
