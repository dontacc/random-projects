from rest_framework.pagination import CursorPagination


class CustomCursorPagination(CursorPagination):
    cursor_query_param = "cursor"
    ordering = "-created_at"
    page_size = 1

