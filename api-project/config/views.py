from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def ApiOverview(req):
    content = {
        "/account": "Overview the Account API [GET]",
        "/todos": "Overview the Todos API [GET]",
    }
    return Response(content)
