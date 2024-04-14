from django.shortcuts import render

from organization.models import Organization

# Create your views here.
def index(request):
    clients = Organization.objects.filter(org_type='1')
    brokers = Organization.objects.filter(org_type='0')
    context = {
        'clients': clients,
        'brokers': brokers
    }
    return render(request, 'transaction/index.html', context=context)