from django.shortcuts import render

# Create your views here.
def HomePage(request):
    pass
def SignupPage(request):
    return render(request,"singup.html")
def LoginPage(request):
    pass
