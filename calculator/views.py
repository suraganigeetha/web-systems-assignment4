# calculator/views.py
from django.shortcuts import render

def tip_calculator(request):
    if request.method == 'POST':
        subtotal = float(request.POST['subtotal'])
        tip_percentage = float(request.POST['tip_percentage'])
        tip_amount = subtotal * (tip_percentage / 100)
        total_amount = subtotal + tip_amount
        return render(request, 'calculator/result.html', {'total_amount': total_amount})
    return render(request, 'calculator/index.html')
