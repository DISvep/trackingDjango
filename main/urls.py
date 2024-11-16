from django.urls import path
from django.contrib.auth import views as auth_views
from .views import TaskList, TaskDetail, TaskCreate, TaskDelete, TaskUpdate, register, CommentDelete, CommentUpdate, LikeView, DislikeView


urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task-detail"),
    path("task/create/", TaskCreate.as_view(), name="task-create"),
    path('task/delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
    path('task/update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('comment/delete/<int:pk>', CommentDelete.as_view(), name='comment-delete'),
    path('comment/update/<int:pk>', CommentUpdate.as_view(), name='comment-update'),
    path('register/', register, name='register'),
    path('like/<int:pk>', LikeView.as_view(), name='like_comment'),
    path('dislike/<int:pk>', DislikeView.as_view(), name='dislike_comment')
]