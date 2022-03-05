from django.shortcuts import render
from django.views import View
from mainpage.views import base, user_is_authenticated, get_wordlist, page_not_found_view
from mainpage.models import UserDetail, Group
from django.contrib.auth.models import User
from .models import Message


class PersonalChatRoomView(View):
    @base
    @user_is_authenticated
    def get(self, request, name, content={}):
        content.update({
            'list': get_wordlist(request).PersonalChatRoom,
        })

        if User.objects.filter(username=name).exists():
            content['person'] = UserDetail.objects.get(user=User.objects.get(username=name))
        elif Group.objects.filter(groupname=name).exists():
            content['person'] = Group.objects.get(groupname=name)
        else:
            return page_not_found_view(self, request, content={})

        return render(request, 'messenger/personal_chat_room.html', content)


class ChatsView(View):
    @base
    @user_is_authenticated
    def get(self, request, content={}):
        chats = []

        chats_query = Message.objects.filter(user1=request.user.username).values('user2').distinct().union(
            Message.objects.filter(user2=request.user.username).values('user1').distinct())

        for el in chats_query:
            for el_in in el:
                chats += UserDetail.objects.get(user=User.objects.get(username=el[el_in])),

        content.update({
            'list': get_wordlist(request).Chats,
            'chats': chats,
        })

        return render(request, 'messenger/chats.html', content)
