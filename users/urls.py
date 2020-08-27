from django.urls import include, path

from .views import UserListView

urlpatterns = [
    path('', UserListView.as_view()),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),

]
