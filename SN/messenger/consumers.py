from channels.generic.websocket import JsonWebsocketConsumer
from mainpage.models import User, UserDetail, Group
from messenger.models import Message
from django.core.serializers import serialize
from django.forms.models import model_to_dict
import json
from time import sleep


class MessagesConsumer(JsonWebsocketConsumer):
    def connect(self):
        personal_name = self.scope['url_route']['kwargs']['personal_name']

        response = {}

        # if User.objects.filter(username=personal_name).exists():
        # elif Group.objects.filter(groupname=personal_name).exists():

        # response['messages'][]
        # response['messages'] = messages_dict

        self.accept()

        while True:
            messages_queryset = Message.objects.filter(user1=self.scope['user'],
                                                       user2=personal_name).union(
                Message.objects.filter(user1=personal_name, user2=self.scope['user']))
            response['messages'] = []
            for el in messages_queryset:
                response['messages'] += {
                                            'id': el.id,
                                            'user1': el.user1,
                                            'user2': el.user2,
                                            'datetime': el.time.strftime('%D %I:%H %p'),
                                            'text': el.text,
                                        },
            sleep(0.001)

            self.send(json.dumps(response))

    def disconnect(self, code=None):
        self.disconnect()