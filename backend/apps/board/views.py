from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.board.models import NoticeBoard
from apps.board.serializers import NoticeBoardSerializer
from config.pagination import BasicPagination


class NoticeBoardViewSet(ModelViewSet):
    queryset = NoticeBoard.objects.all().order_by('id')
    serializer_class = NoticeBoardSerializer
    pagination_class = BasicPagination
    permission_classes = [AllowAny]
