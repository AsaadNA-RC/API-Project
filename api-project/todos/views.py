from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from .serializer import TodoSerializer
from .models import TodosData

# Todo CRUD
class Todo(APIView, LimitOffsetPagination):

    permission_classes = [IsAuthenticated]
    throttle_scope = 'todos'  # This is scoped throttle for this specific endpoint

    # This will retrieve all the todos for the authenticated user
    def get(self, req, format=None):
        data = TodosData.objects.filter(user=req.user)
        results = self.paginate_queryset(data, req, view=self)
        serializer = TodoSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    # This will create a new todo for the authenticated user
    def post(self, req):
        serialized = TodoSerializer(data=req.data)
        # Set the FK of the user to the authenticated user
        serialized.set_user_fk(req.user)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response({
            "message": "Todo created !",
            "data": serialized.data
        }, status=200)

    # Update todo with a specific ID
    def put(self, req, id):
        user_data = req.data
        result = TodosData.objects.filter(user=req.user, pk=id).update(
            todo_text=user_data['todo_text'], is_completed=user_data['is_completed'])
        if result > 0:  # if the fields are updated then we know we found them
            return Response({
                "message": "Todo updated!",
                "data": req.data
            }, status=200)
        else:
            return Response({"error": "Could not find todo to update!"}, status=400)

    # This will delete the todo with a specific ID
    def delete(self, req, id):
        try:
            result = TodosData.objects.get(user=req.user, pk=id).delete()
        except TodosData.DoesNotExist:
            return Response({"error": "Could not find todo to delete!"}, status=400)
        return Response({"message": "Todo deleted!"}, status=200)
