from django.conf.urls import url, include
from profiles_api import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
urlpatterns = [
    url('hello-view',views.HelloApiView.as_view()),
    url('',include(router.urls)),
]
