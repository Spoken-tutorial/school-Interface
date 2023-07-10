# from django.shortcuts import render
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
            if msgtype == 'Single Message' and matching_rows.single_msg:
                pass
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
