from rest_framework.pagination import LimitOffsetPagination


# Implementing Custom pagination using 'LimitOffsetPagination'
class MyLimitOffsetPagination(LimitOffsetPagination):

    # You can specify the limit:
    # http: // 127.0.0.1: 8000/list /?limit = 4
    # limit means page size

    # You can also specify the offset value
    # http://127.0.0.1:8000/list/?limit=4&offset=3
    # offset means to show us record from the given offset

    # you can also define the default limit
    default_limit = 5

    # if you want to override the 'limit' query params
    limit_query_param = 'size'

    # if you want to override the 'offset' query params
    offset_query_param = 'from'

    # define max limit
    max_limit = 6
