from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406413104',
        'name': 'Elliot Randy Panggabean',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)