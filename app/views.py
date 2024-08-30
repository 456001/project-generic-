from django.shortcuts import render

# Create your views here.
d={'name':'ashu','mob':'12345'}
def loops(request):
    return render(request,'loops.html',d)



d={'a':100,'b':20}
def conditions(request):
    return render(request,'conditions.html',d)
    