from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    
    # as Class based views
    path('cart/', views.Cart.as_view(), name="cart"),
	path('', views.Index.as_view(), name='home'),
	path('prodview/<int:myid>', views.prodview, name='prodview'),

]