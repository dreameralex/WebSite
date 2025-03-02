
from django.urls import path
from home import views as home_views


urlpatterns = [
    path('credits/', home_views.credits, name='credits'),
    path('', home_views.post_list, name='post_list'),
]