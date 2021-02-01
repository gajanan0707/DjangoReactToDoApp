from django.shortcuts import render

# Create your views here.
#--user show view ---------#
def index(request):
    return render(request,'base.html')