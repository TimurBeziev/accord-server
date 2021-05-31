function get(){
    let text = document.getElementById("input").value
    document.getElementById("input").value = ""
    if(text)  {
            
      document.getElementById("textarea").innerHTML += '<div class="container">' + text + '<span class="time-right">' + new Date().toLocaleTimeString().slice(0,5) + '</span></div>'
      var element = document.getElementById("text");
      element.scrollTop = element.scrollHeight - element.clientHeight;
    }
}

async function joinNetwork(){
    const port = prompt('Введите порт');
    console.log(`Got port ${port}`);
    console.log(`Out port ${location.port}`);
    if (port) {
        await fetch(`http://localhost:${location.port}/ui/join_network?port=${port}`)
    }
}

function createChat(){
    fetch(`http://localhost:${location.port}/ui/get_available_users`)
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            // window.location.replace('/ui/choose_user')
            console.log(data)
        })
}