from django.shortcuts import render

from organization.models import Organization
from transaction.models import Transaction

# Create your views here.
def index(request):
    clients = Organization.objects.filter(org_type='CL').order_by('name')
    context = {
        'clients': clients,
    }
    return render(request, 'organization/index.html', context=context)

def org_detail(request, org_id):
    transactions = Transaction.objects.filter(seller_id=org_id) | Transaction.objects.filter(buyer_id=org_id)
    final_transactions = []

    for transaction in transactions:
        if transaction.seller_id == org_id:
            name, city, brokerage_rate = transaction.buyer, transaction.buyer.city, transaction.seller_brokerage_rate
        else:
            name, city, brokerage_rate = transaction.seller, transaction.seller.city, transaction.buyer_brokerage_rate

        final_transactions.append({
            'name': name,
            'city': city,
            'buyer': transaction.buyer,
            'broker': transaction.broker,
            'date': transaction.date,
            'item': transaction.item,
            'quantity': transaction.quantity,
            'weight': transaction.weight,
            'rate': transaction.rate,
            'brokerage_rate': brokerage_rate,
            'borkerage_amount': brokerage_rate * transaction.weight,
        })

    context = {
        'org_name': Organization.objects.get(pk=org_id).name,
        'transactions': final_transactions,
    }

    return render(request, 'organization/transaction.html', context)