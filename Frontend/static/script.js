const navbar = document.querySelector(".navbar");
const menuButton = document.querySelector(".menu-button");

menuButton.addEventListener("click", () => {
  navbar.classList.toggle("show-menu");
});

const isSegundaPagina = document.body.classList.contains("pagina um");

let count = 1;
document.getElementById("radio1").checked = true;

setInterval(function () {
  nextImage();
}, 5000);

function nextImage() {
  count++;
  if (count > 3) {
    count = 1;
  }
  document.getElementById("radio" + count).checked = true;
}

document
  .getElementById("linkParaOFinal")
  .addEventListener("click", function () {
    window.scrollTo(0, document.body.scrollHeight);
  });

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if this cookie string begins with the name we want
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    const formData = new FormData(form);

    fetch('http://localhost:9090/users/register/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,  // Inclui o token CSRF no cabeçalho
            'Content-Type': 'application/x-www-form-urlencoded' // ou 'application/json' dependendo da sua configuração
        },
        body: new URLSearchParams(formData)  // Transforma o FormData em uma URL-encoded string
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});