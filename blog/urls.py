from django.urls import path

from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact/', contact, name='contact'),
    path('', HomeBlog.as_view(), name='home'),
    path('category/<int:category_id>/', BlogByCategory.as_view(), name='category'),
    path('blog/<int:pk>/', ViewBlog.as_view(), name='view_blog'),
    path('blog/add-blog/', CreateBlog.as_view(), name='add_blog'),
]
