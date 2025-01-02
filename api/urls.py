from django.urls import path
from . import views

urlpatterns = [
    path('listings', views.ListCreateListingsView.as_view()),
    path('listings/<int:pk>', views.GetUpdateDeleteListingView.as_view()),
    path('contacts', views.ListContactsView.as_view()),

    # Auth
    path('signup', views.signup),
    path('login', views.login)
]
