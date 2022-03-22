from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router1 = DefaultRouter()

router1.register('users', views.UserViewSet, basename='users')
router1.register('tags', views.TagViewset, basename='tag')
router1.register('ingredients', views.IngredientViewset, basename='ingredient')
router1.register('recipes', views.RecipeViewset, basename='recipe')

urlpatterns = [
    path('', include(router1.urls)),
    path(
        'auth/token/login/',
        views.GetTokenView.as_view(),
        name='token_login'
    ),
    path(
        'auth/token/logout/',
        views.DelTokenView.as_view(),
        name='token_logout'
    ),
]