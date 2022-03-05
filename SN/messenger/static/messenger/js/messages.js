let socket = new WebSocket('ws://' + window.location.host + '/messenger/messages/' + person_name + '/')
let socket2 = new WebSocket('ws://' + window.location.host + '/messenger/send_message/' + person_name + '/')
// var messages = document.getElementById('message1');

socket.onopen = function (event) {
    console.log("[SOCKET] connected");

}

socket.onmessage = function (event) {

    let data = JSON.parse(event.data);

    // console.log(data);

    if(data.status == "OK"){
        alert("ВОт");
    }

    document.getElementById('messages').innerHTML = "";

    for (let el in data.messages) {
        if (data.messages[el].user1 != person_name) {
            document.getElementById('messages').innerHTML = "<p class='message user1'>" + "<b class='user_name user1_name'>" + data.messages[el].user1_name + ": </b>" + data.messages[el].text + "<br><time>"+ data.messages[el].datetime +"</time>" + "</p>" + document.getElementById('messages').innerHTML;
        } else {
            document.getElementById('messages').innerHTML = "<p class='message user2'>" + "<b class='user_name user2_name'>" + data.messages[el].user1_name + ": </b>" + data.messages[el].text + "<br><time>"+ data.messages[el].datetime +"</time>" + "</p>" + document.getElementById('messages').innerHTML;
        }
    }
    // go_to_last_message();
    // if(messages.scrollHeight-messages.scrollTop < 780){
    //     go_to_last_message();
    // }
}
socket.onerror = function (event) {
    console.log(event);
}

socket.onclose = function (event) {
    // alert("Some problems with connection");
    window.location.reload();
}

socket2.onopen = function (event){
    console.log('[SOCKET2] connected ');
    // go_to_last_message();
}

socket2.onclose = function (event){
    console.log(event);
}

socket2.onmessage = function (event){
    console.log(event);
}

mes_input.onkeydown = function (e) {
    if (e.key == "Enter") {
        let data = {
            action: 'send_message',
            text: mes_input.value,
        };
        mes_input.value = "";
        socket2.send(JSON.stringify(data));
        // setTimeout(scroll_to_last_message, 300);
    }
}

// function scroll_to_last_message(){
//     messages.scrollTo({ top: messages.scrollHeight, behavior: 'smooth' });
// }
// function go_to_last_message(){
//     messages.scrollTo({ top: messages.scrollHeight});
// }