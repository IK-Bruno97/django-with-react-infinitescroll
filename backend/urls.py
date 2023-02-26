from django.urls import path
from .views import getData, PostView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', getData),
    path('post/', PostView.as_view({'get': 'list', 'post': 'create'}) )
]
urlpatterns = format_suffix_patterns(urlpatterns)