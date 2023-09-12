from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# tugas 2: function untuk show app main
def show_main(request):
    context = {
        'name': 'Kursi Gaming',
        'price' : '2000000',
        'amount' : '1',
        'description' : 'Kursi Gaming dengan desain menyerupai mobil sport akan meningkatkan kemampuan coding anda sebanyak 250%'
    }
    return render(request, "main.html", context)