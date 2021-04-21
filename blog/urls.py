from .views import PostCreateView,PostDetailView,PostListView,PostUpdateView,PostDeleteView
from django.urls import path
from . import views


urlpatterns = [

    path("", PostListView.as_view() ,name="home" ),
    path("post/<int:pk>", PostDetailView.as_view() ,name="post-detail" ),
    path("post/<int:pk>/update", PostUpdateView.as_view() ,name="post-update" ),
    path("post/new/", PostCreateView.as_view() ,name="post-create" ),
    path("post/<int:pk>/delete", PostDeleteView.as_view() ,name="post-delete" ),


]
