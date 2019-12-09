from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'xcp.html')

def xcp(request):
    return render(request,'xcp1.html')