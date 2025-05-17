from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.home, name="blog-home"),
    path('<int:post_id>/', views.post_detail, name="post-detail"),
    path('news/', views.news),
    path('category/<str:category_name>/', views.category_posts, name="category-posts"),
    path('<int:post_id>/delete/', views.post_delete, name="post-delete"),

    path('login/', views.user_login, name="user-login"),
    path('logout/', views.user_logout, name="user-logout"),


    # path('new/category/', views.new_category, name="new-category"),
    path('new/category/', views.NewCategory.as_view(), name="new-category"),
]
