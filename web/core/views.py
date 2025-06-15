from django.shortcuts import render

def webapp_view(request):
    return render(request, 'webapp.html')

