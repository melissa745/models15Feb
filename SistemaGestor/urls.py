from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SistemaInteligente.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
