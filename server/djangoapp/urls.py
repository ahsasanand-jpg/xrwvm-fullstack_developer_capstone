from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Correct Registration API as per instructions
    path('register', views.registration, name='register'),

    # Login API
    path('login', views.login_user, name='login'),

    # Logout API
    path('logout', views.logout_user, name='logout'),
]

# Serving Media Files (if used)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
