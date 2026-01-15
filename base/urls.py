from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),

    path('home/', views.home, name='home'),

    path('register/', views.register_user, name='register'),

    path('logout/', views.logout_user, name='logout'),

    path('new_account/', views.new_account, name="new_account"),

    path('transfer/', views.transfer, name='transfer'),

    path('statements/', views.statements, name='statements'),

    path('deactivate_account/<int:pk>', views.deactivate_account, name='deactivate_account'),

    path('beneficiaries/', views.beneficiaries, name='beneficiaries'),

    path('fixed_deposits/', views.fixed_deposits, name="fixed-deposits"),

    path('analytics/', views.analytics, name="analytics"),
]