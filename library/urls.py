from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
)
from . import views

urlpatterns = [
    path('', BookListView.as_view(), name='library-home'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('about/', views.about, name='library-about'),
    path('order-b/', views.orderBook, name='order-book'),
    path('order-confirm-b/', views.orderConfirmBook, name='confirm-order-book'),
    path('addreview', views.addReview, name='add-review')
]
