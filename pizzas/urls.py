from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "pizzas"

urlpatterns = [
    path('', views.index, name='index'),
    # "127.0.0.1:8000/ pizzas" just adds pizzas to the address bar
    path('pizzas', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza' ),
    path('comment/<int:pizza_id>/',views.comment, name='comment'),   

]