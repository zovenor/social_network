var socket = new WebSocket('ws://' + window.location.host + '/like/');

socket.onmessage = function (event) {
    let data = JSON.parse(event.data);
    console.log(data);

    if (data.status == 'OK') {
        if (data.action == 'count') {
            let el_text = document.getElementById('like_' + data.post);
            let el_img = document.querySelector('#like_img_' + data.post).children[0];
            console.log(el_img);
            el_text.innerText = data.count;
            if (data.like) {
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
        post: id,
        get: 'count'
    };
    socket.send(JSON.stringify(data));
}