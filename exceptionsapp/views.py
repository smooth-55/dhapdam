
from django.shortcuts import render

def error_404(request, exception):
    print("exceptions")
    return render(request,'exceptions/400.html', status=404)

def error_500(request,  exception):
    return render(request,'exceptions/400.html', status=500)

def error_403(request,  exception):
    return render(request,'exceptions/400.html', status=403)


def error_400(request,  exception):
    return render(request,'exceptions/400.html', status=400)