import json
from django.core.serializers import serialize
from channels.generic.websocket import JsonWebsocketConsumer
from mainpage.models import Post, UserDetail


class LikesConsumer(JsonWebsocketConsumer):

    def connect(self):
        self.accept()

    def receive_json(self, json_data):

        response = {}

        if self.scope['user']:
            user = self.scope['user']
            user_detail = UserDetail.objects.get(user=user)
            if json_data['get'] == 'count':
                if Post.objects.filter(id=json_data['post']).exists():
                    post = Post.objects.get(id=json_data['post'])
                    if not post.likes.filter(user=user).exists():
                        post.likes.add(user_detail)
                        response['like'] = True
                    else:
                        post.likes.remove(user_detail)
                        response['like'] = False
                    response.update({
                        'status': 'OK',
                        'count': post.count_likes(),
                        'action': 'count',
                        'post': json_data['post']
                    })
                else:
                    response['status'] = 'This post is not found!'
            else:
                response['status'] = 'This function is not found!'
        else:
            response['status'] = 'User is not aunthenticated!'

        self.send(json.dumps(response))
