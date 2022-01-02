from django.urls import path,include
from rest_framework.authtoken import views
from .views import Home

urlpatterns = [
    path('', Home , name='api.Home'),
    path('category/', include('api.category.urls'))
] 