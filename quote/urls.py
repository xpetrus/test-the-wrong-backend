from django.urls import include, path
from rest_framework import routers
from quote import views


router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'quotes', views.QuoteViewSet)


urlpatterns = [
    path('', include(router.urls))
]