from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # TODO: add custom admin urls here (before admin.site.urls)
	path('s-a-a-s/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('app_store.urls')), # TODO: RENAME TO STORE
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
