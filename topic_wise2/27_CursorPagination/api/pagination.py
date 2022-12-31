from rest_framework.pagination import CursorPagination


# Implementing Custom pagination using 'CursorPagination'
class MyCursorPagination(CursorPagination):
    page_size = 5

    # if you added 'created' field inside model in that case it could have pagination using 'created' filed
    # but we have not specify that field we have to specify the different field here
    ordering = 'name'

    # if you want to override the cursor parameter in that case you can specify this
    cursor_query_param = 'cu'
