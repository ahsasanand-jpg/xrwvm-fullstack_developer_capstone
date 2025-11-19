from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # ------ USER AUTH ENDPOINTS ------
    path('get_cars', views.get_cars, name='get_cars'),
    path('register', views.registration, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),

    # ------ DEALERSHIPS API ------
    # Fetch all dealers
    path('fetchDealers', views.get_dealerships, name='fetch_dealers'),

    # Fetch dealers by state
    path('fetchDealers/<str:state>', views.get_dealerships_by_state, name='fetch_dealers_by_state'),

    # Fetch single dealer by ID
    path('fetchDealer/<int:id>', views.get_dealer_by_id, name='fetch_dealer'),

    # ------ REVIEWS API ------
    # Fetch reviews for a dealer
    path('fetchReviews/dealer/<int:dealer_id>', views.get_reviews, name='fetch_reviews'),

    # Add a new review
    path('addReview', views.add_review, name='add_review'),

    # ------ CARMODEL & CARMAKE OPTIONAL ENDPOINTS (IBM requires admin CRUD only) ------
    # You can add these URLs if assignment needs it
    # path('carmakes', views.get_carmakes, name='carmakes'),
    # path('carmodels/<int:make_id>', views.get_carmodels, name='carmodels'),

]

# Serving media files (if needed)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
