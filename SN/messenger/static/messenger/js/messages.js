let socket = new WebSocket('ws://' + window.location.host + '/messenger/messages/' + person_name + '/')
// var messages = document.getElementById('message1');

socket.onopen = function (event) {
    console.log("[CONNECTED]");

}

socket.onmessage = function (event) {

    let data = JSON.parse(event.data);

    document.getElementById('messages').innerHTML = "";

    for (let el in data.messages){
        document.getElementById('messages').innerHTML += "<p>"+data.messages[el].text+"</p>";
    }
}
socket.onclose = function (event) {
    console.log(event);

}
