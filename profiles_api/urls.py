from django.conf.urls import url, include
from profiles_api import views


urlpatterns = [
    url('hello-view',views.HelloApiView.as_view()),
]
