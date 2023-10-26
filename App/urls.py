from django.urls import path
from . import views



urlpatterns = [
        path('',views.home ,name="home"   ),
        path('about/',views.about_us ,name="about_us"   ),
        path('articles/',views.articles ,name="articles"   ),
        path('details/<int:pk>/',views.articles_details ,name="details"),
        path('create/',  views.articles_create ,name="create"   ),
        path('update/<int:pk>/', views.articles_update, name="update"),

    #path('articles/update/<int:article_id>/', views.articles_update, name='update_article'),

]







