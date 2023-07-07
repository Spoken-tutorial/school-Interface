# from django.shortcuts import render
from fuzzywuzzy import fuzz
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User, Condition, MessageType, Message
from django.contrib.auth.models import Group


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MessageWithinCommunity(APIView):

    def post(self, request):
        senderRole = request.data.get('sender_role')
        senderName = request.data.get('sender')
        recvName = request.data.get('msg_recv', [])
        message_ = request.data.get('message')
        msgtype = request.data.get('msg_type')
        recvRole = request.data.get('rec_role')


        x = User.objects.get(username=senderName)

        if hasattr(x, senderRole):
            s = Group.objects.get(name=senderRole)
            r = Group.objects.get(name=recvRole)
            m = MessageType.objects.get(messagetype=msgtype)
            matching_rows = Condition.objects.get(sender=s, receiver=r)
        elif msgtype == 'Bulk Message' and matching_rows.bulk_msg:
                pass
        else:
                print("not a valid combination")

        for i in range(0, len(recvName)):
            ide = User.objects.get(username=recvName[i])
            if hasattr(ide, recvRole):
                message = Message(
                    receiver=ide, sender=x, sender_role=s,
                    receiver_role=r, message=message_, message_type=m
                )
                message.save()
            else:
                print('not the role')
        else:
            print('Not a valid sender!!')
        response = HttpResponse("Message Part")
        return response


def partial(original,comparison):
    a1=fuzz.partial_ratio(original, comparison)
    return a1/100

def tokenratio(original,comparison):
    original=original
    comparison=comparison

    a2=fuzz.token_sort_ratio(original,comparison)
    return a2/100

def exact_match(original,comparison):

    if original == comparison:
        return 1
    return 0  

def match_location(n,e):
    q1=n.location
    q2=e.location
    s1=q1.address
    s2=q2.address
    a1=tokenratio(s1,s2)
    c1=q1.city.name
    c2=q2.city.name
    d1=q1.district.name
    d2=q2.district.name
    st1=q1.state.name
    st2=q2.state.name
    a2=exact_match(c1,c2)
    a3=exact_match(d1,d2)
    a4=exact_match(st1,st2)
    af=a2*a3*a4*a1
    return af


def match_name(original,comparison):

    a3=tokenratio(original,comparison)
    return a3
def match_usernamename(original,comparison):

    a3=tokenratio(original,comparison)
    return a3

def match_email(original,comparison):
    a4=partial(original,comparison)
    return a4

def match_phone(original,comparison):
    a5=exact_match(original,comparison)
    return a5
  
def Match_user(u1,u2):
    u1name=''
    u2name=''
    u1name=u1.first_name+u1.last_name
    u2name=u2.first_name+u2.last_name
    l=match_location(u1,u2)
    n=match_name(u1name,u2name)
    e=match_email(u1.email,u2.email)
    p=match_phone(u1.phone,u2.phone)
    u=match_usernamename(u1.username,u2.username)
    nm=n*e
    np=n*p
    ln=l*n*0.8
    ue=u*e
    maxi=max(nm,np,ln,ue)
    
    return(maxi)

class Match (APIView):
    def post(self, request):
        user1  =  request.data.get('user1')
        user2 =  request.data.get('user2')
        try:
            u1=User.objects.get(id=user1)
            u2=User.objects.get(id=user2)
            r=Match_user(u1,u2)
            
            if(r>0.5):
                print("Matched!",r)
                return HttpResponse("matched")
            else:
                print("not Match",r)
                return HttpResponse("not matched")
        except User.DoesNotExist:
            print("\n\n\n User not found! \n\n\n")
        

