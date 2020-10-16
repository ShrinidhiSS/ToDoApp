from django.urls import path, include

from my_app import views

from django.conf.urls.static import static
from django.conf import settings

# from .views import TaskListView

urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.todoAdd,name='add'),
    # path('',TaskListView.as_view(),name='add'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)