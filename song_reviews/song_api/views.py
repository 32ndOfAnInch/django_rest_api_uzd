from rest_framework import generics, permissions
from . import models, serializers


class SongList(generics.ListAPIView):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SongReviewList(generics.ListCreateAPIView):
    queryset = models.SongReview.objects.all()
    serializer_class = serializers.SongReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
