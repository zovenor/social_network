from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from mainpage.models import User, UserDetail, Group
from messenger.models import Message
from django.core.serializers import serialize
from django.forms.models import model_to_dict
import json
import asyncio
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async, SyncToAsync
from time import sleep
from random import randint


class MessagesConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        personal_name = self.scope['url_route']['kwargs']['personal_name']
        response = {}

        @sync_to_async
        def get_messages(self, user1, user2):
            m1 = Message.objects.filter(user1=user1, user2=user2)
            m2 = Message.objects.filter(user1=user2, user2=user1)

            response = {
                'messages': [],
            }

            messages = m1.union(m2)

            for el in messages:
                response['messages'] += {
                                            'id': el.id,
                                            'user1': el.user1,
                                            'user1_name': f'{User.objects.get(username=el.user1).first_name} {User.objects.get(username=el.user1).last_name}',
                                            'user2': el.user2,
                                            'user2_name': f'{User.objects.get(username=el.user2).first_name} {User.objects.get(username=el.user2).last_name}',
                                            'datetime': el.time.strftime('%D %I:%H %p'),
                                            'text': el.text,
                                        },

            sleep(0.001)
            return response

        while True:
            await self.send(json.dumps(
                await get_messages(self, user1=str(self.scope['user']), user2=str(personal_name))
            ))

    async def disconnect(self, code=None):
        await self.disconnect()


class SendMessageConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    @sync_to_async()
    def receive_json(self, data):
        personal_name = self.scope['url_route']['kwargs']['personal_name']
        Message.objects.create(text=data['text'], user1=self.scope['user'], user2=personal_name)
        self.send(json.dumps({
            'status': 'OK',
            'text': data['text'],
        }))
