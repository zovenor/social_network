var socket = new WebSocket('ws://' + window.location.host + '/like/');

socket.onmessage = function (event) {
    let data = JSON.parse(event.data);
    console.log(data);

    if (data.status == 'OK') {
        if (data.action == 'post_count_likes') {
            let el_text = document.getElementById('like_' + data.post_id);
            let el_img = document.querySelector('#like_img_' + data.post_id).children[0];
            console.log(el_img);
            el_text.innerText = data.count;
            if (data.is_liked) {
                el_img.src = STATIC_PATH + "/img/like.png";
                el_img.style.filter = "";
                el_img.style.opacity = 1;
            } else {
                el_img.src = STATIC_PATH + "/img/no-like.png"
                el_img.style.filter = "invert(1)";
                el_img.style.opacity = 0.75;
            }
        }
    }
    else{
        console.log('[Error] '+data.status);
    }
}

function like(id) {
    let data = {
        action: 'post_count_likes',
        post_id: id,
    };
    socket.send(JSON.stringify(data));
}