from django.conf.urls import url, include
import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views as auth_view

router = routers.DefaultRouter()
router.register(r'userbase', views.UserViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'owner', views.OwnerViewSet)
router.register(r'customer', views.CustomerViewSet)


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^', include(router.urls)),
    url(r'^register/$', views.UserViewSet.as_view({'post': 'create'})),
    url(r'^profile/$', views.profile_user),
    url(r'^login/$', auth_view.obtain_auth_token, name='login'),
    url(r'^cart/$', views.view_cart, name='view_cart'),
    url(r'^cart/modify/$', views.modify_cart, name='modify_cart'),
    url(r'^change/password/$', views.change_passqord, name="change-passqord"),
    


]
    