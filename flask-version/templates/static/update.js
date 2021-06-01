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
                    `<div class="menu-container" id=${data[i].id}> ${data[i].name} </div>`
            }
        })
}
