# myapp/middleware.py
from django.db import connections
from django.utils.deprecation import MiddlewareMixin
from .models import Tenant
from django.conf import settings
from decouple import config
from django.shortcuts import redirect

config_file_path = "../.env"

class TenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        domain = request.get_host().split(':')[0]
        try:
            tenant = Tenant.objects.get(domain_url=domain)
            
            # Update the DATABASES settings for the current tenant
            settings.DATABASES['default'] = {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': tenant.db_name,
                'USER': tenant.db_user,
                'PASSWORD': tenant.db_password,
                'HOST': tenant.db_host,
                'PORT': tenant.db_port,
                'OPTIONS': settings.DATABASES['default'].get('OPTIONS', {}),
                'ATOMIC_REQUESTS': settings.DATABASES['default'].get('ATOMIC_REQUESTS', False),
                'AUTOCOMMIT': settings.DATABASES['default'].get('AUTOCOMMIT', True),
                'CONN_MAX_AGE': settings.DATABASES['default'].get('CONN_MAX_AGE', 0),
                'TIME_ZONE': settings.DATABASES['default'].get('TIME_ZONE', None),
            }
            
            # Ensure the new database settings are used
            connections.close_all()
            request.tenant = tenant
        except Tenant.DoesNotExist:
            request.tenant = None


class MultiTenantRouteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Determine the domain from the request
        domain = request.get_host().split(':')[0]

        # Check if the domain is for the landlord or a tenant
        if domain == config('LANDLORD_URL'):  # Replace with your landlord domain
            request.urlconf = 'website.urls'
        else:
            try:
                tenant = Tenant.objects.get(domain_url=domain)
                request.tenant = tenant
                request.urlconf = 'website.urls_tenant'
            except Tenant.DoesNotExist:
                # Handle case where tenant does not exist
                return redirect('some_error_page')

        response = self.get_response(request)
        return response