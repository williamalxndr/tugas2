from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        "nama": "William Alexander",
        "npm": "2306226914",
        "kelas": "PBP E",
    }
    
    return render(request, "main.html", context)
