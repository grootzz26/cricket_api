from rest_framework import pagination

class PlayerPagination(pagination.PageNumberPagination):
    page_size = 2
    page_query_param = 'p'

class MatchDetailsPagination(pagination.LimitOffsetPagination):
    default_limit = 2

class MatchNoPagination(pagination.CursorPagination):
    page_size = 3
    ordering = 'match'