from django.shortcuts import render, redirect

from organization.models import Organization
from transaction.models import Transaction

# Create your views here.
def index(request):
    clients = Organization.objects.filter(org_type='CL')
    brokers = Organization.objects.filter(org_type='BR')

    context = {
        'clients': clients,
        'brokers': brokers
    }
    return render(request, 'transaction/index.html', context=context)

def transaction(request):
    if request.method == 'POST':
        seller = Organization.objects.get(pk=request.POST['seller'])
        buyer = Organization.objects.get(pk=request.POST['buyer'])
        broker = Organization.objects.get(pk=request.POST['broker'])
        date = request.POST['date']
        item = request.POST['item']
        quantity = request.POST['quantity']
        weight = request.POST['weight']
        rate = request.POST['rate']
        brokerage_rate = request.POST['brokerage']

        transaction = Transaction(seller=seller, buyer=buyer, broker=broker, date=date, item=item, quantity=quantity, weight=weight, rate=rate, brokerage_rate=brokerage_rate)
        transaction.save()
        return redirect('transaction:index')
    
    return redirect('transaction:index')