# Social network
## WebSockets
<b>Add/remove like in the post: </b> ws://{SITE_URL}/like/

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
