from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import CursorPagination
from rest_framework.pagination import LimitOffsetPagination


class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
    cursor_query_param = 'cu'


# -----------
class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'
    page_size_query_param = 'records'
    max_page_size = 7
    last_page_strings = 'end'


class MyLimitOffsetPagination(LimitOffsetPagination):
    page_size = 5
    page_query_param = 'mylimit'
    page_size_query_param = 'myoffset'
    max_page_size = 6
    last_page_strings = 'end'