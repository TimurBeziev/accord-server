setInterval(function () {
        updateChats();
    }, 250);

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
    document.getElementById("chat_name").innerHTML =
        `<h1 align="center" id="current_chat_info" chat_id=${object.id}> ${object.innerText} </h1>`
}
