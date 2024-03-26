from rest_framework import serializers
from document.models import Document, DocumentAccess

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'content', 'owner']

class DocumentAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentAccess
        fields = ['id', 'document', 'user', 'can_edit']
