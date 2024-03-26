from django.urls import path
from document.views import DocumentListCreateAPIView, DocumentDetailAPIView, DocumentAccessAPIView

urlpatterns = [
    path('', DocumentListCreateAPIView.as_view(), name='document-list-create'),
    path('<int:pk>/', DocumentDetailAPIView.as_view(), name='document-detail'),
    path('<int:pk>/access/', DocumentAccessAPIView.as_view(), name='document-access'),
]