from rest_framework.serializers import ModelSerializer
from .models import TodosData

class TodoSerializer(ModelSerializer):
    class Meta:
        model = TodosData
        # Avoid using exlcude
        fields = ['todo_id', 'todo_text', 'is_completed']

    # Sets the foreign key relation with the authenticated user
    def set_user_fk(self, user):
        self.user = user

    # Method Override
    def create(self, validated_data):
        validated_data["user"] = self.user
        return super().create(validated_data)
