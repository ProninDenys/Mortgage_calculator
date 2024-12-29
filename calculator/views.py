from django.shortcuts import render

def mortgage_calculator(request):
    result = None
    data = {}  
    if request.method == 'POST':
        # Retrieve data from the form
        amount = request.POST.get('amount')
        term = request.POST.get('term')
        rate = request.POST.get('rate')

        # Save the entered data
        data = {'amount': amount, 'term': term, 'rate': rate}

        # Perform calculations
        if amount and term and rate:
            amount = float(amount)
            term = int(term) * 12  
            rate = float(rate) / 100 / 12  

            # Formula for annuity payment calculation
            monthly_payment = (amount * rate * (1 + rate) ** term) / ((1 + rate) ** term - 1)
            result = {
                'monthly_payment': round(monthly_payment, 2),
                'total_payment': round(monthly_payment * term, 2),
                'interest_paid': round(monthly_payment * term - amount, 2),
            }

    return render(request, 'calculator/mortgage_calculator.html', {'result': result, 'data': data})
