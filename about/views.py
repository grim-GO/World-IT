from django.shortcuts import render, redirect
from .forms import EmailForm
from django.views.generic import View

def about(request):
    return render(request, 'about.html')


class EmailView(View):
    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/about/')