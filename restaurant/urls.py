from django.urls import path,include
from restaurant import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)


urlpatterns=[
    path('restaurant', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/menu-items/', views.MenuItemsView.as_view()),
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/api-token-auth/', obtain_auth_token),
]