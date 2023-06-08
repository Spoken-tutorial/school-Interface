from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from common.models import State, District, City
from accounts.models import User
# Create your tests here.

class AccountsTest(APITestCase):
    def setUp(self):
        s = State.objects.create(id=1,name='Maharashtra')
        d = District.objects.create(id=1,name='Mumbai',state=s)
        c = City.objects.create(id=1,name='Mumbai',state=s)
        u = User.objects.create_user(id=1,username="ankitamk",email="ankitamk@gmail.com",password="Root@123")
        self.post_data = {
            "user": {
                "first_name": "Aditi",
                "last_name": "P",
                "email": "aditip3@gmail.com",
                "username": "aditip3@gmail.com",
                "password":"Admin@1234"
            },
            "profile": {
                "dob": "1991-06-05",
                "gender": "F",
                "phone": "9810150191",
                
                "location": {
                    "address": "lorem ipsum",
                    "state_id" : 1,
                    "district_id" : 1,
                    "city_id" : 1,
                    "pincode": "201010"
                }
                
            }
        }
        # self.create_url = reverse('training-team-register-list')
        self.create_user_url = 'http://127.0.0.1:8000/accounts/register/training-team'
        
        self.org_data = {
            "name_of_association": "kendriya vidyalaya 10",
            "type": "Central Government",
            "location": {
                "address": "lorem ipsum",
                "state_id": 1,
                "district_id": 1,
                "city_id": 1,
                "pincode": "122011"
            },
            "added_by_id": 1
        }
        self.create_org_url = 'http://127.0.0.1:8000/accounts/register/organisations'
        
    def test_create_user(self):
        """
        Ensure we can create a new Training Team user.
        """
        response = self.client.post(self.create_user_url,self.post_data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_create_organisation(self):
        """
        Ensure we can create a new Organisation.
        """
        response = self.client.post(self.create_org_url,self.org_data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        