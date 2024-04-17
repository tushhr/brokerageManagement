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
