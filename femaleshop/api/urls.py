from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'produkty', views.ProductViewSet)
router.register(r'opinie', views.OpiniaViewSet)
router.register(r'uzytkownik', views.UzytkownikViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
