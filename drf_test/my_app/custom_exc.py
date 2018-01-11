from rest_framework.response import Response
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # First get the default response
    res = exception_handler(exc, context)
    if res:
        return Response({'error': res.data})
    else:
        return Response({'error': 'Encountered unknown error {} {}'.format(exc, context)})
