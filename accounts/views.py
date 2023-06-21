# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User, Role, Condition, MessageType, Message


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


class InputValue(APIView):
    def get(self, request, sender, username):
        msg_recv = []
        n = int(input("Enter Number of Receiver: "))
        for i in range(0, n):
            print("User", i+1, ": ")
            val = input()
            try:
                User.objects.get(username=val)
                msg_recv.append(val)
            except User.DoesNotExist:
                print("Not a Valid Receiver!!")

        message_ = input("Enter the message: ")
        msg_type = input("Enter the message type 'single' or 'bulk' : ")
        rec_role = input("Enter the Receiver role: ")

        response = MessageWithinCommunity.get(
            request, username, sender, msg_recv,
            rec_role, message_, msg_type
        )

        return response


class MessageWithinCommunity(APIView):

    def get(request, sendername, senderRole, recvName, recvRole, message_, msgtype):
        x = User.objects.get(username=sendername)
        if hasattr(x, senderRole):
            s = Role.objects.get(role=senderRole)
            r = Role.objects.get(role=recvRole)
            m = MessageType.objects.get(messagetype=msgtype)

            matching_rows = Condition.objects.get(sender=s, receiver=r)
            if msgtype == 'single' and matching_rows.single_msg:
                pass
            elif msgtype == 'bulk' and matching_rows.bulk_msg:
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
