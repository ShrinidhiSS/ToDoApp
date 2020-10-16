from django.urls import path, include

from my_app import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

# from .views import TaskListView

urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.todoAdd,name='add'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.todoDelete, name='delete'),
    # path('',TaskListView.as_view(),name='add'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)