from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('timeline/', TimelineView.as_view(), name='timeline'),
    path('new_tweet/', NewTweetView.as_view(), name='new_tweet'),
]
