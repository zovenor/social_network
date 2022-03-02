# Social network
## WebSockets
<b>Add/remove like in the post: </b> ws://{SITE_URL}/like/

<p>Request</p>

```yaml
{
    post: POST_ID,g
}
```
<p>Response example</p>

```yaml
{
    like: true,
    status: 'OK',
    count: 10,
    action: 'count',
    post: 5,
}
```