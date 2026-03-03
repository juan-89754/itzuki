from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect # <--- 1. AÑADE ESTA IMPORTACIÓN

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vistas/', include('app.urls')),
    # 2. MODIFICA ESTA LÍNEA para que redirija al login automáticamente:
    path('', lambda request: redirect('login:login'), name='root_redirect'), 
    path('login/', include(('login.urls', 'login'), namespace='login')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)