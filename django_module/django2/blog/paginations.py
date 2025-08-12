from django.core.paginator import InvalidPage
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.utils.urls import replace_query_param, remove_query_param


class CustomPagePagination(PageNumberPagination):

    def __init__(
            self,
            page: int = 1,
            url: str = ""
    ):
        self.page_number = page
        self.url = url

    def paginate_queryset(self, queryset):

        paginator = self.django_paginator_class(queryset, self.page_size)
        page_number = self.page_number

        try:
            self.page = paginator.page(page_number)
        except InvalidPage as exc:
            msg = self.invalid_page_message.format(
                page_number=page_number, message=str(exc)
            )
            raise NotFound(msg)

        return list(self.page)

    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        return replace_query_param(self.url, self.page_query_param, page_number)

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        if page_number == 1:
            return remove_query_param(self.url, self.page_query_param)
        return replace_query_param(self.url, self.page_query_param, page_number)
