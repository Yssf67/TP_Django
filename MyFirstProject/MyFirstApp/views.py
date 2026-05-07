from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'MyFirstApp/index.html')
    return render(request, 'MyFirstApp/index2.html')

