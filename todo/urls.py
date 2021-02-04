
from django.contrib import admin
from django.urls import path
from .views import TaskTodo,IndexView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TaskTodo.as_view(), name='tasktodo'),
    path('index/', IndexView.as_view(), name='index')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)