from django.urls import  include,re_path
from profiles_api import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)
urlpatterns = [
    re_path(r'^hello-view',views.HelloApiView.as_view()),
    re_path(r'^login/',views.UserLoginApiView.as_view()),
    re_path(r'^',include(router.urls)),
]
