from django.urls import path,include
from .views import UserCreateView, LoginView, LogoutView, UserListView, TicketCreateView,ProfileView , UserUpdateView, UserTicketView, UserSignupView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('',TicketViewSet)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('list/', UserListView.as_view(),  name ='user-list'),
    path('ticket/', TicketCreateView.as_view(), name = 'ticket' ),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update/',UserUpdateView.as_view(),name='profile-update'),
    path('my-ticket/', UserTicketView.as_view(), name = 'ticket-view'),
    path('signupandlogin/', UserSignupView.as_view(), name ='signup-login'),
]