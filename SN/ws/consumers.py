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
            if json_data['action'] == 'post_count_likes':
                if Post.objects.filter(id=json_data['post_id']).exists():
                    post = Post.objects.get(id=json_data['post_id'])
                    response['status'] = 'OK'
                    response['action'] = 'post_count_likes'
                    if not post.likes.filter(user=user).exists():
                        post.likes.add(user_detail)
                        response['is_liked'] = True
                    else:
                        post.likes.remove(user_detail)
                        response['is_liked'] = False
                    response.update({
                        'count': post.count_likes(),
                        'post_id': json_data['post_id']
                    })
                else:
                    response['status'] = 'This post is not found!'
            else:
                response['status'] = 'This function is not found!'
        else:
            response['status'] = 'User is not aunthenticated!'

        self.send(json.dumps(response))
