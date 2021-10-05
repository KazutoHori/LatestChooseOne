from django.contrib import admin
from django.urls import path,include, re_path
from rest_framework.routers import SimpleRouter

from . import views

# router=SimpleRouter()
# router.register('api', views.QuestionsAPI, basename='questions')
# router.register('api-auth/', include('rest_framework.urls'), basename='auth')
# router.register('.*', views.root, basename='root')

# urlpatterns = router.urls

urlpatterns = [
    # path('api/<int:pk>', views.DetailAPI.as_view()),
    path('api/questions', views.QuestionsAPI.as_view()),
    path('api/users', views.UsersAPI.as_view()),
    re_path('.*', views.root),
]