# from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from common.models import State, District, City
from django.contrib.auth.models import Group
from django.urls import reverse
from common.models import State,District,City
from django.test import TestCase

from rest_framework.test import APIClient
from datetime import date
from accounts.models import User, Message, MessageType, Condition, Teacher, Profile, Location, School, Parent, Location

 class AccountsTest(APITestCase):
    def setUp(self):
        s = State.objects.create(id=1, name='Maharashtra')
        District.objects.create(id=1, name='Mumbai', state=s)
        City.objects.create(id=1, name='Mumbai', state=s)
        User.objects.create(id=1, username="ankitamk", email="ankitamk@gmail.com",
                                 password="Root@123")
        self.post_data = {
            "user": {
                "first_name": "Aditi",
                "last_name": "P",
                "email": "aditip3@gmail.com",
                "username": "aditip3@gmail.com",
                "password": "Admin@1234"
            },
            "profile": {
                "dob": "1991-06-05",
                "gender": "F",
                "phone": "9810150191",

                "location": {
                    "address": "lorem ipsum",
                    "state_id": 1,
                    "district_id": 1,
                    "city_id": 1,
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
        #Ensure we can create a new Training Team user.
"""
        response = self.client.post(self.create_user_url, self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_organisation(self):
        """
        #Ensure we can create a new Organisation.
"""
        response = self.client.post(self.create_org_url, self.org_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
        
 class MessageWithinCommunity1(APITestCase):

    def setUp(self):
        sender_group = Group.objects.create(name='teacher')
        receiver_group = Group.objects.create(name='parent')      
        state_ = State.objects.create(id=1, name='Maharashtra')
        district = District.objects.create(id=1, name='Mumbai', state=state_)
        city = City.objects.create(id=1, name='Mumbai', state=state_)

        # Create a Location instance
        l = Location.objects.create(
            address='lorem ipsum',
            state=state_,
            district=district,
            city=city,
            pincode='201010'
        )

        # Create a User instance
        teacher_user = User.objects.create(
            username='athmikha',
            email='teacher1@example.com',
            password='password',
            first_name='John',
            last_name='Doe',
            phone='+1234567890'
        )
       
        # Create a Profile instance and associate it with the User and Location instances
        teacher_profile = Profile.objects.create(
            user=teacher_user,
            dob='1991-06-05',
            gender='F',
            location=l
        )
    
        school = School.objects.create(
            added_by=teacher_user,
            name_of_association='kendriya vidyalaya 10',
            date_of_association=date(2023, 6, 27),
            type='Central Government Funded',
            organisation=None,  # If applicable, replace with the appropriate Organisation instance
            location=l,
        )
        
        sender = Teacher(user_ptr=teacher_user,school=school,profile=teacher_profile,unique_id='12345')
        sender.save_base(raw=True)
        q=Teacher.objects.all()
        
        parent_user = User.objects.create(
            username='janthuu',
            email='parent1@example.com',
            password='password1',
            first_name='Johne',
            last_name='Doev',
            phone='+1234567892'
        )
       
        # Create a Parent instance and associate it with the User instance
        receiver = Parent(
            user_ptr=parent_user
        )
        receiver.save_base(raw=True)
        message_type = MessageType.objects.create(messagetype='Single Message')
        message_type = MessageType.objects.create(messagetype='Bulk Message')
        
        Condition.objects.create(sender=sender_group, receiver=receiver_group,single_msg=1,bulk_msg=1)
        Message.objects.create(
            message='Test message',
            sender=sender,
            sender_role=sender_group,
            receiver=receiver,
            receiver_role=receiver_group,
            message_type=message_type
        )
        self.url = 'http://127.0.0.1:8000/accounts/message-list'

    def test_get_with_valid_data(self):
        # Test the 'get' method with valid data
        request_data = {
            
           "sender_role" : "teacher",
           "sender" : "athmikha",
           "msg_recv" : ["janthuu"],
           "message" : "Hello janthuuu ",
           "msg_type" : "Single Message",
           "rec_role" : "parent"

        } 
        
        self.url = 'http://127.0.0.1:8000/accounts/message-list'
        response = self.client.post(self.url, data=request_data, format='json', follow=True)
        self.assertEqual(response.status_code, 200)


class LocationMatchTestCase(TestCase):
    def setUp(self):
        state_ = State.objects.create(id=1, name='Maharashtra')
        state1_ = State.objects.create(id=2, name='tamil nadu')
        district = District.objects.create(id=1, name='Mumbai', state=state_)
        city = City.objects.create(id=1, name='Mumbai', state=state_)
        self.location1 = Location.objects.create(address='Address 1', state=state_, district=district, city=city, pincode='123456')
        self.location2 = Location.objects.create(address='Address 2', state=state1_, district=district, city=city, pincode='654321')
        self.user1 = User.objects.create(username='user1', first_name='Johne', last_name='Doev', email='user1@example.com', phone='1234567890',location_id=self.location1.id)
        self.user2 = User.objects.create(username='athmikha', first_name='athmikha',last_name='cds', email='ath2@example.com', phone='9876543210',location_id=self.location2.id)
       
      

    def test_match_location_view(self):
        request_data = {
            "user1": self.user1.id,
            "user2": self.user2.id
        }
        url = 'http://127.0.0.1:8000/accounts/match/' 
        response = self.client.post(url, data=request_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'matched')