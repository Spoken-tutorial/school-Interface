# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User, Condition, MessageType, \
    Message, GroupPermission, Permission, Context
from django.contrib.auth.models import Group
from django.http import HttpResponse, JsonResponse
from .helper import manage_group_permissions


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


@api_view(['GET'])
def get_group_data(request):
    """Retrieve group-specific permissions and associated context data.

    This function takes a Django HTTP request object and returns a JSON response
    containing permissions and context data for a specified group.
    If the group has permission for a specific resource & context, the 'status' for that
    resource will be set to True; otherwise, it will be False.

    Args:
        request (HttpRequest): A Django HttpRequest object containing user request data.

    Returns:
        JsonResponse: A JSON response containing permissions and context data.
    """
    print(f"\033[91m ** {type(request)} \033[0m")
    group_id = request.GET.get('group_id')
    allowed_permissions = GroupPermission.objects.filter(role_id=group_id).values(
                          'permission_id', 'context_id')
    group_permissions = {item['permission_id']: item['context_id']
                         for item in allowed_permissions}
    context = context = list(Context.objects.values('id', 'name'))
    permissions = {}
    for item in Permission.objects.all():
        resource = item.resource
        if resource not in permissions:
            permissions[resource] = []
        permissions[resource].append({'id': item.id,
                                      'name': item.name,
                                      'status': (item.id in group_permissions),
                                      'context': group_permissions.get(item.id, 0)})
    data = {'permissions': permissions, 'context': context}
    return JsonResponse(data, status=status.HTTP_200_OK)


class PermissionsView(APIView):
    def post(self, request):
        try:
            data = request.data
            permissions = data.get('permissions', {})
            group = Group.objects.create(name=data.get('name', ''))
            manage_group_permissions(group, permissions)
            return Response({'message': f"Group {group} added."},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


class PermissionsDetailView(APIView):
    def patch(self, request, pk):
        data = request.data
        permissions = data.get('permissions', {})
        try:
            group = Group.objects.get(id=pk)
            name = data.get('name', None)
            if name:
                group.name = name
                group.save()
            manage_group_permissions(group, permissions)
            return Response({'message': f"Group {group} modified."},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
