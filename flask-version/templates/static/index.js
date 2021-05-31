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

function addChat(){
    const name = prompt('Введите название чата');
    if (name) {
      document.getElementById("some_menu").innerHTML +=  '<div class="menu-container" >' + `${name}` +  '</div>'
    }
}