from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Member

def detail(request, slug):
    print slug
    member = get_object_or_404(Member, slug=slug)
    print member
    return render(request, 'member_detail.html', {'member': member})