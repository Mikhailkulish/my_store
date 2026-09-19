from django.urls import path
from blog.apps import BlogConfig
# from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = BlogConfig.name

urlpatterns = [
#     path('', ProductListView.as_view(), name='product_list'),
#     path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
#     path('create/', ProductCreateView.as_view(), name='product_create'),
#     path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
#     path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
#     path('contacts/', ContactsView.as_view(), name='contacts')
]