function get() {
    let text = document.getElementById("input").value
    document.getElementById("input").value = ""
    if (text) {

        document.getElementById("textarea").innerHTML += '<div class="container">' + text + '<span class="time-right">' + new Date().toLocaleTimeString().slice(0, 5) + '</span></div>'
        var element = document.getElementById("text");
        element.scrollTop = element.scrollHeight - element.clientHeight;
    }
}

async function joinNetwork() {
    const port = prompt('Введите порт');
    if (port) {
        await fetch(`http://localhost:${location.port}/ui/join_network?port=${port}`)
    }
}

<<<<<<< HEAD
function addChat() {
    const name = prompt('Введите название чата');
    if (name) {
        document.getElementById("some_menu").innerHTML += '<div class="menu-container" >' + `${name}` + '</div>'
    }
}

function updateChats() {
    fetch(`http://localhost:${location.port}/check_for_new_chats`)
=======
function createChat() {
    fetch(`http://localhost:${location.port}/ui/get_available_users`)
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            // window.location.replace('/ui/choose_user')
            console.log(data)
        })
}

async function createChatWithUser(user_id) {
    // let user_id = object.getAttribute('id')
    let chat_id = BigInt(Math.floor(Math.random() * 1125899906842624)) // from 0 to 2**50
    await fetch(`http://localhost:${location.port}/ui/create_chat_with_user?user_id=${user_id}&chat_id=${chat_id}`)
>>>>>>> a60ba0af6f05d88d8f77a031b2fc8f5965c2aaa5
}