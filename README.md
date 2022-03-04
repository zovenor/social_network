# Social network
## WebSockets
<b>Add/remove like in the post: </b> ws://{ SITE_URL }/like/

<p>Request example</p>

```yaml
{
    action: 'post_count_likes',
    post_id: 5,
}
```
<p>Response example</p>

```yaml
{
    status: "OK",
    action: "post_count_likes",
    is_liked: true,
    count: 2,
    post_id: 5,
}
```
<b>Send message: </b> ws://{ SITE_URL }/messenger/send_message/{ NAME_OF_USER_OR_GROUP }

<p>Request example</p>

```yaml
{
    action: 'send_message',
    text: { SOME_TEXT_FOR_MESSAGE },
}
```
<p>Response example</p>

```yaml
{
    status: "OK",
    text: { REQUEST_TEXT }
}
```
