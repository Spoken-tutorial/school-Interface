# from django.urls import reverse
from rest_framework.test import APITestCase
from common.models import State, District, City
from django.contrib.auth.models import Group
from rest_framework import status
from datetime import date
from accounts.models import User, Message, MessageType, \
    Condition, Teacher, Profile, Location, School, Parent


class AccountsTest(APITestCase):
    def setUp(self):
        s = State.objects.create(id=1, name='Maharashtra')
        District.objects.create(id=1, name='Mumbai', state=s)
        City.objects.create(id=1, name='Mumbai', state=s)
        User.objects.create(
            username='user2',
            email='parent1@example.com',
            password='password1',
            first_name='Johne',
            last_name='Doev',
            phone='+1234567892'
        )
        self.post_data = {
            "user": {
                "username": "user3",
                "email": "user3@example.com",
                "password": "password1",
                "first_name": "Johne",
                "last_name": "Doev",
                "phone": "+1234567892"
            },
            "profile": {
                "user": "user",
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

        # Ensure we can create a new Training Team user.

        response = self.client.post(self.create_user_url, self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_organisation(self):

        # Ensure we can create a new Organisation.

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
        locat = Location.objects.create(
            address='lorem ipsum',
            state=state_,
            district=district,
            city=city,
            pincode='201010'
        )

        # Create a User instance
        teacher_user = User.objects.create(
            username='user1',
            email='teacher1@example.com',
            password='password',
            first_name='John',
            last_name='Doe',
            phone='+1234567890'
        )

        # Create a Profile instance
        teacher_profile = Profile.objects.create(
            user=teacher_user,
            dob='1991-06-05',
            gender='F',
            location=locat
        )

        # Create a School instance
        school = School.objects.create(
            added_by=teacher_user,
            name_of_association='kendriya vidyalaya 10',
            date_of_association=date(2023, 6, 27),
            type='Central Government Funded',
            organisation=None,
            location=locat,
        )

        # Create a Teacher instance
        sender = Teacher(
            user_ptr=teacher_user,
            school=school,
            profile=teacher_profile,
            unique_id='12345'
        )
        sender.save_base(raw=True)

        # Create a User instance
        parent_user = User.objects.create(
            username='user2',
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

        # Create a Message Type instance
        message_type = MessageType.objects.create(messagetype='Single Message')
        message_type = MessageType.objects.create(messagetype='Bulk Message')

        # Create a Condition instance
        Condition.objects.create(
            sender=sender_group,
            receiver=receiver_group,
            single_msg=1,
            bulk_msg=1
        )

        # Create a Message instance
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

           "sender_role": "teacher",
           "sender": "user1",
           "msg_recv": ["user2"],
           "message": "Hello user2 ",
           "msg_type": "Single Message",
           "rec_role": "parent"

        }
        self.url = 'http://127.0.0.1:8000/accounts/message-list'
        response = self.client.post(self.url, data=request_data, format='json', follow=True)
        self.assertEqual(response.status_code, 200)
