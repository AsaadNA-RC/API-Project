from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status
from django.urls import reverse

from .models import UserData

NAME = "Asaad Noman"
EMAIL = "asaad.abbasi@gmail.com"
PASSWORD = "1234"

class AccountTestCase(APITestCase):

   
    def setUp(self):
        #Create User & Authorize him 
        user = UserData.objects.create_user(
            name = NAME,
            email = EMAIL,
            password = PASSWORD
        )

        self.data = {
            "name" : NAME,
            "email" : EMAIL,
            "password" : PASSWORD
        }

    #Testing the Creation of An Account
    def test_register_account(self):
        data = {
            "name" : "Ali",
            "email" : "ahmed@gmail.com",
            "password" : "123"
        }
        response = self.client.post("/api/account/register" , data, follow=True)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #Testing Login with exisiting user
    def test_login_account_exists(self):
        response = self.client.post("/api/account/login" , self.data, follow=True)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #Testing Login with non existing user
    def test_login_account_not_exists(self):
        data = {
            "email" : 'ahmed@gmail.com',
            "password" : PASSWORD
        }
        response = self.client.post("/api/account/login" , data, follow=True)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)