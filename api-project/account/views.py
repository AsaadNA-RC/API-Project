from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer


@api_view(['GET'])
def AccountApiOverview(req):
    content = {
        "/register": "Register an Account [POST]",
        "/login": "Login into the Account [POST]",
        "/refresh": "Generate a new Access token with the refresh token [POST]",
    }
    return Response(content)


'''
    This is for registering the user 
'''


class RegisterView(APIView):

    def post(self, req):
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "User account created",
        })
