from django.shortcuts import render

# Create your views here.
def image(request):
    return render(request,'image.html')

def image_2(request):
    return render(request,'image_2.html')