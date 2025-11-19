"""
djangoproj URL Configuration

Routes URLs to views and templates.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    
    # ----- STATIC FRONTEND PAGES -----
    path('', TemplateView.as_view(template_name="Home.html"), name='home'),
    path('about/', TemplateView.as_view(template_name="About.html"), name='about'),
    path('contact/', TemplateView.as_view(template_name="Contact.html"), name='contact'),

    # ----- AUTH PAGES (Frontend forms) -----
    path('login/', TemplateView.as_view(template_name="index.html"), name='login_page'),
    path('register/', TemplateView.as_view(template_name="index.html"), name='register_page'),

    # ----- ADMIN -----
    path('admin/', admin.site.urls),

    # ----- DJANGOAPP API ROUTES -----
    path('djangoapp/', include('djangoapp.urls')),
]

# Serving static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serving media files (if used)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
