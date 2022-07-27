from django.urls import path
from .views import forums, posts, detail

urlpatterns = [
    path('', forums, name='forums'),
    path('posts/', posts, name='posts'),
    path('detail/', detail, name='detail'),
]
