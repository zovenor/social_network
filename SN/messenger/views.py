from django.shortcuts import render
from django.views import View
from mainpage.views import base, user_is_authenticated, get_wordlist


class ChatRoomView(View):
    @base
    @user_is_authenticated
    def get(self, request, name, content={}):
        content.update({
            'list': get_wordlist(request).ChatRoom,
        })

        return render(request, 'messenger/chat_room.html', content)
