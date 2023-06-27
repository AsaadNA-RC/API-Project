from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status
from django.urls import reverse

from .models import UserData,TodosData

class TodoTestCase(APITestCase):

    #Creating a new user and logging in
    def setUp(self):

        #Create User & Authorize him 
        user = UserData.objects.create_user(
            name="Asaad",
            email="asaad@gmail.com",
            password="123"
        )

        token = AccessToken.for_user(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        #Insert Data into database
        TodosData.objects.create(
            user_id="1",
            todo_text="Test hello world"
        )
    
    #Testing the Creation of Todo
    def test_create_todo(self):
        data = {
            "todo_text" : "Hello World",
        }

        response = self.client.post("/api/todos/" , data, follow=True)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['message'], "Todo created !")

    #Testing Fetch of all todos
    def test_get_all_todos(self):
        response = self.client.get("/api/todos", follow=True)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #Testing updating a todo
    def test_update_todo_exists(self):
        data = {
            "todo_text" : "Updated !",
            "is_completed" : False
        }

        response = self.client.put("/api/todos/1" , data, follow=True)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #Testing deleting a todo that does not exist
    def test_update_todo_not_exists(self):
        data = {
            "todo_text" : "Updated !",
            "is_completed" : False
        }

        response = self.client.put("/api/todos/3" , data, follow=True)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_todo(self):
        response = self.client.delete("/api/todos/1", follow=True)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)