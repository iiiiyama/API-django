from django.urls import path
from .views import CommentlistAPIView, CommentdetailAPIView

urlpatterns = [
    path('API/', CommentlistAPIView.as_view()),
    path('API/<int:id>/', CommentdetailAPIView.as_view()),
]