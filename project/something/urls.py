from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('logout', views.Logout.as_view()),
    path('login', views.LoginView.as_view(), name='login'),
    path('add_url', views.AddURLView.as_view()),
    path('edit_url/<int:pk>', views.EditURLView.as_view()),
    path('delete_url/<int:id>/', views.delete),
    path('sign_up', views.SignUp.as_view()),

]