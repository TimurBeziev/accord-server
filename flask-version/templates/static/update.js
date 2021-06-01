setInterval(function () {
    updateChats();
}, 250);

var chatUpdateInterval = null
var chatUpdateId = null

function updateChats() {
    fetch(`http://localhost:${location.port}/ui/check_for_new_chats`)
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            document.getElementById("some_menu").innerHTML = ""
            for (var i = 0; i < data.length; ++i) {
                document.getElementById("some_menu").innerHTML +=
                    `<div class="menu-container" onclick=onChatClick(this) id=${data[i].id}> ${data[i].name} </div>`
            }
        })
}

function onChatClick(object) {
    if (chatUpdateInterval) {
        clearInterval(chatUpdateInterval)
    }
    document.getElementById("chat_name").innerHTML =
        `<h1 align="center" id="current_chat_info" chat_id=${object.id}> ${object.innerText} </h1>`
    chatUpdateId = object.id
    chatUpdateInterval = setInterval(function () {
        updateChat()
    }, 1000)
}

function updateChat() {
    document.getElementById("textarea").innerHTML = ""
    fetch(`http://localhost:${location.port}/ui/check_for_new_messages?chat_id=${chatUpdateId}`)
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log(data)
            for (var i = 1; i < data.length; ++i) {
                if (data[i].user.port === location.port) {
                    document.getElementById("textarea").innerHTML += '<div class="container">'
                        + data[i].data + '<span class="time-right">' + new Date().toLocaleTimeString().slice(0, 5) + '</span></div>'
                } else {
                    document.getElementById("textarea").innerHTML += '<div class="container darker">'
                        + data[i].data + '<span class="time-left">' + new Date().toLocaleTimeString().slice(0, 5) + '</span></div>'
                }
                var element = document.getElementById("text");
                element.scrollTop = element.scrollHeight - element.clientHeight;
            }
        })
}
