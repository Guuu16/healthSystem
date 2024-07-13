from django.urls import path
from .views import *

urlpatterns = [
    path('gift_detail/', gift_detail, name='gift_detail'),
    path('assignGifts/', assignGifts, name='assignGifts'),
    path('view_rewards/',view_rewards,name='view_rewards')

]
