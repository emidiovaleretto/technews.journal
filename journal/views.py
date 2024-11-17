from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'journal/index.html')


@login_required(login_url='index')
def members(request):
    return render(request, 'journal/members.html')
