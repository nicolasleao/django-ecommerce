from django.http import Http404
from .models import Store

def get_current_store(request):
    try:
        current_domain = request.build_absolute_uri('/')
        store = Store.objects.get(domain=current_domain)
        return store
    except Store.DoesNotExist:
        raise Http404