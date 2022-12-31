from rest_framework.pagination import PageNumberPagination


# Implementing Custom pagination using 'PageNumberPagination'
class MyPageNumberPagination(PageNumberPagination):
    page_size = 4

    # http://127.0.0.1:8000/list/?page=2
    # by default the query parameter for PageNumberPagination is 'page' if you want to change it then you can override it
    page_query_param = 'pg'
    # http://127.0.0.1:8000/list/?pg=2

    # if you want client to define the page size in that case you override this property
    page_size_query_param = 'records'
    # http://127.0.0.1:8000/list/?pg=2&records=3

    # you can also define the max page size that client can specify
    max_page_size = 5

    # if you will go to http://127.0.0.1:8000/list/?pg=last
    # then it will reach to the last page if you want to override the 'last' string in then:
    last_page_strings = 'end'
    # http://127.0.0.1:8000/list/?pg=end
