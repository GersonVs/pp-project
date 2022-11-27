from django.urls import path
from apps.core.views import (ManageItem, ListItem, VoteItem)

app_name = 'core'

urlpatterns = [
    path('api/item/create/', ManageItem.as_view()),
    path('api/item/delete/', ManageItem.as_view()),
    path('api/item/list/'  , ListItem.as_view()),
    path('api/item/vote/'  , VoteItem.as_view()),
]
