let input = document.querySelector('#input')
let textarea = document.querySelector('#textarea')
let send = document.querySelector('#send')
let search = document.querySelector('#find')

function message(){
  let text = input.value
  input.value = ''
  if(text)  {
	  var uri_enc = encodeURI(text)
	  var uri_enc = decodeURI(text)
	    
	  textarea.innerHTML += '<div class="container">' + uri_enc.replace(/</g,"&lt;") 
+ '<span class="time-right">' + new Date().toLocaleTimeString().slice(0,5) + '</span></div>'
	  var element = document.getElementById("text");
   	  element.scrollTop = element.scrollHeight - element.clientHeight;    
    }
}

send.addEventListener('click', () => {
  message();
});

send.dispatchEvent(new Event('click'))

input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    send.click();
  }
});

search.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("find").value = ''
  }
});

