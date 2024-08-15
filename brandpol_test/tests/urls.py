from django.urls import path
from . import views

urlpatterns = [
    path("", views.tests_home, name='tests_home'),
    path("create", views.create_test, name='create'),
    path('<int:pk>', views.TestDetailView.as_view(), name='test_detail'),
    path('<int:pk>/update', views.TestUpdateView.as_view(), name='test_update'),
    path('<int:pk>/delete', views.TestDeleteView.as_view(), name='test_delete'),
    path('<int:pk>/create_quest', views.create_quest, name='create_quest')
]