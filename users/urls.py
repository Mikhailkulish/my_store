from django.urls import path
from users.apps import UsersConfig
#from users.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = UsersConfig.name

urlpatterns = [
    #path('', PostListView.as_view(), name='post_list'),
    # path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # path('create/', PostCreateView.as_view(), name='post_create'),
    # path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    # path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete')
]