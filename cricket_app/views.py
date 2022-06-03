from rest_framework import viewsets
from .serializer import PlayerSerializer, MatchDetailSerializer, MatchNoSerializer, StreamSerializer
from .models import matchNo, matchDetails, Stream, PlayerDetails
from .paginations import PlayerPagination, MatchDetailsPagination, MatchNoPagination

class matchDetailsView(viewsets.ModelViewSet):
    pagination_class = MatchDetailsPagination
    serializer_class = MatchDetailSerializer
    queryset = matchDetails.objects.all()

class matchNoView(viewsets.ModelViewSet):
    serializer_class = MatchNoSerializer
    queryset = matchNo.objects.all()
    pagination_class = MatchNoPagination

class PlayerDetailsView(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = PlayerDetails.objects.all()
    pagination_class = PlayerPagination