
from django.urls import path
from . import views
urlpatterns = [

    path('signup/',views.RegisterView.as_view()),

    path('login/',views.LoginView.as_view()),
    path('vertical/',views.ShowProductsByVerticals.as_view()),
    path('addproduct/',views.ProductView.as_view()),
    path('add-to-cart/<int:product_id>/',views.AddToCartView.as_view()),
    path('cart/',views.CartView.as_view()),
    path('history/',views.OrderView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('check-auth/',views.authenticate),
    path('get-populars/',views.PopularView.as_view()),
]
