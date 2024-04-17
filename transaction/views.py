from django.shortcuts import render, redirect

from organization.models import Organization
from transaction.models import Transaction, Item

# Create your views here.
def index(request):
    clients = Organization.objects.filter(org_type='CL').order_by('name')
    brokers = Organization.objects.filter(org_type='BR').order_by('name')
    items = Item.objects.all()

    context = {
        'clients': clients,
        'brokers': brokers,
        'items': items,
    }
    return render(request, 'transaction/index.html', context=context)

def transaction(request):
    if request.method == 'POST':
        seller = Organization.objects.get(pk=request.POST['seller'])
        buyer = Organization.objects.get(pk=request.POST['buyer'])
        broker = Organization.objects.get(pk=request.POST['broker'])
        date = request.POST['date']
        item = Item.objects.get(pk=request.POST['item'])
        quantity = request.POST['quantity']
        weight = request.POST['weight']
        rate = request.POST['rate']
        seller_brokerage_rate = seller.brokerage_rate
        buyer_brokerage_rate = buyer.brokerage_rate

        transaction = Transaction(seller=seller, buyer=buyer, broker=broker, date=date, item=item, quantity=quantity, weight=weight, rate=rate,seller_brokerage_rate=seller_brokerage_rate, buyer_brokerage_rate=buyer_brokerage_rate)
        transaction.save()
        return redirect('transaction:index')
    
    return redirect('transaction:index')