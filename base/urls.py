from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('room/<str:pk>/',views.room,name = 'Room Page'),
    path('profile/<str:pk>/',views.userProfile,name = "user-profile"),
    path('create-room/',views.createRoom,name = "create-room"),
    path('create-topic/',views.createTopic,name = "create-topic"),
    path('update-room/<str:pk>/',views.updateRoom,name = 'update-room'),
    path('delete-room/<str:pk>/',views.deleteRoom,name = 'delete-room'),
    path('login/',views.LoginPage,name = "Login"),
    path('logout/',views.logout_view,name = "Logout"),
    path('register/',views.register,name = "Register"),
    path('delete-message/<str:pk>/',views.deleteMessage,name = 'delete-message'),
    path('update-message/<str:pk>/',views.updateMessage,name = 'update-message'),
]