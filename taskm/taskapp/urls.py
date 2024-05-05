from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register_user"),

    path('show', views.show, name='show'),
    path('data', views.data, name='admin'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),

]

