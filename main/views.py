from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nameclass' : 'Ameera Khaira Tawfiqa - KKI 2023',
        'name' : 'Cookie',
        'price': '5000',
        'description': 'Homey chocolate chip cookies baked fresh everyday'
    }

    return render(request, "main.html", context)