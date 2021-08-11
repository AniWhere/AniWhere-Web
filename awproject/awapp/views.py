from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,"main.html")

def board(request):
    return render(request,"board.html")

def bookmark(request):
    return render(request,"bookmark.html")

def plan(request):
    return render(request,"plan.html")

def recommend(request):
    return render(request,"recommend.html")