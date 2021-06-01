async function joinNetwork() {
    const port = prompt('Введите порт');
    if (port) {
        await fetch(`http://localhost:${location.port}/ui/join_network?port=${port}`)
    }
}

function createChat() {
    window.location.replace('/ui/choose_user')
}

function sendMessage() {
    let chat_id = document.getElementById("current_chat_info").getAttribute("chat_id")
    let data = document.getElementById("input").value
    let timestamp = Date.now()
    fetch(`http://localhost:${location.port}/ui/write_message?data=${data}&chat_id=${chat_id}&timestamp=${timestamp}`)
    document.getElementById("input").value = ""
    if (data) {
        document.getElementById("textarea").innerHTML += '<div class="container">'
            + data + '<span class="time-right">' + new Date().toLocaleTimeString().slice(0, 5) + '</span></div>'
        var element = document.getElementById("text");
        element.scrollTop = element.scrollHeight - element.clientHeight;
    }
}