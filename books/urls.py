from django.urls import path
from rest_framework.routers import SimpleRouter


from .views import (BookListApiView, book_list_view, BookDetailView,
                    BookDeleteApiView, BookUpdateApiView, BookCreateApiView,
                    BookListCreateApiView, BookUpdateDeleteView, BookViewset,)

router = SimpleRouter()
router.register('books', BookViewset, basename='books')


urlpatterns = [
    # path('books/', BookListApiView.as_view(), name='book-list' ),
    # path('booklistcreate/', BookListCreateApiView.as_view(),),
    # path('bookupdatedelete/<int:pk>/', BookUpdateDeleteView.as_view(),),
    # path('books/<int:pk>/', BookDetailView.as_view()),
    # path('books/<int:pk>/update', BookUpdateApiView.as_view()),
    # path('books/<int:pk>/delete', BookDeleteApiView.as_view()),
    # path('books/create', BookCreateApiView.as_view()),
    # path('books/', book_list_view),
]

urlpatterns = urlpatterns+ router.urls



