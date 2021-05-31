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

function updateChats() {
    fetch(`http://localhost:${location.port}/check_for_new_chats`)
}

function createChat() {
    window.location.replace('/ui/choose_user')
}