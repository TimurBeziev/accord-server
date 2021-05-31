function get(){
    let text = document.getElementById("input").value
    document.getElementById("input").value = ""
    if(text)  {
            
      document.getElementById("textarea").innerHTML += '<div class="container">' + text + '<span class="time-right">' + new Date().toLocaleTimeString().slice(0,5) + '</span></div>'
      var element = document.getElementById("text");
      element.scrollTop = element.scrollHeight - element.clientHeight;
    }
}

function connect(){
  const port = prompt('Connect');
  fetch('http://127.0.0.1:5000/connect')
}

function addChat(){
const name = prompt('Chat');
if (name) {
  document.getElementById("some_menu").innerHTML +=  '<div class="menu-container" >' + `${name}` +  '</div>'
}
}