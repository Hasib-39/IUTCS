from django.urls import path

from . import views

app_name = 'activity'

urlpatterns = [
    path('', views.index, name='activity'),
    path('create_activity/', views.createAchievement, name='create_activity'),
    path('edit_activity/<int:pk>', views.editActivity.as_view(), name='edit_activity'),
    path('update_activity/<int:pk>', views.updateActivity, name='update_activity'),
]